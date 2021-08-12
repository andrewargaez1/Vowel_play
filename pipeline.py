import numpy as np
import pandas as pd
import os
import pickle
from parselmouth import Sound, Formant
import parselmouth
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
       
def lst_dir(item):
    dirs = os.listdir(item)
    if '.DS_Store' in dirs:
        dirs.remove('.DS_Store')
    return dirs

def gimme_dat_frequency(path,f, window, threshold):
    lst_s = []
    snd = parselmouth.Sound(path)
    formant = snd.to_formant_burg()
    pch = snd.to_pitch_ac(time_step=formant.dt)
    f0 = pch.selected_array["frequency"]
    T = np.arange(formant.nt)*formant.dt + formant.t1
    form = [formant.get_value_at_time(f, t) for t in T]
    form = np.array(form)[f0[:len(form)]>0][0:]
    for i in range(window,len(form)-(window-1)):
        space = np.array(form[i-window:i+window]).var()
        lst_s.append(space)
    lst_s=np.array(lst_s)
    x = np.array(form)[window:-(window-1)][lst_s<threshold]
    formant_freq = x.mean()
    return round(formant_freq,2)

def gimme_dat_duration(path,f,window,threshold):
    lst_s = []
    formant = parselmouth.Sound(path).to_formant_burg()
    T = np.arange(formant.nt)*formant.dt + formant.t1
    form = [formant.get_value_at_time(f, t) for t in T]
    for i in range(window,len(form)-(window-1)):
        space = np.array(form[i-window:i+window]).var()
        lst_s.append(space)
    lst_s=np.array(lst_s)
    x = np.array(form)[window:-(window-1)][lst_s<threshold]
    dura = len(x)*formant.dt
    return dura

def build_df(yourpath,window,threshold):
    lst = []
    for target in lst_dir(yourpath):
        newpath = yourpath + target
        for gender in lst_dir(newpath):
            agepath = newpath + '/'+ gender
            for age in lst_dir(agepath):
                namepath = agepath + '/'+ age
                for name in lst_dir(namepath):
                    filepath = namepath + '/'+ name
                    for word in lst_dir(filepath):
                        d = {}
                        finalpath = filepath + '/'+ word
                        d['Vowel']= target
                        d['gender']= gender
                        d['age']= age
                        d['word']=word[:-4]
                        d['path']= finalpath
                        lst.append(d)                      
    df = pd.DataFrame(lst)                   
    df['F1'] = df['path'].apply(lambda x: gimme_dat_frequency(x,1,window,threshold))
    df['F2'] = df['path'].apply(lambda x: gimme_dat_frequency(x,2,window,threshold))
    df['Duration'] = df['path'].apply(lambda x: gimme_dat_duration(x,1,window,threshold))
    df = pd.get_dummies(data = df ,columns=['gender'],drop_first='True')
    df.dropna(inplace=True)
    return df

def pickler(name, model):
    with open(str(name) +'.pkl', 'wb') as f:
        pickle.dump(model, f)


def unpickle(name):
    with open(str(name) + '.pkl', 'rb') as f:
        model = pickle.load(f)
        return model

def model_gender(item):
    model = RandomForestClassifier()
    x = item.drop(['age','word','Vowel','path','gender_M'], axis=1)
    y = item.pop('gender_M')
    X_train, X_test, y_train, y_test = train_test_split(x, y,random_state=1)
    model.fit(X_train, y_train)
    return model


def get_data(item):
    data=item.drop(['age','Vowel','path','word'], axis=1)
    labels = item.Vowel
    le = LabelEncoder()
    y = le.fit_transform(labels)
    seen = []
    vowel_label_map = {}
    for label, _y in list(zip(labels, y)):
        if label not in seen:
            vowel_label_map[str(_y)] = label
            seen.append(label)
    return data, y, vowel_label_map

    
def model_vowel(item):
    model= RandomForestClassifier()
    data, y, label_map = get_data(item)
    X_train, X_test, y_train, y_test = train_test_split(data, y,random_state=1)
    model.fit(X_train, y_train)
    return model, label_map


def convert(path, model):
    df1= {}
    df1['F1'] = [gimme_dat_frequency(path,1,6,1100)]
    df1['F2'] = [gimme_dat_frequency(path,2,6,1100)]
    df1['Duration'] = [gimme_dat_duration(path,1,6,1100)]
    df1=pd.DataFrame(df1)
    try:
        df1['gender']= model.predict(df1.iloc[0,:].values.reshape(1,-1))
    except:
        df1['gender']= [1]
    return df1


#if __name__ == '__main__':
    #df = build_df('/Users/andrewargaez/Vowel_play/wav_files/',5,1100)
    #pickler('gherkins/datah')
    #model_g = model_gender(df)
    #pickler('gherkins/gender', model_g)
    
    
    
    #df1 = convert('/Users/andrewargaez/Vowel_play/audio.wav',model_g)
    #model_v, label_map = model_vowel(df)
    #pickler('gherkins/vowel',model_v)

    #score = model_vowel(df)
    #print(score)

    #model = unpickle('gherkins/gender')
    #clean_data = convert('/Users/andrewargaez/Vowel_play/audio_gui/audio157937.wav', model)
    #print(clean_data)
    #print(label_map)
    #model_v = unpickle('gherkins/model_x')
    #guess = model_v.predict(clean_data.iloc[0,:].values.reshape(1,-1))
    #for k, v in list(label_map.items()):
        #if str(guess[0]) == str(k):
            #print(v)

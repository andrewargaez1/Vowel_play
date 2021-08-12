from math import nan
from subprocess import run, PIPE

from flask import logging, Flask, render_template, request
import numpy as np
import sys
import random 

from pipeline import unpickle, convert
sys.path.append('/path/to/ffmpeg')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/audio', methods=['POST'])
def audio():
    filename = 'audio'+str(random.randint(35000,400000))
    with open(f'audio_gui/{filename}.wav', 'wb') as f:
        f.write(request.data)
    model = unpickle('gherkins/gender')
    clean_data = convert(f'/Users/andrewargaez/Vowel_play/audio_gui/{filename}.wav', model)
    print(clean_data)
    model_v = unpickle('gherkins/model_x')
    try:
        guess = model_v.predict(clean_data.iloc[0,:].values.reshape(1,-1))
    except:
        return f" I'm sorry I didn't quite catch that. Can you try again?" 
    certainty = model_v.predict_proba(clean_data.iloc[0,:].values.reshape(1,-1)).max()
    print(guess)
    for k, v in list({'4': 'ɒ', '6': 'ɛ', '5': 'ɔ', '7': 'ɪ', '2': 'u', '0': 'i', '1': 'o', '9': 'ʌ', '8': 'ʊ', '3': 'æ'}.items()):
        if str(guess[0]) == str(k):
            print(v)
            return f' {str(clean_data)}\n Vowel:    {str(v)} \n I am {str(round((certainty*100),2))}% sure that this is the vowel'
    return f" I'm sorry I didn't quite catch that. Can you try again?" 



if __name__ == "__main__":
    #app.logger = logging.getLogger('audio-gui')
    app.run(debug=True)
    

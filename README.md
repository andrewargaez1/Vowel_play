# Vowel_play
Vowels are the nucleus of every sylable. If we can identify vowels we can go a long way towards being able to identify speach audio. I have a degree in linguistics from the University of Arizona. A large part of linguistics is phonetics, the study of how humans produce and perceive sounds. A method of this study of sounds is looking at spectograms. With some studying one can look at a spectogram and see what sounds are being made. In a spectrogram, time is always represented on the x-axis and frequency on the y-axis. Intensity is depicted by the relative darkness of the frequencies shown. Vowels are very distinct when looking at a spectogram. The dark lines that stretch across the spectogram are voiced segments. What that means is that your glottis is engaged when producing the sound. The source of sound for speech is the glottis, air passing through and on the other side of the vibrating vocal folds is excited by the opening and closing movements. All vowels are voiced so they show up as dark lines on the spectograms. The technical term for these dark voice segments are formants. Looking at the spectogram we see multiple formant stacked on top of each other. There are two formants that tell us which vowel that is being produced. They are formants 1 and 2 the bottom most formants that you see in the figure below. The relationship between these two formants will be the crux of how I am able to properly classify vowels.  

<img width="301" alt="keep" src="https://user-images.githubusercontent.com/60011848/129136847-ed5f5cff-620a-4f04-876c-abef3130ac25.png">

So a little more about these formants and how they are produced and calculated. Before the air can exit the mouth the air must pass through the vocal tract, which acts as a filter (or resonator) that suppresses or damps some frequencies while intensifying others. Which frequencies get damped and which intensified depends on the shape of the vocal tract at a given point in time. The frequencies that are intensified are the formants that we see on a spectrogram and represent the sounds that resonate the loudest in the particular filter formed by the vocal tract.


# Formant 1 (F1)
The first formant (F1) in vowels is inversely related to vowel height the higher the vowel, the lower the first formant (and vice versa).

              High      [i]~[u]>F1 ≈ 280~310
              Mid-high  [I]~[ʊ]>F1 ≈ 400~450
              Mid-low   [ɛ]~[ɔ]>F1 ≈ 550~590
              Low       [æ]~[ɒ]>F1 ≈ 690~710

<img width="1173" alt="Screen Shot 2021-08-12 at 8 40 01 AM" src="https://user-images.githubusercontent.com/60011848/129226302-207da565-4b86-4cae-90a2-86fe79342beb.png">

<img width="1160" alt="Screen Shot 2021-08-12 at 9 53 59 AM" src="https://user-images.githubusercontent.com/60011848/129237592-78258b04-513e-493b-b528-a21907ef6416.png">


Red = high vowels, low F1 Blue = mid/low vowels, higher F1

# Formant 2 (F2)
The second formant (F2) in vowels is somewhat related to degree of backness. The more front the vowel, the higher the second formant (but affected by lip-rounding).

              Front     Back
              [i] ~ [u] >F2≈2250~870
              [I] ~ [ʊ] >F2≈1920~1030
              [ɛ] ~ [ɔ] >F2≈1770~880
              [æ] ~ [ɒ] >F2≈1660~1100
     
<img width="1172" alt="Screen Shot 2021-08-12 at 9 57 26 AM" src="https://user-images.githubusercontent.com/60011848/129237482-90c04b8e-3c70-422a-86e8-157c662a0dbe.png">

<img width="1165" alt="Screen Shot 2021-08-12 at 9 45 50 AM" src="https://user-images.githubusercontent.com/60011848/129236012-7ac7d96b-551b-4497-8502-6d98b378cce8.png">

Red = front vowels, higher F2 Purple = back vowels, lower F2

# F1, F2 relationship

The distance between F1 and F2 is a better predictor of degree of backness in vowels.The closer F1 and F2 are to each other, the more back a vowel is.
               
                   F1 F2              F1  F2 
              [i] 280 2250        [u] 310 870 
              [I] 400 1920        [ʊ] 450 1030 
              [ɛ] 550 1770        [ɔ] 590 880 
              [æ] 690 1660        [ɒ] 710 1100

<img width="1178" alt="Screen Shot 2021-08-12 at 10 06 07 AM" src="https://user-images.githubusercontent.com/60011848/129238898-f730d854-03b9-490e-8c98-1cedc8d3b208.png">

<img width="1161" alt="Screen Shot 2021-08-12 at 10 04 26 AM" src="https://user-images.githubusercontent.com/60011848/129238876-ee637baa-1019-4600-8f44-1fa315648395.png">

Yellow = front vowels, Orange = back vowels, further apart F1-F2 closer F1-F2

# Data

In order to do the project in the week and a half I was given, I needed to set realistic goals. I decided that in the given time I would be able to create a model that classify vowels from monosylabic words. In order to accomplish this I needed to have a good data set. After a prolonged search I was unable to find any, so I decided to make my own dataset. I created a list of 200 monosylabic words, every 20 words isolated a specific vowel. I did my best to very the enviroments of the vowels so that way my model could account for the variance of diferent onsets and coda. In the week and a half I was able to collect a data set of 8,000 recordings. The age range of the participants were from 24-62. I did my best to get a good distrobution in age particpants but that proved to be difficult in such a short amount of time. The split between male and femal contributers was close to an even split 19 females and 21 males. 

# Methodology
              
The figure below shows a couple different things. The first thing is on the left side that shows the spectograms of the words kit, keep, court, and cod. The red dots that are overlayed on the formants is one of the functionalities of Praat. If it is a capability of Praat it is a capablility of Parselmouth. I first process the audio file as a spectogram that is represented as an array. Then using .formant it extracts the frequency of the formant as an array. The difficulty is that in both Praat and therefore Parselmouth it requires either manually croping the desired section or manually noteing the start and end time of the section. I did not have the luxury of noteing or cropping each of my 8,000 audio files. My solution to this problem was to write an algorithim that would create a window the size of my choosing and slide across the array of formants checking the variance. If the variance was under the threshold I set as my paramater the points would be appended into a new list. 


<img width="1792" alt="Screen Shot 2021-08-11 at 9 45 21 PM" src="https://user-images.githubusercontent.com/60011848/129139477-fec987e9-5869-40aa-950b-7b66d18c8ade.png">

# Feature Engineering
From looking at the top F1 and F2 relationship was going to be the most important features. Looking at the graph below we already see that they group just by being F1 and F2. 

<img width="999" alt="Screen Shot 2021-08-11 at 9 42 27 PM" src="https://user-images.githubusercontent.com/60011848/129139303-ef104c7e-2666-445f-9d1a-a5a014ef0139.png">
              
Gender played a vital part in my models performance. Knowing the gender of the speaker improved my models accuracy by 5%. Looking at the average F1 and F2 feequency for each gender we see there is a clear distinction. The char below shows a that the male speakers spoke at about 200Hz lower than females. It was so vital of a feature I trained a model to predict the gender in my app so that way I made sure to have the feature incorporated. 

<img width="920" alt="Screen Shot 2021-08-12 at 10 19 59 AM" src="https://user-images.githubusercontent.com/60011848/129240472-9cebfe27-0c54-4780-beef-8ff64fb579dc.png">

The vowels duration was also a vauable feature. The difference between long and short vowels are known vowels like i,æ,u,ɔ are known as long vowels. The short vowels are as follows:I,ɛ,ʊ,ɒ,^,o. This feature increased my models performance by 3%

<img width="446" alt="Screen Shot 2021-08-12 at 10 29 51 AM" src="https://user-images.githubusercontent.com/60011848/129241853-447af470-6bb1-44c6-ad75-b47e51db271d.png">

# Model Selection

With a baseline of 10% all the models performed comparibly well but Random Forest out performed the rest of the models with an accuracy score of 60.3%.

<img width="1191" alt="Screen Shot 2021-08-12 at 10 34 57 AM" src="https://user-images.githubusercontent.com/60011848/129242601-a07d6469-faa5-46b8-96f5-6187198df027.png">

# Conclusion

In the end my model is able to classify the vowel fairly regularly given a good audio sample with minimal white noise. Certain vowels are easier to identify for it than others. I  would like to connect this to a database so that way anytime someone used my application it would conintue its learning. When I had only 25 participants recorded my model was hovering at 53% accuracy. once I added another 15 my model jumped nearly 10%. Not ever data set improved my model, but overall it was a positive trend. I would also like to add the capability for the user to review the models categorization and correct it before it is stored in the data base. Being able to identify the vowel in words can be highly varied and in different enviroments if a model is able to consistantly identify the vowel in words it will go a long way towards accurate speach processing. 

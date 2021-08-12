# Vowel_play
Vowels are the nucleus of every sylable. If we can identify vowels we can go a long way towards being able to identify speach audio. I have a degree in linguistics from the University of Arizona. A large part of linguistics is phonetics, the study of how humans produce and perceive sounds. A method of this study of sounds is looking at spectograms. With some studying one can look at a spectogram and see what sounds are being made. In a spectrogram, time is always represented on the x-axis and frequency on the y-axis. Intensity is depicted by the relative darkness of the frequencies shown. Vowels are very distinct when looking at a spectogram. The dark lines that stretch across the spectogram are voiced segments. What that means is that your glottis is engaged when producing the sound. The source of sound for speech is the glottis, air passing through and on the other side of the vibrating vocal folds is excited by the opening and closing movements. All vowels are voiced so they show up as dark lines on the spectograms. The technical term for these dark voice segments are formants. Looking at the spectogram we see multiple formant stacked on top of each other. There are two formants that tell us which vowel that is being produced. They are formants 1 and 2 the bottom most formants that you see in the figure below. The relationship between these two formants will be the crux of how I am able to properly classify vowels.  

<img width="301" alt="keep" src="https://user-images.githubusercontent.com/60011848/129136847-ed5f5cff-620a-4f04-876c-abef3130ac25.png">

So a little more about these formants and how they are produced and calculated. Before the air can exit the mouth the air must pass through the vocal tract, which acts as a filter (or resonator) that suppresses or damps some frequencies while intensifying others. Which frequencies get damped and which intensified depends on the shape of the vocal tract at a given point in time. The frequencies that are intensified are the formants that we see on a spectrogram and represent the sounds that resonate the loudest in the particular filter formed by the vocal tract.

The first formant (F1) in vowels is inversely related to vowel height the higher the vowel, the lower the first formant (and vice versa).

              High      [i]~[u]>F1 ≈ 280~310
              Mid-high  [I]~[ʊ]>F1 ≈ 400~450
              Mid-low   [ɛ]~[ɔ]>F1 ≈ 550~590
              Low       [æ]~[ɒ]>F1 ≈ 690~710


The second formant (F2) in vowels is somewhat related to degree of backness. The more front the vowel, the higher the second formant (but affected by lip-rounding).

              Front     Back
              [i] ~ [u] >F2≈2250~870
              [I] ~ [ʊ] >F2≈1920~1030
              [ɛ] ~ [ɔ] >F2≈1770~880
              [Q] ~ [ɒ] >F2≈1660~1100

The distance between F1 and F2 is a better predictor of degree of backness in vowels.The closer F1 and F2 are to each other, the more back a vowel is.
               
                   F1 F2              F1  F2 
              [i] 280 2250        [u] 310 870 
              [I] 400 1920        [ʊ] 450 1030 
              [ɛ] 550 1770        [ɔ] 590 880 
              [æ] 690 1660        [ɒ] 710 1100
              
The figure below shows a couple different things. The first thing is on the left side that shows the spectograms of the words kit, keep, court, and cod. The red dots that are overlayed on the formants is one of the functionalities of Praat. If it is a capability of Praat it is a capablility of Parselmouth. I first process the audio file as a spectogram that is represented as an array. Then using .formant it extracts the frequency of the formant as an array. The difficulty is that in both Praat and therefore Parselmouth it requires either manually croping the desired section or manually noteing the start and end time of the section. I did not have the luxury of noteing or cropping each of my 8,000 audio files. My solution to this problem was to write an algorithim that would create a window the size of my choosing and slide across the array of formants checking the variance. If the variance was under the threshold I set as my paramater the points would be appended into a new list. 


<img width="1792" alt="Screen Shot 2021-08-11 at 9 45 21 PM" src="https://user-images.githubusercontent.com/60011848/129139477-fec987e9-5869-40aa-950b-7b66d18c8ade.png">

<img width="999" alt="Screen Shot 2021-08-11 at 9 42 27 PM" src="https://user-images.githubusercontent.com/60011848/129139303-ef104c7e-2666-445f-9d1a-a5a014ef0139.png">
              

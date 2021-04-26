import speech_recognition as sr
import cv2
import sounddevice as sd
import soundfile as sf
import csv
import time
my_dict = {}
# get audio from the microphone
r = sr.Recognizer()
duration = 3.2  # seconds
filename = 'myfile.wav'
fs=48000
sd.default.samplerate = 48000
with sr.Microphone(chunk_size = 2048,sample_rate = 48000) as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    while True:
        print("Do you want to continue?")
        a=input("Y/N: ")
        if(a=="y" or a=="Y" or a==""):
            print("Roll No:")
            #time.sleep(1)
            myrecording = sd.rec(int(duration * fs), channels=2,blocking=True)
            sf.write(filename,myrecording,fs)
            
            with sr.AudioFile(filename) as source:
                #reads the audio file. Here we use record instead of
                #listen
                audio = r.record(source)

            try:
                #print("In")
                rno=r.recognize_google(audio)
                try:
                    print(int(rno))
                except:
                	print("Try Again")
                	continue

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                print("Try Again")
                continue

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                print("Try Again")
                continue

            print("Marks:")
            #time.sleep(2)
            myrecording = sd.rec(int(duration * fs), channels=2,blocking=True)
            sf.write(filename,myrecording,fs)
            #print("Saved!!")
            with sr.AudioFile(filename) as source:
                #reads the audio file. Here we use record instead of
                #listen
                audio = r.record(source)

            try:
                marks=r.recognize_google(audio)
                try:
                    print(int(marks))
                except:
                    print("Try Again")
                    continue

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                print("Try Again")
                continue

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            my_dict[rno]=marks
        else:
            with open('test.csv', 'w') as f:
                for key in my_dict.keys():
                    f.write("%s,%s\n"%(key,my_dict[key]))
            print("Saved!!")
            break

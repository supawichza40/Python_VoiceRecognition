

#My first voice recognition program
import speech_recognition as sr
import os
counter = 0
recognizer_instance = sr.Recognizer()

test_data = sr.AudioFile("test_data.wav")
#1234 hello world
# test_data = sr.AudioFile("audio_files_jackhammer.wav")
#the snail smell of old gear vendors.
print(os.getcwd())
with test_data as source:
    recognizer_instance.adjust_for_ambient_noise(source,duration = 0.5)

    audio = recognizer_instance.record(source)
    

output = recognizer_instance.recognize_google(audio)
print(output)


microphone = sr.Microphone()



# Check a list of the microphone
for x in sr.Microphone.list_microphone_names():
   print(counter,x)
   counter+=1




#Test first microphone interpreter
#print("Please speak into the microphone.")
#with mic as source:
#    audio = recognizer_instance.listen(source)
#    recognizer_instance.adjust_for_ambient_noise(source)
#    print("Converting your voice into text,please wait..")
#    print(recognizer_instance.recognize_google(audio))

time = 0

while True:
    try:
        try:
            mic_index = input("What is the index of the microphone, you would like to use?")
            mic = sr.Microphone(device_index=1)
            with mic as source:
                print("Please speak into the microphone")
                audio = recognizer_instance.listen(source)
            
                recognizer_instance.adjust_for_ambient_noise(source,duration = time)
                print(recognizer_instance.recognize_google((audio)))



    
        except :
            print("Invalid input to microphone, please try again")

    except:
        print("Invalid index of microphone, please try again")
    

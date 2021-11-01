

#My first voice recognition program
import speech_recognition as sr
counter = 0
recognizer_instance = sr.Recognizer()

#test_data = sr.AudioFile("test_data.wav")
#1234 hello world
test_data = sr.AudioFile("audio_files_jackhammer.wav")
#the snail smell of old gear vendors.
with test_data as source:
    recognizer_instance.adjust_for_ambient_noise(source,duration = 0.5)

    audio = recognizer_instance.record(source)
    

output = recognizer_instance.recognize_google(audio)
print(output)


microphone = sr.Microphone()



#Check a list of the microphone
#for x in sr.Microphone.list_microphone_names():
#    print(counter,x)
#    counter+=1

lst_mic = sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=1)

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
        with mic as source:
            print("Please speak into the microphone")
            audio = recognizer_instance.listen(source)
            for _ in range(31):
                recognizer_instance.adjust_for_ambient_noise(source,duration = time)

                print("time = {0} output = {1}".format(time,recognizer_instance.recognize_google(audio)))
                time = time + 0.1


    
    except :
        print("Invalid input to microphone, please try again")


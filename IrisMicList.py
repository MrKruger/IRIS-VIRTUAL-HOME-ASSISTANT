import speech_recognition as SR

mic_list = SR.Microphone.list_microphone_names()

for m in mic_list:
	print (m)

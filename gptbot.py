#For chatbot Material
import speech_recognition as sr
import pyttsx3
import openai
import sys

openai.api_key = "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"
def my_bot():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)

    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    conversation = ""
    user_name = "You"
    bot_name = "Rio"

    while True:
        with mic as source:
            print("\n Listening...")
            r.energy_threshold=5000
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
        print("no longer listening")

        try:
            user_input = r.recognize_google(audio)
        except:
            continue

        prompt = user_name+":"+user_input + "\n"+bot_name+":"
        conversation += prompt

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=conversation,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str =response_str.split(user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

        conversation+= response_str +"\n"
        print(response_str)

        engine.say(response_str)
        engine.runAndWait()

        if "goodbye" in user_input.lower():
            break

my_bot()
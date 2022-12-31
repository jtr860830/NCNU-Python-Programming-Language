import tempfile
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer, USEREVENT, display, event
from googletrans import Translator


def main():
    with open("./news.txt", encoding="utf-8") as file:
        news = [line for line in file]
    mixer.init()
    display.init()
    sr_flag = True
    idx = 0
    while True:
        for e in event.get():
            if e.type == USEREVENT:
                sr_flag = True

        if sr_flag:
            with sr.Microphone() as input:
                print("speak command")
                r = sr.Recognizer()
                r.energy_threshold = 4000
                audio = r.listen(input)
                text = r.recognize_google(audio, language="zh-TW")
                print(text)

                if "讀報" in text:
                    speak(news[idx], "zh-TW")
                    sr_flag = False
                elif "英文" in text:
                    lang = "en"
                    translated_news = translate(news[idx], lang)
                    speak(translated_news, lang)
                    sr_flag = False
                elif "日文" in text:
                    lang = "ja"
                    translated_news = translate(news[idx], lang)
                    speak(translated_news, lang)
                    sr_flag = False
                elif "韓文" in text:
                    lang = "ko"
                    translated_news = translate(news[idx], lang)
                    speak(translated_news, lang)
                    sr_flag = False
                elif "印尼" in text:
                    lang = "id"
                    translated_news = translate(news[idx], lang)
                    speak(translated_news, lang)
                    sr_flag = False
                elif "德文" in text:
                    lang = "de"
                    translated_news = translate(news[idx], lang)
                    speak(translated_news, lang)
                    sr_flag = False
                elif "下一篇" in text:
                    idx = idx + 1 if idx < len(news) - 1 else 0
                elif "上一篇" in text:
                    idx = idx - 1 if idx > 0 else len(news) - 1
                elif "結束" in text or "停止" in text:
                    break
                else:
                    print("invalid command")
                    sr_flag = False


def speak(content, lang):
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        gTTS(content, lang=lang).save(tmp.name)
        mixer.music.load(tmp.name)
        mixer.music.set_endevent(USEREVENT)
        mixer.music.play()


def translate(content, lang):
    return Translator().translate(content, lang).text


if __name__ == "__main__":
    main()

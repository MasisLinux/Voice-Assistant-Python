# Милена ассистент BETA версия 1.2.0
# Библиотеки распознавания и синтеза речи
import speech_recognition as sr
from gtts import gTTS

# Воспроизведение речи
import pygame
from pygame import mixer
mixer.init()

import os
import sys
import time
import datetime
import logging
import webbrowser
import subprocess


class Speech_AI:

    def __init__(self):
        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()

        
        now_time = datetime.datetime.now()
        self._mp3_name = now_time.strftime("%d%m%Y%I%M%S")+".mp3"
        self._mp3_nameold='111'

    def work(self):
        print("Минутку тишины, пожалуйста...")
        with self._microphone as source:
            self._recognizer.adjust_for_ambient_noise(source)

        try:
            while True:
                print("Скажи что - нибудь!")
                with self._microphone as source:
                    audio = self._recognizer.listen(source)
                print("Понял, идет распознавание...")
                try:
                    statement = self._recognizer.recognize_google(audio, language="ru_RU")
                    statement=statement.lower()

                    # Команды для открытия различных внешних приложений

                    if((statement.find("калькулятор")!=-1) or (statement.find("calculator")!=-1)):
                        self.osrun('calc')
                               
                    if((statement.find("блокнот")!=-1) or (statement.find("notepad")!=-1)):
                        self.osrun('notepad')
                             
                    if((statement.find("paint")!=-1) or (statement.find("паинт")!=-1)):
                        self.osrun('mspaint')

                    if((statement.find("browser")!=-1) or (statement.find("браузер")!=-1)):
                        self.openurl('http://google.ru', 'Открываю браузер')
                    
                    if((statement.find("camera")!=-1) or (statement.find("камера")!=-1)):
                        self.osrun('camera')
                    

                    # Команды для открытия URL в браузере
                    
                    if(((statement.find("youtube")!=-1) or (statement.find("youtub")!=-1) or (statement.find("ютуб")!=-1) or (statement.find("you tube")!=-1)) and (statement.find("смотреть")==-1)):                        
                        self.openurl('http://youtube.com', 'Открываю ютуб')
 
                    if((statement.find("новости в россии")!=-1) or (statement.find("новости россии")!=-1) or (statement.find("российские новости")!=-1) or (statement.find("новости российские")!=-1)):
                        self.openurl('https://lenta.ru/rubrics/russia/', 'Открываю новости в России')

                    if((statement.find("новости в армении на русском")!=-1) or (statement.find("новость в армении на руском")!=-1) or (statement.find("на усть")!=-1)):
                        self.openurl('https://news.am/rus/', 'Открываю новости в Армении на русском')
                    
                    if((statement.find("новости в армении на армянском")!=-1) or (statement.find("новость в армении на армянском")!=-1)):
                        self.openurl('https://news.am/arm/', 'Открываю новости в Армении на армянском')
                         
                    if((statement.find("mail")!=-1) or (statement.find("майл")!=-1)):
                        self.openurl('https://e.mail.ru/messages/inbox/', 'Открываю почту')
                        
                    if((statement.find("вконтакте")!=-1) or (statement.find("в контакте")!=-1)):
                        self.openurl('http://vk.com', 'Открываю Вконтакте')
                        
                    if((statement.find("инстаграм")!=-1) or (statement.find("instagram")!=-1) or (statement.find("Instagram")!=-1) or (statement.find("Insta")!=-1) or (statement.find("Инста")!=-1) or (statement.find("открой инсту")!=-1)):
                        self.openurl('https://www.instagram.com', 'Открываю Инстаграм ')
                    
                    if((statement.find("facebook")!=-1) or (statement.find("открой фейсбук")!=-1) or (statement.find("fb")!=-1) or(statement.find("ефбе")!=-1) or (statement.find("open facebook")!=-1) or (statement.find("фб")!=-1) or (statement.find("фасебук")!=-1) or (statement.find("facebuk")!=-1)):
                        self.openurl('https://www.facebook.com/', 'Открываю Фейсбук')
                    
                    if((statement.find("twiiter")!=-1) or (statement.find("twiter")!=-1) or (statement.find("twitter")!=-1)):
                        self.openurl('https://twitter.com/', 'Открываю twitter')

                    if((statement.find("линкедин")!=-1) or (statement.find("линкед ин")!=-1) or (statement.find("linkedin")!=-1) or (statement.find("открой линкедин")!=-1) or (statement.find("open linkedin")!=-1) or (statement.find("open linked in")!=-1) or (statement.find("открой линкедин")!=-1) or (statement.find("открой линкед ин")!=-1)):
                        self.openurl('https://www.linkedin.com/', 'Открываю Линкедин')

                    # Команды для поиска в сети интернет             


                    if((statement.find("найти")!=-1) or (statement.find("поиск")!=-1) or (statement.find("найди")!=-1) or (statement.find("дайте")!=-1) or (statement.find("mighty")!=-1)):
                        statement=statement.replace('найди', '')
                        statement=statement.replace('найти', '')
                        statement=statement.strip()
                        self.openurl('https://www.google.ru/search?q=' + statement, "Я нашла следующие результаты")
                        
                    if((statement.find("смотреть")!=-1) and ((statement.find("фильм")!=-1) or (statement.find("film")!=-1))):
                        statement=statement.replace('посмотреть', '')
                        statement=statement.replace('смотреть', '')
                        statement=statement.replace('хочу', '')
                        statement=statement.replace('фильм', '')
                        statement=statement.replace('film', '')
                        statement=statement.strip()
                        self.openurl('https://www.google.com/search?q=%D0%A1%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C+%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD+%D1%84%D0%B8%D0%BB%D1%8C%D0%BC+' + statement, "Выберите сайт где смотреть фильм")

                    if(((statement.find("youtube")!=-1) or (statement.find("ютуб")!=-1) or (statement.find("you tube")!=-1)) and (statement.find("смотреть")!=-1)):
                        statement=statement.replace('хочу', '')
                        statement=statement.replace('на ютубе', '')
                        statement=statement.replace('на ютуб', '')
                        statement=statement.replace('на youtube', '')
                        statement=statement.replace('на you tube', '')
                        statement=statement.replace('на youtub', '')
                        statement=statement.replace('youtube', '')
                        statement=statement.replace('ютуб', '')
                        statement=statement.replace('ютубе', '')
                        statement=statement.replace('посмотреть', '')
                        statement=statement.replace('смотреть', '')
                        statement=statement.strip()
                        self.openurl('http://www.youtube.com/results?search_query=' + statement,  'Ищу в ютуб')


                    if((statement.find("слушать")!=-1) and (statement.find("песн")!=-1)):
                        statement=statement.replace('песню', '')
                        statement=statement.replace('песни', '')
                        statement=statement.replace('песня', '')
                        statement=statement.replace('песней', '')
                        statement=statement.replace('послушать', '')
                        statement=statement.replace('слушать', '')
                        statement=statement.replace('хочу', '')
                        statement=statement.strip()
                        self.openurl('https://my.mail.ru/music/search/' + statement, "Нажмите плэй")

                    # сказать текущее время
                     
                    if((statement.find("Milena")!=-1) or (statement.find("milena")!=-1) or (statement.find("Милена")!=-1) or (statement.find("милена")!=-1) and (statement.find("время")!=-1) or (statement.find("time")!=-1) or (statement.find("который час")!=-1) or (statement.find("сколько часов")!=-1) or (statement.find("сколько чисов")!=-1) or (statement.find("сколько чсов")!=-1) or (statement.find("сколько времени")!=-1) or (statement.find("сколько времени милена")!=-1)):
                        now = datetime.datetime.now()
                        self.say("Сейчас " + str(now.hour) + ":" + str(now.minute))  

                    # сказать текущею дату
                    
                    if((statement.find("Milena")!=-1) or (statement.find("milena")!=-1) or (statement.find("Милена")!=-1) or (statement.find("милена")!=-1) and (statement.find("скажи дату")!=-1) or (statement.find("data")!=-1) or (statement.find("дата")!=-1)):
                        now = datetime.datetime.now()
                        self.say("Сейчас " + str(now.month) + "/" + str(now.day) + "/" + str(now.year)) 

                    # Режым (расскажи анекдот)
                    
                    if((statement.find("расскажи анекдот про водку")!=-1) or (statement.find("расзкажи анекдот про водку")!=-1) or (statement.find("расмеши меня аникдотами про водку")!=-1) or (statement.find("расмиши миня аникдотами про водку")!=-1) or (statement.find("анекдот про водку")!=-1) or (statement.find("анекдоти про водку")!=-1) or (statement.find("анекдоты про водку")!=-1)):
                        self.say("Ладно Слушай внимательно")
                        self.say("— Да пошел ты в бизнес! — сказал директор школы пьяному трудовику. — Вовочка, учительница жалуется, что ты играешь в карты на деньги.— А на что, спрашивается, ты покупаешь себе водку?— Да ладно, я что, против? Ты только учительницу не обыгрывай сильно. Пьют два алкоголика метиловый спирт.Один из них встает и говорит: «Пойдем домой, ХА ХА ХА !  …")

                    if((statement.find("расскажи анекдот про бизнес")!=-1) or (statement.find("расзкажи анекдот про бизнез")!=-1) or (statement.find("расмеши меня аникдотами про бизнеса")!=-1) or (statement.find("расмиши миня аникдотами про бизнса")!=-1) or (statement.find("анекдот про бизнеса")!=-1) or (statement.find("анекдоти про бзнеса")!=-1) or (statement.find("анекдоты про бизнес")!=-1) or (statement.find("анекдот про бизнес")!=-1)):
                        self.say("Ладно Слушай внимательно")                    
                        self.say("Встречаются как-то два бизнес-тренера и один другого спрашивает: — Как увеличить продажи? — Могу рассказать... — Рассказать и я могу!, как увеличить? ХА ХА ХА !")
                    
                    if((statement.find("расскажи анекдот про коронавирус")!=-1) or (statement.find("расзкажи анекдот про карнавирус")!=-1) or (statement.find("расмеши меня аникдотами про коронавируса")!=-1) or (statement.find("расмиши миня аникдотами про коронавируса")!=-1) or (statement.find("анекдот про коронавируса")!=-1) or (statement.find("анекдоти про коронавирус")!=-1) or (statement.find("анекдоты про коронавирус")!=-1) or (statement.find("анекдот про коронавирус")!=-1)):
                        self.say("Ладно Слушай внимательно")
                        self.say("- Алло, дорогая, я в магазине. Что брать?- Ты в маске?- Да.- Бери кассу. ХА ХА ХА!")

                    if((statement.find("расскажи анекдот про воров")!=-1) or (statement.find("расзкажи анекдот варов")!=-1)):
                        self.say("Окей")
                        self.say("Увидев на холодильнике всего два магнитика — из Магадана и Воркуты, воры покормили кошку и помыли посуду. ХА ХА ХА!")

                    # Поддержание диалога

                    if((statement.find("Hello")!=-1) or (statement.find("Hi")!=-1) or (statement.find("hello")!=-1) or (statement.find("hi")!=-1) or (statement.find("привет")!=-1) or (statement.find("приветики")!=-1) or (statement.find("прив")!=-1) or (statement.find("хелло")!=-1) or (statement.find("хаи")!=-1) or (statement.find("хло")!=-1) or (statement.find("алоха")!=-1) or (statement.find("hola")!=-1) or (statement.find("aloha")!=-1)):
                        self.say("Привет! чем могу вам помочь?")

                    # if((statement.find("нормально")!=-1) or (statement.find("нармально")!=-1) or (statement.find("прекрсно")!=-1)):
                    #     self.say("круто!")
                        
                    # if((statement.find("норм а у тебя")!=-1) or (statement.find("нормально а у тебя")!=-1) or (statement.find("хорошо а у тебя")!=-1) or (statement.find("хорошо. спасибо а у тебя")!=-1)):
                    #     self.say("Нормально, спасибо!")

                    # if((statement.find("плохо")!=-1) or (statement.find("очень плохо")!=-1)):
                    #     self.say("почему?")

                    if((statement.find("What is your name")!=-1) or (statement.find("как тебя зовут")!=-1) or (statement.find("как тебя завут")!=-1) or (statement.find("what is your name")!=-1)):
                        self.say("Милена. Очень приятнo")

                    if((statement.find("How old are you")!=-1) or (statement.find("Сколько тебе лет")!=-1) or (statement.find("how old are you")!=-1) or (statement.find("сколько тебе лет")!=-1)):
                        self.say("Я родилась в 10/04/2020")                                                

                    if((statement.find("кто создал тебя")!=-1) or (statement.find("кто тебя создавал")!=-1) or (statement.find("кто создавал тебя")!=-1) or (statement.find("кто тебя создал или создала")!=-1) or (statement.find("кто тебя создавал или создавала")!=-1) or (statement.find("кто тебя создал")!=-1)):
                        self.say("Меня создал Масис Осипян!")

                    

                    if((statement.find("перейди на гитхаб аккаунт твоего создателя")!=-1) or (statement.find("перейди на гитхаб аккаунт тваево создателя")!=-1) or (statement.find("перейди на github аккаунт тваего создателя")!=-1) or (statement.find("открой гитхаб акаунт таваего создателя")!=-1) or (statement.find("открой github аккаунт тваего создателя")!=-1) or (statement.find("открой гитхаб аккаунт таваего создателя")!=-1) or (statement.find("открой github акаунт тваего создателя")!=-1)):
                        self.openurl('https://github.com/MasisLinux', 'Открываю Гитхаб аккаунт моего создателя')

                    if((statement.find("перейди на фейсбук аккаунт твоего создателя")!=-1) or (statement.find("перейди на facebook аккаунт твоего создателя")!=-1) or (statement.find("перейди на facebuk аккаунт твоего создателя")!=-1) or (statement.find("перейди на fb аккаунт твоего создателя")!=-1) or (statement.find("перейди на фасебук аккаунт твоего создателя")!=-1) or (statement.find("перейди на фб аккаунт твоего создателя")!=-1) or (statement.find("перейди на ефб аккаунт твоего создателя")!=-1) or (statement.find("перейди на ефбе аккаунт твоего создателя")!=-1)):
                        self.openurl('https://www.facebook.com/masis.osipyan.31', 'Открываю Фейсбук аккаунт моего создателя')

                    if((statement.find("перейди на instagram аккаунт твоего создателя")!=-1) or (statement.find("перейди на инстаграм аккаунт твоего создателя")!=-1) or (statement.find("перейди на инсту твоего создателя")!=-1) or (statement.find("перейди на инст аккаунт твоего создателя")!=-1)):
                        self.openurl('https://www.instagram.com/masis_0000_/', 'Открываю Инстаграм аккаунт моего создателя')

                    if((statement.find("как дела")!=-1) or (statement.find("how are you")!=-1)):
                        self.say("норм. А у тебя?")

                    if((statement.find("молодец")!=-1) or (statement.find("маладец")!=-1) or (statement.find("milena молодец")!=-1) or(statement.find("милена молодец")!=-1) or (statement.find("молодец милена")!=-1) or (statement.find("молодец milena")!=-1) or (statement.find("молодчина")!=-1) or (statement.find("маладчина")!=-1)):
                        self.say("Спасибо!")

                    if((statement.find("спасибо милена")!=-1) or (statement.find("спасибо")!=-1) or (statement.find("спс")!=-1) or (statement.find("милена спасибо")!=-1) or (statement.find("милена спс")!=-1) or (statement.find("спс милена")!=-1)):
                        self.say("Связись если что!")

                    # Оканчание диалога

                    if((statement.find("до свидания")!=-1) or (statement.find("досвидания")!=-1) or (statement.find("пока")!=-1)):
                        answer = "Пока!"
                        self.say(str(answer))
                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1) 
                        sys.exit()
                    
                    print("Вы сказали: {}".format(statement))
                    
                except sr.UnknownValueError:
                    print("Упс! Кажется, я тебя не поняла, повтори еще раз")
                except sr.RequestError as e:
                    print("Не могу получить данные от сервиса Google Speech Recognition; {0}".format(e))
        except KeyboardInterrupt:
            self._clean_up()
            print("Пока!")
        
    def osrun(self, cmd):
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

    def openurl(self, url, ans):
        webbrowser.open(url)
        self.say(str(ans))
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    def say(self, phrase):
        tts = gTTS(text=phrase, lang="ru")
        tts.save(self._mp3_name)

        # Play answer
        mixer.music.load(self._mp3_name)
        mixer.music.play()
        if(os.path.exists(self._mp3_nameold)):
            os.remove(self._mp3_nameold)
       
        now_time = datetime.datetime.now()
        self._mp3_nameold=self._mp3_name
        self._mp3_name = now_time.strftime("%d%m%Y%I%M%S")+".mp3"
        
        
    

    def _clean_up(self):
        def clean_up():
            os.remove(self._mp3_name)


def main():
    ai = Speech_AI()
    ai.work()


main()


# ОБНАВЛЕНО В 4/01/2021
# СОЗДАНО В 10/04/2020
# СОЗДАТЕЛЬ ꧁ ༒_M_A_S_I_S_༒ ꧂

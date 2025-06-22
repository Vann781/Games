from play_vid import *   # here we are importing every function in play_vid file.
import random  # ye hume random funtion use karne deta hai jis se random value utha sakte hai 
import speech_recognition as sr  # library installed that takes user input from mic
import time  # sleep funtion use karne ke liye 
from playsound import playsound

r = sr.Recognizer()
score = 0

Elements = ["rock", "paper", "scissors"]

Video_condition = {
    ("rock", "rock"): "A:\\Games\\Rock-Paper-Scissors\\Using MP4 Videos\\Videos\\U-R C-R.mp4",  
    ("paper", "paper"): "A:\\Games\\Rock-Paper-Scissors\\Using MP4 Videos\\Videos\\U-P C-P.mp4",
    ("scissors", "scissors"): "A:\\Games\\Rock-Paper-Scissors\\Using MP4 Videos\\Videos\\U-S C-S.mp4",
    ("rock", "paper"): "A:\\Games\\Rock-Paper-Scissors\\Using MP4 Videos\\Videos\\U-R C-P.mp4",
    ("paper", "rock"): "A:\\Games\\Rock-Paper-Scissors\\Using MP4 Videos\\Videos\\U-P C-R.mp4",
    ("scissors", "rock"): "A:\\Games\\Rock-Paper-Scissors\\Using MP4 Videos\\Videos\\U-S C-R.mp4",
    ("rock", "scissors"): "A:\\Games\\Rock-Paper-Scissors\\Using MP4 Videos\\Videos\\U-R C-S.mp4",
    ("paper", "scissors"): "A:\\Games\\Rock-Paper-Scissors\\Using MP4 Videos\\Videos\\U-P C-S.mp4",
    ("scissors", "paper"): "A:\\Games\\Rock-Paper-Scissors\\Using MP4 Videos\\Videos\\U-S C-P.mp4"
}

lose_sound=["A:\\Games\\Rock-Paper-Scissors\audios\gabbar_threat_short.mp3","A:\\Games\\Rock-Paper-Scissors\\audios\\har_ni_ka_daar.mp3","A:\\Games\\Rock-Paper-Scissors\\audios\\086053_damn-youwav-82631.mp3","A:\\Games\\Rock-Paper-Scissors\audios\\Chennai Express- Dialogue Promo - 'Don't Underestimate The Power Of A Common Man'.mp3"]


print("\n============================")
print("      ROCK PAPER SCISSORS      ")
print("============================\n")
print("\n==========================================================================================================")
print("      RULES : agr ek baar haar jao ya jeet jao tab ek video aaygi use hatane ke liye 'q' press kar dena     ")
print("=============================================================================================================\n")


while True:
    wanna_Play = int(input("Enter 1 to play or 0 to exit: "))
    if wanna_Play == 0:
        print("Thanks for playing! See you again 🎮")
        print("Your Score : " + str(score))
        break

    if wanna_Play == 1:
        with sr.Microphone() as source:
            print("Say Your choice in \n")
            for i in range(3, 0, -1):  # using loop for countdown
                if i == 3:
                    print("Rock")
                    playsound("A:\\Games\\Rock-Paper-Scissors\\audios\\rock.mp3", block=False) 
                elif i == 2:
                    print("Paper")
                    playsound("A:\\Games\\Rock-Paper-Scissors\\audios\\paper.mp3", block=False)
                elif i == 1:
                    print("Scissors\n")
                    playsound("A:\\Games\\Rock-Paper-Scissors\\audios\\scissors.mp3", block=False)
                time.sleep(0.7)  # 0.7 sec ke baad agla countdown aayega 

            print("Let the war begin!⚔️🤺 ")
              

            audio = r.listen(source)

            try:    
                U_Choice = r.recognize_google(audio).lower()  # converting spoken input to lowercase text
                print(f"You chose {U_Choice}.\n") 

                if U_Choice not in Elements:
                    print("Bhai Rock Paper Scissors kehl rehe hum \n")
                    continue  # wapas se le lega input

                Comp_Choice = random.choice(Elements)  # saare elements se ek random choice itha lega 

                key = (U_Choice, Comp_Choice)  # dono ki choice ka ek variable bana ke store kara liya compare karane ke liye bo video play karne ke liye

                if key in Video_condition:
                    video_path = Video_condition[key]
                    playVid(video_path)  
                else:
                    print("Kuch to Gadbad Hai Dayaaaa🤔") 

                
                if ( (U_Choice == "rock" and Comp_Choice == "scissors") or
                     (U_Choice == "scissors" and Comp_Choice == "paper") or
                     (U_Choice == "paper" and Comp_Choice == "rock") ):
                    score =score+1
                    print("🔥 You WON this round! Current Score:", score)
                elif U_Choice == Comp_Choice:
                    print("⚔️ It's a DRAW!")
                else:
                    print("😢 You LOST this round!")

            except sr.UnknownValueError:
                print("Could not understand your voice ❌")
            except sr.RequestError:
                print("Could not request results from Google API 🚫")        
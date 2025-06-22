from play_vid import *   # here we are importing every function in play_vid file.
import random  # ye hume random funtion use karne deta hai jis se random value utha sakte hai 
import speech_recognition as sr  # library installed that takes user input from mic
import time  # sleep funtion use karne ke liye 

r = sr.Recognizer()
score = 0

Elements = ["rock", "paper", "scissors"]

Video_condition = {
    ("rock", "rock"): "A:\\Fun Projects\\Rock-Paper-Scissors\\Videos\\U-R C-R.avi",  
    ("paper", "paper"): "A:\\Fun Projects\\Rock-Paper-Scissors\\Videos\\U-P C-P.avi",
    ("scissors", "scissors"): "A:\\Fun Projects\\Rock-Paper-Scissors\\Videos\\U-S C-S.avi",
    ("rock", "paper"): "A:\\Fun Projects\\Rock-Paper-Scissors\\Videos\\U-R C-P.avi",
    ("paper", "rock"): "A:\\Fun Projects\\Rock-Paper-Scissors\\Videos\\U-P C-R.avi",
    ("scissors", "rock"): "A:\\Fun Projects\\Rock-Paper-Scissors\\Videos\\U-S C-R.avi",
    ("rock", "scissors"): "A:\\Fun Projects\\Rock-Paper-Scissors\\Videos\\U-R C-S.avi",
    ("paper", "scissors"): "A:\\Fun Projects\\Rock-Paper-Scissors\\Videos\\U-P C-S.avi",
    ("scissors", "paper"): "A:\\Fun Projects\\Rock-Paper-Scissors\\Videos\\U-S C-P.avi",
}

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
                elif i == 2:
                    print("Paper")
                elif i == 1:
                    print("Scissors\n")
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
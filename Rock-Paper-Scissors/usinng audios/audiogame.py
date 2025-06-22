import random
import speech_recognition as sr
import time
from playsound import playsound

r = sr.Recognizer()
score = 0

Elements = ["rock", "paper", "scissors"]

lose_sound = [
    r"A:\Games\Rock-Paper-Scissors\audios\gabbar_threat_short.mp3",
    # r"A:\Games\Rock-Paper-Scissors\audios\har_ni_ka_daar.mp3",
    r"A:\Games\Rock-Paper-Scissors\audios\086053_damn-youwav-82631.mp3",
    r"A:\Games\Rock-Paper-Scissors\audios\Chennai Express- Dialogue Promo - 'Don't Underestimate The Power Of A Common Man'.mp3"
]

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
            for i in range(3, 0, -1):
                if i == 3:
                    print("Rock")
                    playsound(r"A:\Games\Rock-Paper-Scissors\audios\rock.mp3")
                elif i == 2:
                    print("Paper")
                    playsound(r"A:\Games\Rock-Paper-Scissors\audios\paper.mp3")
                elif i == 1:
                    print("Scissors\n")
                    playsound(r"A:\Games\Rock-Paper-Scissors\audios\scissors.mp3")
                time.sleep(0.6)

            print("Let the war begin!⚔️🤺 ")
            audio = r.listen(source)

            try:
                U_Choice = r.recognize_google(audio).lower()
                print(f"You chose {U_Choice}.\n")

                if U_Choice not in Elements:
                    print("Bhai Rock Paper Scissors kehl rehe hum \n")
                    continue

                Comp_Choice = random.choice(Elements)
                print(f"Computer chose {Comp_Choice}.\n")

                if ((U_Choice == "rock" and Comp_Choice == "scissors") or
                    (U_Choice == "scissors" and Comp_Choice == "paper") or
                    (U_Choice == "paper" and Comp_Choice == "rock")):
                    score += 1
                    print("🔥 You WON this round! Current Score:", score)
                elif U_Choice == Comp_Choice:
                    print("⚔️ It's a DRAW!")
                else:
                    print("😢 You LOST this round!")
                    playsound(random.choice(lose_sound))

            except sr.UnknownValueError:
                print("Could not understand your voice ❌")
            except sr.RequestError:
                print("Could not request results from Google API 🚫")

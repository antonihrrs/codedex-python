import random

symbols = ["🍒", "🍇", "🍉", "7️⃣"]

def play():
  while True :
    symbol_output = random.choices(symbols, k=3)

    def line_thingy():
      lines = [letter for letter in (results)]
      print(" | ".join(lines))
  
    results = symbol_output
    line_thingy()
  

    if all(item == "7️⃣" for item in results) :
      print ("Jackpot ! 💰")
    
    elif all(item == "🍒" for item in results):
      print("𝓒𝓱𝓮𝓻𝓻𝓲𝓮𝓼\n")

    else :
      print ("Thanks for playing !")
      while True :
        user_ask = input("Do you want to keep playing ? Yes or No\n").lower()
        if user_ask == "yes":
          break
        elif user_ask == "no":
          print("Okay bye")
          quit()

play()

https://replit.com/join/slrvbqwpgy-samanthadesaida

"""
STEPS FOR MY CODE:
1- limit attempts to 3
2- secret word = pozole
3- write the blanks for the secret word 
make the user guess one at a time
"""
number_attempts = 0
while number_attempts < 3:
  number_attempts+=1
  print("This is your attempt",number_attempts)
  print("Remember you have 3 attempts only")
  print("_ _ _ _ _ _")
  first = input("Write your first guess: ")
  if first == "p":
    print("P _ _ _ _ _")
    second = input("Write your second guess: ")
    if second == "o":
      print("P O _ O _ _")
      third = input("Write your third guess:  ")
      if third == "z":
        print("P O Z O _ _")
      fourth = input("Write your fourth guess:  ")
      if fourth == "l":
        print("P O Z O L _")
        fifth = input("Write your fifth guess:  ")
        if fifth == "e":
          print("yay! you guessed the word")
          print("P O Z O L E")
    else:
      print("That's incorrect")
  else:
    print("That's incorrect")
number_attempts = 100

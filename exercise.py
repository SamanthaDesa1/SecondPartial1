emotion = input("How are you? Options: sad, angry, happy  ")

if emotion == "sad":
  question = input("Why are you sad? ")
  if question == "idk":
    print("just don't :)")
elif emotion == "angry":
  question = input("Why are you angry?")
elif emotion == "happy":
  question = input("Why are you happy?")
else:
  print("please enter a valid answer")

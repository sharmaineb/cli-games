# flashcards.py
# imported the json module from python3
import json


# opened the file and parse from python3
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

    
    total = len(data["cards"])

score = 0


for i in data["cards"]:
    guess = input(i["q"] + " > ")
    
    if (guess.lower() == i["a"].lower()):
        score +=  1
        print(f"Correct! Current Score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current Score: {score}/{total}")

    play_again = input(f"Ready for the next card? (yes/no): ")
    if play_again == "yes":
        player = False
    else:
      break

    





    



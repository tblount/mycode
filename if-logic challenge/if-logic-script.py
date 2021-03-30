#!/usr/bin/env python3

print("Welcome to the Hidden Leaf Village")
print("Lets get you assigned to a team!!!")
print("")

teams=  {
"Team 7":
    {"Sensei": "Kakashi",
    "members": "Naruto, Sakura, Sasuke, and now You!!"},
"Team Guy":
    {"Sensei": "Might Guy",
    "members": "You of course!, Rock Lee, Ten Ten, and Neji!"},
"Team 10":
    {"Sensei": "Asuma",
    "members": "Your team leader Shikamaru, Ino, and Choji. Also the newest member you!! "}
        }

your_squad = print(teams["Team 7"]["members"])

pick = input("Choose a number 1-3.")

if pick == "1":
    print("Looks like you will be on Team 7, with Big brother Naruto!")
elif pick == "2":
    print("Nice you will be assigned to Shikamaru's team!!!")
else:
    print("Hmm, you should get along with the Hyuga kid just fine! Guy will be your sensei!!")

next = input("What you like to know who else is on your team?")
# print(your_squad)
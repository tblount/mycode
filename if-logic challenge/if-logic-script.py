#!/usr/bin/env python3

print("Welcome to the Hidden Leaf Village")
name = input("Hey! What is your name?")
print("Ok," + name + " lets get you assigned to a team!!!")
print("")

teams=  {
"Team 7":
    {"Sensei": "Kakashi",
    "members": "Naruto, Sakura, Sasuke, and now " + name + "!!"},
"Team Guy":
    {"Sensei": "Might Guy",
    "members": name + " of course!, Rock Lee, TenTen, and Neji!"},
"Team 10":
    {"Sensei": "Asuma",
    "members": "Your team leader Shikamaru, Ino, and Choji. Also the newest member" + name + "!!"}
        }

pick = input("Choose a number 1-3.")

if pick == "1":
    print("Looks like you will be on Team 7, with Big brother Naruto!")
    print("Team 7 members are now...")
    your_squad = print(teams["Team 7"]["members"])
elif pick == "2":
    print("Nice you will be assigned to Shikamaru's team!!!")
    print("Team 10 members are now...")
    your_squad = print(teams["Team 10"]["members"])
else:
    print("Hmm, you should get along with the Hyuga kid just fine! Guy will be your sensei!!")
    print("Team Guy members are now...")
    your_squad = print(teams["Team Guy"]["members"])

# next = input("What you like to know who else is on your team?")

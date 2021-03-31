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
    "members": "Your team leader Shikamaru, Ino, and Choji. Also the newest member " + name + "!!"}
        }

pick = input("Choose a number 1-3.")

if pick == "1":
    print("Looks like you will be on Team 7, with Big brother Naruto!")
    print("Team 7 members are now...")
    your_squad = print(teams["Team 7"]["members"])
    print('')
    print('About Team 7: ')
    team_7 = print(
        "Team 7 was a Konohagakure team formed under the leadership of Kakashi Hatake. Two-and-a-half years after Sasuke Uchiha left the village, Kakashi filled out paperwork to form Team Kakashi, \n"
        "with his former pupils Naruto Uzumaki and Sakura Haruno now being treated as equals alongside their teacher.\n Following Yamato and Sai joining the team, the group went by Team Yamato during the former's leadership.")
elif pick == "2":
    print("Nice you will be assigned to Shikamaru's team!!!")
    print("Team 10 members are now...")
    your_squad = print(teams["Team 10"]["members"])
    print('')
    print('Here is a little team knowledge.')
    team_10 = print(
        "Team Asuma, also known as Team 10, is a generation in the Ino–Shika–Chō Trio (いの しか ちょうトリオ, Ino–Shika–Chō Torio).\n As such, the three team members are good friends and have exceptional team work, although they tend to bicker from time to time. All three members of Team 10 are skilled at stalling opponents. "
        "\nThey were led by Asuma until his death in Part II. Kakashi led them temporarily after that to help them avenge Asuma's death.\n The team is assumed to still be active, although without a permanent leader.")
else:
    print("Hmm, you should get along with the Hyuga kid just fine! Guy will be your sensei!!")
    print("Team Guy members are now...")
    your_squad = print(teams["Team Guy"]["members"])
    print('')
    print('Here is a bit about your team')
    team_guy = print(
        'Team Guy was a team led by Might Guy and was formed a year before the other main Konoha teams of the series.\n They specialise in close-quarters combat with all of its members using some sort of physical attacks. '
        'Guy waited a year before entering them in the Chūnin Exams, though none of his apprentices were promoted at that time.\n Later, between the events of Parts I and II, Rock Lee and Tenten became chūnin while Neji Hyūga surpassed his teammates and rose to the ranks of jōnin. Despite becoming more busy, Neji still goes on missions with his team. \nAlong with the other members of the Konoha 11, Team Guy regrettably had decided to kill Sasuke Uchiha personally in order to prevent war between Konoha and Kumogakure or/and any of the other major nations, but were persuaded by Naruto Uzumaki that he would deal with Sasuke alone. '
        '\nDuring the events of the Fourth Shinobi World War, Neji was among those killed in the line of duty, and later Guy suffered a permanent injury which forced him to retire after the end of the war, leaving only Lee and Tenten remaining in active duty.')


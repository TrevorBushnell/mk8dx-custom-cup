import random
import sys

def choose_track(tracks, reroll=1):    
    if reroll == 1: #first time rolling!
        # create a dictionary of weights
        probs = [0.11, 0.225, 0.235, 0.15, 0.125, 0.1, 0.055]
        chosen_tier = random.choices(list(tracks.keys()), probs, k=1)[0]
    if reroll == 2: #second time rolling!
        tiers = ["a", "b", "c", "d", "f"]
        probs = [0.25, 0.3, 0.2, 0.15, 0.1]
        chosen_tier = random.choices(tiers, probs, k=1)[0]
    if reroll == 3: #third time rerolling!
        tiers = ["b", "c", "d", "f"]
        probs = [0.2, 0.3, 0.25, 0.25]
        chosen_tier = random.choices(tiers, probs, k=1)[0]
    if reroll == 4: #fourth time rerolling!
        tiers = ["c", "d", "f"]
        probs = [0.33, 0.33, 0.34]
        chosen_tier = random.choices(tiers, probs, k=1)[0]

    return chosen_tier, random.choice(tracks[chosen_tier])


tracks = {
    "ss" : ['Wii Rainbow Road'],
    "s" : ['GCN Yoshi Circuit', 'Wii DK Summit', 'Wii Mushroom Gorge', 'Wii Coconut Mall', '3DS Rainbow Road', 'Wii Maple Treeway'],
    "a" : ['Wii Koopa Cape', '3DS Rock Rock Mountain', '3DS Music Park', 'Mount Mario', 'Sunshine Airport', 'Big Blue', 'DS Tick Tock Clock', 'N64 Yoshi Valley', 'GCN Waluigi Stadium', 'GCN DK Mountain', 'Mario Circuit', 'N64 Rainbow Road', 'SNES Rainbow Road', 'N64 Choco Mountain', 'GBA Snow Land', 'DS Mario Circuit'],
    "b" : ['SNES Bowser Castle 3', 'Piranha Plan Cove', 'SNES Mario Circuit 3', 'Wii Wario\'s Gold Mine', 'GCN Daisy Cruiser', '3DS DK Jungle', 'Wii Moo Moo Meadows', 'Merry Mountain', 'DS Waluigi Pinball', 'Wii Moonview Highway', 'Toad Harbor', '3DS Piranha Plant Slide', 'GBA Mario Circuit', 'N64 Royal Raceway', 'Electrodome', 'Bowser Castle', 'Dragon Driftway', 'Shy Guy Falls', 'Ninja Hideaway', 'GCN Dry Dry Desert', 'Hyrule Circuit', 'Tour LA Laps', 'Tour New York Minute', 'GBA Boo Lake', 'Tour Singapore Speedway', 'Yoshi\'s Island', 'Squeaky Clean Sprint'],
    "c" : ['Wii Daisy Circuit', 'N64 Kalimari Desert', 'DS Shroom Ridge', 'GBA Ribbon Road', 'Super Bell Subway', 'Animal Crossing', 'Sky High Sundae', 'Mute City', 'Wild Woods', 'DS Cheep Cheep Beach', 'Tour Vancouver Velocity', 'Tour London Loop', 'Tour Paradise Promenade', 'Tour Berlin Byways', 'Tour Sydney Sprint', 'Tour Madrid Drive', 'Tour Tokyo Blur', 'Water Park', 'GBA Cheese Land', '3DS Neo Bowser City', 'GBA Riverside Park', 'Tour Rome Avanti', 'Tour Amsterdam Drift'],
    "d" : ['GBA Sunset Wilds', 'Twisted Mansion', 'Excitebike Arena', 'DS Wario Stadium', 'Tour Athens Dash', 'DS Peach Gardens', '3DS Toad Circuit', 'GBA Sky Garden', 'Rainbow Road', 'N64 Toad\'s Turnpike', 'Cloudtop Cruise', 'Thwomp Ruins', 'SNES Donut Plains 3', 'Sweet Sweet Canyon', 'Mario Kart Stadium', 'Ice Ice Outpost', 'GCN Sherbet Land', 'Tour Bankok Rush'],
    "f" : ['GCN Baby Park', 'Wii Grumble Volcano', '3DS Rosalina\'s Ice World', 'Bone Dry Dunes', 'Dolphin Shoals']
    }
custom_cup = []

for i in range(4):
    tier, track = choose_track(tracks)
    custom_cup.append(track)
    tracks[tier].remove(track)

print("CUSTOM CUP (Pull #1):")
for i in range(1,5):
    print(f"{i}: {custom_cup[i-1]}")

print()
flag = int(input("Enter the # for the track to re-roll. Enter 0 if happy."))

if flag == 0:
    print("Good luck and enjoy your custom GP!")
    sys.exit()
else:
    tier, track = choose_track(tracks, reroll=2)
    custom_cup[flag-1] = track
    tracks[tier].remove(track)

print("\n")
print("CUSTOM CUP (Pull #2):")
for i in range(1,5):
    print(f"{i}: {custom_cup[i-1]}")

print()
flag = int(input("Enter the # for the track to re-roll. Enter 0 if happy."))

if flag == 0:
    print("Good luck and enjoy your custom GP!")
    sys.exit()
else:
    tier, track = choose_track(tracks, reroll=3)
    custom_cup[flag-1] = track
    tracks[tier].remove(track)
    
print("\n")
print("CUSTOM CUP (Pull #3):")
for i in range(1,5):
    print(f"{i}: {custom_cup[i-1]}")

print()
flag = int(input("Enter the # for the track to re-roll. Enter 0 if happy."))

if flag == 0:
    print("Good luck and enjoy your custom GP!")
    sys.exit()
else:
    tier, track = choose_track(tracks, reroll=3)
    custom_cup[flag-1] = track
    tracks[tier].remove(track)
    
print("\n")
print("CUSTOM CUP (Pull #4):")
for i in range(1,5):
    print(f"{i}: {custom_cup[i-1]}")

print("\nSuck and deal, good luck :O")

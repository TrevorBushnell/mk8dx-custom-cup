import random
import streamlit as st
from PIL import Image

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

if 'initial_roll' not in st.session_state:
    st.session_state.initial_roll = True

if 'counter' not in st.session_state:
    st.session_state.counter = 1

if 'tracks' not in st.session_state:
    st.session_state.tracks = {
    "ss" : ['Wii Rainbow Road'],
    "s" : ['GCN Yoshi Circuit', 'Wii DK Summit', 'Wii Mushroom Gorge', 'Wii Coconut Mall', '3DS Rainbow Road', 'Wii Maple Treeway'],
    "a" : ['Wii Koopa Cape', '3DS Rock Rock Mountain', '3DS Music Park', 'Mount Wario', 'Sunshine Airport', 'Big Blue', 'DS Tick Tock Clock', 'N64 Yoshi Valley', 'GCN Waluigi Stadium', 'GCN DK Mountain', 'Mario Circuit', 'N64 Rainbow Road', 'SNES Rainbow Road', 'N64 Choco Mountain', 'GBA Snow Land', 'DS Mario Circuit'],
    "b" : ['SNES Bowser Castle 3', 'Piranha Plan Cove', 'SNES Mario Circuit 3', 'Wii Wario\'s Gold Mine', 'GCN Daisy Cruiser', '3DS DK Jungle', 'Wii Moo Moo Meadows', 'Merry Mountain', 'DS Waluigi Pinball', 'Wii Moonview Highway', 'Toad Harbor', '3DS Piranha Plant Slide', 'GBA Mario Circuit', 'N64 Royal Raceway', 'Electrodome', 'Bowser Castle', 'Dragon Driftway', 'Shy Guy Falls', 'Ninja Hideaway', 'GCN Dry Dry Desert', 'Hyrule Circuit', 'Tour LA Laps', 'Tour New York Minute', 'GBA Boo Lake', 'Tour Singapore Speedway', 'Yoshi\'s Island', 'Squeaky Clean Sprint'],
    "c" : ['Wii Daisy Circuit', 'N64 Kalimari Desert', 'DS Shroom Ridge', 'GBA Ribbon Road', 'Super Bell Subway', 'Animal Crossing', 'Sky High Sundae', 'Mute City', 'Wild Woods', 'DS Cheep Cheep Beach', 'Tour Vancouver Velocity', 'Tour London Loop', 'Tour Paradise Promenade', 'Tour Berlin Byways', 'Tour Sydney Sprint', 'Tour Madrid Drive', 'Tour Tokyo Blur', 'Water Park', 'GBA Cheese Land', '3DS Neo Bowser City', 'GBA Riverside Park', 'Tour Rome Avanti', 'Tour Amsterdam Drift'],
    "d" : ['GBA Sunset Wilds', 'Twisted Mansion', 'Excitebike Arena', 'DS Wario Stadium', 'Tour Athens Dash', 'DS Peach Gardens', '3DS Toad Circuit', 'GBA Sky Garden', 'Rainbow Road', 'N64 Toad\'s Turnpike', 'Cloudtop Cruise', 'Thwomp Ruins', 'SNES Donut Plains 3', 'Sweet Sweet Canyon', 'Mario Kart Stadium', 'Ice Ice Outpost', 'GCN Sherbet Land', 'Tour Bankok Rush'],
    "f" : ['GCN Baby Park', 'Wii Grumble Volcano', '3DS Rosalina\'s Ice World', 'Bone Dry Dunes', 'Dolphin Shoals']
    }

if 'track_1' not in st.session_state:
    st.session_state.track_1 = ""

if 'track_2' not in st.session_state:
    st.session_state.track_2 = ""

if 'track_3' not in st.session_state:
    st.session_state.track_3 = ""

if 'track_4' not in st.session_state:
    st.session_state.track_4 = ""

if st.session_state.initial_roll:
    tier, track = choose_track(st.session_state.tracks)
    st.session_state.track_1 = track
    st.session_state.tracks[tier].remove(track)

    tier, track = choose_track(st.session_state.tracks)
    st.session_state.track_2 = track
    st.session_state.tracks[tier].remove(track)

    tier, track = choose_track(st.session_state.tracks)
    st.session_state.track_3 = track
    st.session_state.tracks[tier].remove(track)

    tier, track = choose_track(st.session_state.tracks)
    st.session_state.track_4 = track
    st.session_state.tracks[tier].remove(track)

    st.session_state.initial_roll = False



st.write("# Mario Kart 8 DX Custom Grand Prix Generator")

st.write("""
Welcome! This website will let you generate a custom grand prix based on a tier list created by me! This mainly exists online because my roommate said I should make an app but I am too lazy to do that so I am putting it on this simple website. Upon loading the site, you will see 4 tracks that can be used in a Grand Prix. If you don't like one of the tracks listed, you can reroll a track, HOWEVER this means that you will lose out on the ability to pull a track from the highest tier. There's also a randomized kart generator should you wish to use something like this as well in your custom grand prixs. You can see the tierlist at the bottom of this website. Enjoy!
         
**HOW TO USE: Click the name of a track to reroll that given track for a different one! Note that you will not be able to pull higher tier tracks the more you re-roll...**
         
*For some reason there is a bug and you need to double click a track in order for the update to actually happen. Apologies!*
         """)
print(st.session_state.counter)

st.write(f"#### CUSTOM CUP (Pull #{st.session_state.counter}):")

if st.button(f"\#1: {st.session_state.track_1}"):
    print("got here!")
    st.session_state.counter += 1
    print("got here 2!")
    print(st.session_state.counter)
    if st.session_state.counter <= 4:
        tier, track = choose_track(st.session_state.tracks, reroll=st.session_state.counter)
        st.session_state.track_1 = track
        st.session_state.tracks[tier].remove(track)

if st.button(f"\#2: {st.session_state.track_2}"):
    print("got here!")
    st.session_state.counter += 1
    print("got here 2!")
    print(st.session_state.counter)
    if st.session_state.counter <= 4:
        tier, track = choose_track(st.session_state.tracks, reroll=st.session_state.counter)
        st.session_state.track_2 = track
        st.session_state.tracks[tier].remove(track)

if st.button(f"\#3: {st.session_state.track_3}"):
    print("got here!")
    st.session_state.counter += 1
    print("got here 2!")
    print(st.session_state.counter)
    if st.session_state.counter <= 4:
        tier, track = choose_track(st.session_state.tracks, reroll=st.session_state.counter)
        st.session_state.track_3 = track
        st.session_state.tracks[tier].remove(track)

if st.button(f"\#4: {st.session_state.track_4}"):
    print("got here!")
    st.session_state.counter += 1
    print("got here 2!")
    print(st.session_state.counter)
    if st.session_state.counter <= 4:
        tier, track = choose_track(st.session_state.tracks, reroll=st.session_state.counter)
        st.session_state.track_4 = track
        st.session_state.tracks[tier].remove(track)

st.write("#### RANDOM KART COMBO GENERATOR")

drivers = ['Mario', 'Luigi', 'Peach', 'Daisy', 'Yoshi', 'Toad', 'Toadette', 'Koopa Troopa', 'Bowser', 'Donkey Kong', 'Wario', 'Waluigi', 'Rosalina', 'Metal Mario', 'Pink Gold Peach', 'Lakitu', 'Shy Guy', 'Baby Mario', 'Baby Luigi', 'Baby Peach', 'Baby Daisy', 'Baby Rosalina', 'Larry', 'Lemmy', 'Wendy', 'Ludwig', 'Iggy', 'Roy', 'Morton', 'Mii', 'Tanooki Mario', 'Link', 'Villager', 'Isabelle', 'Cat Peach', 'Dry Bowser', 'Gold Mario', 'Dry Bones', 'Bowser Jr.', 'King Boo', 'Inkling', 'Birdo', 'Wiggler', 'Petey Piranha', 'Kamek', 'Diddy Kong', 'Funky Kong', 'Peachette', 'Pauline']
karts = ['Standard Kart', 'Pipe Frame', 'Mach 8', 'Steel Driver', 'Cat Cruiser', 'Circuit Special', 'Tri-Speeder', 'Badwagon', 'Prancer', 'Biddybuggy', 'Landship', 'Sneeker', 'Sports Coupe', 'Gold Standard', 'Standard Bike', 'Comet', 'Sport Bike', 'The Duke', 'Flame Rider', 'Varmint', 'Mr. Scooty', 'Jet Bike', 'Yoshi Bike', 'Standard ATV', 'Wild Wiggler', 'Teddy Buggy', 'GLA', 'W 25 Silver Arrow', '300 SL Roadster', 'Blue Falcon', 'Tanooki Kart', 'B Dasher', 'Master Cycle', 'Streetle', 'P-Wing', 'City Tripper', 'Bone Rattler', 'Koopa Clown', 'Splat Buggy', 'Inkstriker']
tires = ['Standard', 'Monster', 'Roller', 'Slim', 'Slick', 'Metal', 'Button', 'Off-Road', 'Sponge', 'Wood', 'Cushion', 'Blue Standard', 'Hot Monster', 'Azure Roller', 'Crimson Slim', 'Cyber Slick', 'Retro Off-Road', 'Gold Tires', 'GLA Tires', 'Triforce Tires', 'Leaf Tires']
gliders = ['Super Glider', 'Cloud Glider', 'Wario Wing ', 'Waddle Wing', 'Peach Parasol', 'Parachute', 'Parafoil', 'Flower Glider  ', 'Bowser Kite', 'Plane Glider  ', 'MKTV Parafoil', 'Gold Glider', 'Hylian Kite', 'Paper Glider']

rand_driver = random.choice(drivers)
rand_kart = random.choice(karts)
rand_tire = random.choice(tires)
rand_glider = random.choice(gliders)

st.write(f"Driver: {rand_driver}")
st.write(f"Kart: {rand_kart}")
st.write(f"Tires: {rand_tire}")
st.write(f"Glider: {rand_glider}")

if st.button('GERNEATE NEW COMBO!'):
    pass

tier_list = Image.open("mk8dx_track_tierlist.png")
st.image(tier_list, use_column_width=True)
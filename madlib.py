print("Welcome to Madlibs!")

pluralnoun = raw_input("Enter a plural noun of your choice:")
noun_1 = raw_input("Enter a noun of your choice:")
noun_2 = raw_input("Enter a second noun of your choice:")
song = raw_input("Enter the title of a song of your choice:")
noun_3 = raw_input("Enter another noun of your choice:")
#madlibs = ("""Learning to drive is a tricky process. There are a few rules to follow.
#1. Keep two""", (pluralnoun), """on the steering wheel at all times.
#2. Step on the""", (noun_1), "to speed up and the", (noun_2), """to slow down.
#3. Your parents will just LOVE it if you play""", (song), """on the radio. 
#4. Make sure to honk your horn when you see""", (noun_3), """on a street sign.""")
madlibs = ("""Learning to drive is a tricky process. There are a few rules to follow.
1. Keep two %s on the steering wheel at all times.
2. Step on the %s to speed up and the %s to slow down.
3. Your parents will just LOVE it if you play %s on the radio. 
4. Make sure to honk your horn when you see %s on a street sign.""")
print(madlibs %(pluralnoun,noun_1,noun_2,song,noun_3))
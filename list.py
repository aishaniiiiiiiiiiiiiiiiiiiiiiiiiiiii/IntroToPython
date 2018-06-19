mylist = ["cream cheeeeeeessssseeeeee", "brownies", "cherries", "a bunch of pillows", "cocnut water"]       
#this is just the list, so if you asked the program to print it it would show the brackets, quotes, commas, etc. We just want the items, hence the "for" command in the next line.
for item in mylist:
    print(item)
    
additem = raw_input("Would you like to add anything else to your list?")
#only use double equal signs in if statements - single equal signs won't work
if additem == "yes":
    newitem = raw_input("What would you like to add?")
    if newitem == "nothing": #you know, just in case if the person changed their mind or whatever
        print ("ok byeeeeeeee") #friendly customer service always helps
    else:
        mylist.append(newitem)  # ".append" will add whatever you input
        print("New list:")
        for new_items in mylist:
            print new_items
if additem == "yeah":
    newitem = raw_input("What would you like to add?")
    if newitem == "nothing": 
        print ("ok byeeeeeeee")
    else:
        mylist.append(newitem)  #gotta indent those lines
        print("New list:")
        for new_items in mylist:
            print new_items
if additem == "sure":
    newitem = raw_input("What would you like to add?")
    if newitem == "nothing": 
        print ("ok byeeeeeeee") 
    else:
        mylist.append(newitem)
        print("New list:")
        for new_items in mylist:
            print new_items
if additem == "why not":    #good question buddy
    newitem = raw_input("What would you like to add?")
    if newitem == "nothing": 
        print ("ok byeeeeeeee") 
    else:
        mylist.append(newitem)
        print("New list:")
        for new_items in mylist:
            print new_items
if additem == "YEEEET":
    newitem = raw_input("What would you like to add?")
    if newitem == "nothing": 
        print ("ok byeeeeeeee") 
    else:
        mylist.append(newitem)
        print("New list:")
        for new_items in mylist:
            print new_items
if additem == "YEEEEET":
    newitem = raw_input("What would you like to add?")
    if newitem == "nothing": 
        print ("ok byeeeeeeee") 
    else:
        mylist.append(newitem)
        print("New list:")
        for new_items in mylist:
            print new_items
if additem == "no":
    print("ok byeeeeeeee")
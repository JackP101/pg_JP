name = "Jack Putrino"

subjects = ["English","Math","Spanish","History","Science","Comp Sci"]

print ("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)

dogs = ["Black Labs","Bassethounds", "Dalmations", "Tibetan Mastiffs","Bulldogs"]

for i in dogs:
    if i == "Black Labs":
        print (i + " are the best at swimming.")
    if i == "Bassethounds":
        print(i + " are the sleepiest.")
    if i == "Dalmmations":
        print (i + " are the dumbest.")
    if i == "Tibetan Mastiffs":
        print (i + " are the fluffiest.")
    if i == "Bulldogs":
        print (i + " are the toughest.")

dogss = []

while True:
    print("What movie do you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        dogs.append(answer)

for i in dogs:
    print("One of your favorites is " + i)

import random

money = int(100)

def saved():
    qw = " ____  ____   ___   _____  _____   ____      ____  _____  ____  _____  "
    we = "|_  _||_  _|.'   `.|_   _||_   _| |_  _|    |_  _||_   _||_   \|_   _| "
    er = "  \ \  / / /  .-.  \ | |    | |     \ \  /\  / /    | |    |   \ | |   "
    rt = "   \ \/ /  | |   | | | '    ' |      \ \/  \/ /     | |    | |\ \| |   "
    ty = "   _|  |_  \  `-'  /  \ \__/ /        \  /\  /     _| |_  _| |_\   |_  "
    yu = "  |______|  `.___.'    `.__.'          \/  \/     |_____||_____|\____| "
    print(qw)
    print(we)
    print(er)
    print(rt)
    print(ty)
    print(yu)

def dead():
    g = " /$$     /$$ /$$$$$$  /$$   /$$       /$$$$$$$  /$$$$$$ /$$$$$$$$ /$$$$$$$ "
    h = "|  $$   /$$//$$__  $$| $$  | $$      | $$__  $$|_  $$_/| $$_____/| $$__  $$"
    i = " \  $$ /$$/| $$  \ $$| $$  | $$      | $$  \ $$  | $$  | $$      | $$  \ $$"
    j = "  \  $$$$/ | $$  | $$| $$  | $$      | $$  | $$  | $$  | $$$$$   | $$  | $$"
    k = "   \  $$/  | $$  | $$| $$  | $$      | $$  | $$  | $$  | $$__/   | $$  | $$"
    l = "    | $$   | $$  | $$| $$  | $$      | $$  | $$  | $$  | $$      | $$  | $$"
    m = "    | $$   |  $$$$$$/|  $$$$$$/      | $$$$$$$/ /$$$$$$| $$$$$$$$| $$$$$$$/"
    n = "    |__/    \______/  \______/       |_______/ |______/|________/|_______/ "

    print(g)
    print(h)
    print(i)
    print(j)
    print(k)
    print(l)
    print(m)
    print(n)


def gamble():
    global money
    print("He promises you that you will get two times the money you bet if you win. You currently have " + str(money) + " vbucks.")
    gamble_amount = int(raw_input("How much do you want to bet? "))

    # make sure to add a sequence thing if they put more that 100 money#
    win_lose = random.choice([0,1])
            
    if win_lose == 1:
        money += 2*gamble_amount
        print("You won! You now have " + str(money) + " vbucks")
                
    if win_lose == 0:
        money -= gamble_amount
        print("You lost! You now have " + str(money) + " vbucks")
        
def NO():
    print("You head to the bridge to see if the captain is there... Nobody's there...")
    signal_choice = raw_input("Do you signal other ships using the radio? ")
    if signal_choice == "YES":
        print("You finally manage to signal a ship and are saved in a matter of hours!")
        saved()
    elif signal_choice == "NO":
        print("You go back to the man selling rafts.")
        beg_answer = raw_input("Do you beg him for a spot? ")
        if beg_answer == "YES":
            print("The raft man pushes you into the icy water and you freeze to death. You are turned to an icecube. RIP ")  
            dead()
        elif beg_answer == "NO":
            NO()   

            
a = "   _____ _       __   _                _____ __    _     "
b = "  / ___/(_)___  / /__(_)___  ____ _   / ___// /_  (_)___ "
c = "  \__ \/ / __ \/ // /_/ __ \/ __ `/   \__ \/ __ \/ / __ \ "
d = " ___/ / / / / / ,< / / / / / /_/ /   ___/ / / / / / /_/ /"
e = "/____/_/_/ /_/_/|_/_/_/ /_/\__, /   /____/_/ /_/_/ .___/ "
f = "                          /____/                /_/      "
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print("Make sure to be in caps lock")
print("You wake up in your cabin. You look to your desk and see 100 vbucks")

explore_answer = str(raw_input("Do you want to explore the deck? YES or NO "))

if explore_answer == "YES":
    gamble_answer = str(raw_input("You see a hustler on the deck. Do you want to bet any money? YES or NO "))
    if gamble_answer == "YES":
        gamble()
print(money)

room_answer = str(raw_input("Do you want to go back to your room? YES or NO "))

if explore_answer == "NO" or room_answer == "YES":
    print("You decide to stay there and rest.")
    print("All of a sudden, you are awoken by a violent jolt. The whole ship is shaking and you fall off your bed.")
    print("You look up and realize that your door is blocked by your cabinet.")
    door_answer = raw_input("What do you do? A. Call room service B. Try to move the cabinet C. Jump out your window onto the deck ")
    if door_answer == "A":
        print("Nobody comes and you die. RIP.You won't even be in the movie adaptation.")
        dead()
    if door_answer == "B":
        lift_fall = random.choice([0, 1])
        if lift_fall == 0:
            print("You remember to lift with your knees and manage to move it. You are now in the hallway and rush to escape.")
            print("Unfortunately for you, you run too quickly and crack your head on the stairs. Nobody helps you and you die. RIP")
            dead()
        if lift_fall == 1:
            print("It falls on you and you die. RIP")
            dead()
    if door_answer == "C":
        print("You see a man selling spots on a raft.")
        approach_answer = raw_input("Do you approach him? ")
        global approach_answer
        if approach_answer == "YES":
            print("He charges you 200 vbucksfor  a spot")
            pay_answer = raw_input("Do you pay him the money? ")
            if pay_answer == "YES" and money >= 200:
                print("He offers you a spot on the raft and you are saved the next day!")
                saved()
        if approach_answer == "NO" or pay_answer == "NO" or money < 200:
            NO()
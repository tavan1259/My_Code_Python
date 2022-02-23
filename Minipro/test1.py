import random
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card = []
com_card = []
Black_jack = ""
get_card = ""
def deal_card():
    while len(user_card) <2:
        user_card.append(random.choice(card))
        com_card.append(random.choice(card))

def Show_card():
    print("")
    print("You card = ",user_card,"You score = %d "%(sum(user_card)))
    print("coumputer First card = ",com_card[0])



def chack_score():
    print("You Final hand = ",user_card,"Final score = %d "%(sum(user_card)))
    print("computer Final hand = ",com_card,"computer Final score = %d"%(sum(com_card)))

def A_TO_11(a,b) :
    while sum(b) > 21 and b.count(11) > 1:
        b.insert(b[-1],1)
        b.pop(b.index(11))
    while sum(a) > 21 and a.count(11) > 1:
        a.insert(a[-1],1)
        a.pop(a.index(11))


def chack_BJ():
    if sum(com_card) == 21:
        print("You hand = ",user_card,"You score = %d "%(sum(user_card)))
        print("computer hand = ",com_card,"computer  score = %d"%(sum(com_card)))
        print("Computer Black Jack YOU LOST!!! ")  
        return 1
    elif sum(user_card)== 21:
        print("You hand = ",user_card,"You score = %d "%(sum(user_card)))
        print("computer hand = ",com_card,"computer  score = %d"%(sum(com_card)))
        print("Black Jack YOU WIN!!! ")
        return 2

def lost_score(x):
    if sum(x) == 21 :
        return 1 
    elif sum(x) > 21 :
        return 2
####################################################################
while Black_jack != 'n':
    Black_jack = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
    if Black_jack.lower() != 'y' and Black_jack.lower()!='n':
        print("Error You type please tye again")

    elif Black_jack.lower() == 'y':

        deal_card()
        A_TO_11(com_card,user_card)
        if chack_BJ() == 1 or chack_BJ() == 2:
            break
        Show_card()

        while get_card != 'n':
            get_card = input("Type 'y' to get another card, Type 'n' to pass : ")
            if get_card.lower() != 'y' and get_card.lower() != 'n':
                print("Error You type please tye again")
            elif get_card.lower() == 'y':
                print("1")
        #chack_score()
    get_card = ""
    user_card.clear()
    com_card.clear()

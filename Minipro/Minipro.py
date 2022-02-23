import random
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card = []
com_card = []
game = ""
get = ""
move = ""
Endgame = ""
Show = 0
def deal_card():
    while len(user_card) <2:
        user_card.append(random.choice(card))
        com_card.append(random.choice(card))

def chack_BJ():
    black =[10,11]
    jack = [11,10]
    if com_card == black or com_card == jack :
        print("You hand = ",user_card,"You score = %d "%(sum(user_card)))
        print("computer hand = ",com_card,"computer  score = %d"%(sum(com_card)))
        print("Computer Black Jack YOU LOST!!! ")  
        return 1
    
    elif user_card == black or user_card == jack:
        print("You hand = ",user_card,"You score = %d "%(sum(user_card)))
        print("computer hand = ",com_card,"computer  score = %d"%(sum(com_card)))
        print("Black Jack YOU WIN!!! ")
        return 2

    if sum(com_card) > 21 :
        
        print("\nYou Final hand = ",user_card,"Final score = %d "%(sum(user_card)))
        print("computer Final hand = ",com_card,"computer Final score = %d"%(sum(com_card)))
        print("You Win Com have too many points ")
        return 3
    if sum(user_card) > 21 :
        
        print("\nYou Final hand = ",user_card,"Final score = %d "%(sum(user_card)))
        print("computer Final hand = ",com_card,"computer Final score = %d"%(sum(com_card)))
        print("Com Win You have too many points !!!")
        return 4
def A_TO_11():
    if user_card.count(11) >= 1:
        while sum(user_card) > 16 and user_card.count(11) >= 2:
            user_card.insert(user_card[-1],1)
            user_card.pop(user_card.index(11))
        if len(user_card) > 2 and sum(user_card) > 21:
            user_card.insert(user_card[-1],1)
            user_card.pop(user_card.index(11))
    if com_card.count(11) >= 1:
        while sum(com_card) > 16 and com_card.count(11) >= 2:
            com_card.insert(com_card[-1],1)
            com_card.pop(com_card.index(11))
        if len(com_card) == 2 and sum(com_card) > 21:
            com_card.insert(com_card[-1],1)
            com_card.pop(com_card.index(11))
def Show_card():
    print("You card = ",user_card,"You score = %d "%(sum(user_card)))
    print("coumputer First card = ",com_card[0])

def show_score():
    print("You Final hand = ",user_card,"Final score = %d "%(sum(user_card)))
    print("computer Final hand = ",com_card,"computer Final score = %d"%(sum(com_card)))
########################################################################################

while game != 'a':
    Black_jack = input("\n Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
    if Black_jack.lower() != 'y' and Black_jack.lower()!='n':
        print("Error You type please tye again")
    elif Black_jack.lower() == 'n':
        game = 'a'

    elif Black_jack.lower() == 'y':
        deal_card()
        A_TO_11()
        Show = chack_BJ()
        if Show == 1 or Show == 2:
            Endgame = "Blackjack!!!!!!"
        
        if Endgame != "Blackjack!!!!!!":
            Show_card()
            while get != 'Get the card':
                get_card = input("\n Type 'y' to get another card, Type 'n' to pass : ")
                if get_card.lower() != 'y' and get_card.lower() != 'n':
                    print("Error You type please tye again")
                elif get_card.lower() == 'n':
                    break
                if get_card.lower() == 'y' :
                    user_card.append(random.choice(card))
                    A_TO_11()
                    Show_card()
                    if chack_BJ() == 4:
                        move = 'User lost'
                        
                        break
                   
            
            if move != 'User lost' :
                Show_card()
                while sum(com_card) < 16:
                    com_card.append(random.choice(card))
                A_TO_11()
                if chack_BJ() == 3:
                    break
                show_score()
                if sum(user_card) > sum(com_card):
                    print("!!You win!!")
                elif sum(com_card) > sum(user_card):
                    print("!!Computer Win!!")
                elif sum(com_card) == sum(user_card):
                    print("!!Draw!!")

    user_card = []
    com_card = []
    move = ""
    Endgame = ""


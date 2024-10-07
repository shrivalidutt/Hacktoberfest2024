import random

def roll():
    roll=random.randint(1,6)
    return roll

players=0
max_score=50
player_score= [0 for _ in range(players)]
#list comprehension, makes a list with 0 for every player we have

def play(i):
    current_score=player_score[i]
    while True:
        print("\nWelcome player "+ str(i+1) +"!")
        print("Your score is",player_score[i])
        
        should_roll=input("would you like to roll?|(press y to roll)(press q to end):").lower()
        if should_roll=="q":
            print("Turn done for player "+str(i+1))
            break
        if should_roll=="y":
            value=roll()
            if value==1:
                current_score=0
                print("you rolled a 1! Turn done!")
                break
            else:
                current_score+=value
                print("you rolled a:",value)
                
        else:
            print("invalid input")
            continue        
        print("your score is",current_score)
    player_score[i]=current_score
    print("your total score is",current_score)
    

while True:
    players=input("enter number of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if players>4 or players<2:
            print("must be 2-4 players")
            continue
        else:
            break
    else:
        print("invalid input.")
        continue
player_score= [0 for _ in range(players)]

while max(player_score)<max_score:
    for i in range(players):
        play(i)
    print("Score:",player_score)
winner_idx=player_score.index(max(player_score))
print("Player ",winner_idx+1," Won with score ",max(player_score))
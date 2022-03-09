import random
number = random.randint(1,9)
chances = 0
while chances < 5:
    guess = int(input("eneter ur guess"))
    if guess == number: 
        print ("CONGRATS YOU WIN!!!!!!!!!!!!!!")
        break
    elif guess < number:
        print ("SORRY UR GUESS IS TOOO LOW")
    else:
        print ("SORRY UR GUESS IS WAYYYY HIGHER THAN THE NUMBER")
    chances += 1
if not chances < 5:
    print ("U LOOOOSEEEEE",number)

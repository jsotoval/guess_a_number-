import random
def guess_a_number():
    three_guesses = 3
    random_number = random.randint(1, 10)
    number_guessed = input("Please input a guess for 1 to 10: ")
    while three_guesses > 1:
        if (int(random_number) == int(number_guessed)):
            print("Correct, the right number was " + str(users_input))
            break
        else:
            guessed_again = input("Wrong number, please guess again: ")
        three_guesses =  three_guesses - 1   
    

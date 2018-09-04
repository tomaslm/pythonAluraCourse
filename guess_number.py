import random

def play():
    print("**********************")
    print("***Guess the number***")
    print("**********************")

    max_tries = 10
    game_round = 0

    max_tries = int(input("Choose the number of tries: "))
    min_number = 0
    max_number = 10
    secret_number = random.randint(min_number, max_number)

    for iteration in range(max_tries):
        print("Iteration {} of {}: ".format(iteration, max_tries))
        user_input = int(input("    Choose a number between {} and {}: ".format(0, max_number)))
        if user_input == secret_number:
            print("You win!")
            break;
        else:
            print("Missed by {}".format(abs(user_input-secret_number)))
        

if(__name__ == "__main__"):
    play()

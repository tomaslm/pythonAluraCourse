import guess_number
import hangman

def play():
    print("***********************")
    print("***  Choose a game  ***")
    print("***                 ***")
    print("***  (H)angman      ***")
    print("***  (G)uess number ***")
    print("***                 ***")
    print("***********************")
    
    option =  input(": ")
    if option == 'H':
        guess_number.play()
    elif option == 'G':
        hangman.play()

if __name__ == "__main__":
    play();

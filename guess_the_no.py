    # Guess the Number
n = int(18)
iterations = int(0)
guess =int(10)
while(True):
    iterations = iterations+1
    guess = guess-1
    print(guess ,"Guesses Left")
    if iterations==10:
        print("Game Over!")
        break
    inp = int(input("Enter No."))
    if inp>18:
        print("Too Large")
        continue
    elif inp<18:
        print("Too Short")
        continue
    else:
        print("Congratulations! You Guess the correct No.")
        print(10-guess, "Guesses you took.")
        break

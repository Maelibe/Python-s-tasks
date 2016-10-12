print("Please think of a number between 0 and 100!")
print("Is your secret number 50 ?")
left = 0
right = 100
guess = abs(left - right)/2
while True:
    print("Enter", "'h'", " to indicate the guess is too high.", end=" ")
    print("Enter", "'l'", " to indicate the guess is too low.", end=" ")
    inp = str(input(" "))
    if inp == "l":
        left = guess
        guess = int(abs(left - right) / 2)
        guess += int(left)
        print("Is your secret number ", guess, "?")
    if inp == "h":
        right = guess
        guess = abs(left - right) / 2
        guess = int(right - guess)
        print("Is your secret number ", guess, "?")
    if inp != "c" and inp != "h" and inp != "l":
        print("Sorry, I did not understand your input.")
        print("Is your secret number ", guess, "?")
    if inp == "c":
        print("Game over.Your secret number was:", guess)
        break

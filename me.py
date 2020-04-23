import random

user = input("Enter Your Name To Begin: ")
print(f"Hi {user}, Game On!")


def guessing_game():
    play = True
    while play:

        easy_level = random.randint(1, 10)
        medium_level = random.randint(1, 20)
        hard_level = random.randint(1, 50)

        print("Type 'e' for easy level, 'm' for medium level, 'h' for hard level")

        choose_level = True
        while choose_level:
            level = input()
            if level == "e":
                print("You chose the easy level!")
                choose_level = not True
                break
            if level == "m":
                print("You chose the medium level!")
                choose_level = not True
                break
            if level == "h":
                print("You chose the hard level!")
                choose_level = not True
                break
            else:
                print("Incorrect Input.")

        if level == "e":
            print("You have 6 guesses. Guess numbers between 1 - 10")
            guess_limit = 6
            guess_limit -= 1
            while guess_limit != 0:
                guess = int(input("Please enter number: "))
            if guess == easy_level:
                print("You got it right! " + str(easy_level))

            elif guess < easy_level:
                print("That was wrong")

            elif guess > easy_level:
                print("That was wrong")

            if guess_limit == 0:
                print("Game Over!")

        if level == "m":
            print("You have 4 guesses. Guess numbers between 1 - 20")
            guess_limit = 4
            guess_limit -= 1
            while guess_limit != 0:
                guess = int(input("Please enter number: "))

                if guess == medium_level:
                    print("You got it right! " + str(medium_level))

                elif guess < medium_level:
                    print("That was wrong")

                elif guess > medium_level:
                    print("That was wrong")

                if guess_limit == 0:
                    print("Game Over!")

        if level == "h":
            print("You have 3 guesses. Guess numbers between 1 - 50")
            guess_limit = 3
            guess_limit -= 1

            while guess_limit != 0:
                guess = int(input("Please enter number: "))
                if guess == hard_level:
                    print("You bgot it right! " + str(hard_level))
                elif guess < hard_level:
                    print("That was wrong")
                elif guess > hard_level:
                    print("That was wrong")
                if guess_limit == 0:
                    print("Game Over!")

    return guessing_game()


print(guessing_game())

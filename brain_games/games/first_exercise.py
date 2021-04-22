from random import randint

import brain_games.engine
import prompt


def is_an_even_number(num, answer, name):
    if num % 2 == 0 and answer == "yes":
        return "Correct!"
    elif num % 2 == 0 and answer == "no":
        string1 = "is wrong answer ;(. Correct answer was"
        string2 = "\nLet's try again"
        template = "{}{}, {}!"
        return template.format(string1, string2, name)
    elif num % 2 != 0 and answer == "no":
        return "Correct!"
    else:
        string1 = "is wrong answer ;(. Correct answer was"
        string2 = "\nLet's try again"
        template = "{}{}, {}!"
        return template.format(string1, string2, name)


def repit_task():
    name = brain_games.engine.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        random_number = randint(1, 100)
        print("Question:", random_number)
        answer = prompt.string("Your answer: ")
        string = is_an_even_number(random_number, answer, name)
        if string == "Correct!":
            counter = counter + 1
            print(string)
        else:
            print(string)
            return
    string = "Congratulations"
    template = "{}, {}!"
    print(template.format(string, name))

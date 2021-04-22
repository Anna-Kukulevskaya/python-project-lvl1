import prompt
from random import randint
import brain_games.engine


def random_number():
    num = randint(1, 100)
    return num


def is_prime(num):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def check(num, answer, name):
    if is_prime(num) is True and answer == "yes":
        return "Correct!"
    elif is_prime(num) is False and answer == "yes":
        string1 = "is wrong answer ;(. Correct answer was"
        string2 = "\nLet\'s try again"
        template = "{}{}, {}!"
        return template.format(string1, string2, name)
    elif is_prime(num) is False and answer == "no":
        return "Correct!"
    else:
        string1 = "is wrong answer ;(. Correct answer was"
        string2 = "\nLet\'s try again"
        template = "{}{}, {}!"
        return template.format(string1, string2, name)


def repit_task():
    name = brain_games.engine.welcome_user()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    counter = 0
    while counter < 3:
        given_number = random_number()
        print("Question:", given_number)
        answer = prompt.string("Your answer: ")
        string = check(given_number, answer, name)
        if string == "Correct!":
            counter = counter + 1
            print(string)
        else:
            print(string)
            return
    string = "Congratulations"
    template = "{}, {}!"
    print(template.format(string, name))

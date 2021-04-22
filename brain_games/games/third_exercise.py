import prompt
from random import randint
import brain_games.engine


def generating_numbers():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    print("Question:", num1, num2)
    return num1, num2


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def check_the_divisor(answer_comp, answer, name):
    if answer == answer_comp:
        return "Correct!"
    else:
        string1 = "is wrong answer ;(. Correct answer was"
        string2 = "\nLet\'s try again"
        template = "{} {} {}. {}, {}!"
        return template.format(answer, string1, answer_comp, string2, name)


def repit_task():
    name = brain_games.engine.welcome_user()
    print("Find the greatest common divisor of given numbers.")
    counter = 0
    while counter < 3:
        random_numbers = generating_numbers()
        answer = int(prompt.string("Your answer: "))
        num1, num2 = random_numbers
        answer_comp = gcd(num1, num2)
        string = check_the_divisor(answer_comp, answer, name)
        if string == "Correct!":
            counter = counter + 1
            print(string)
        else:
            print(string)
            return
    string = "Congratulations"
    template = "{}, {}!"
    print(template.format(string, name))

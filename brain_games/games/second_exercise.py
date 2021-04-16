import prompt
from random import randint, choice
import engine


def generating_numbers():
    num1 = randint(1,100)
    num2 = randint(1,100)
    operators = ['+', '-', '*']
    operator = choice(operators)
    print('Question: ', num1 , operator , num2 )
    return num1, operator, num2


def calc(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2


def check(random_expression, answer, name):
    num1, operator, num2 = random_expression
    if answer == calc(num1, operator, num2):
        return 'Correct!'
    if answer != calc(num1, operator, num2):
        string1 = 'is wrong answer ;(. Correct answer was'
        string2 = '\nLet\'s try again'
        template = '{} {} {}. {}, {}!'
        return template.format(answer, string1, calc(num1, operator, num2), string2, name)
    

def repit_task():
    name = engine.welcome_user()
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        random_expression = generating_numbers()
        answer = int(prompt.string('Your answer: '))
        string = check(random_expression, answer, name)
        if string == 'Correct!':
            counter = counter + 1
            print(string)
        else:
            print(string)
            return
    string = 'Congratulations'
    template = '{}, {}!'
    print(template.format(string, name))

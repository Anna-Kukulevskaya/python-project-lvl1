import prompt
from random import randint
import brain_games.engine


def generating_numbers():
    num = randint(1,100)
    difference = randint(1,100)
    length = randint(5,10)
    n = randint(0, length - 1)
    return num, difference, length, n


def calc_answer_comp(num, difference, n):
    return num + difference * ((n + 1) - 1)


def progression(num, difference, length, n):
    result = ''
    i = 0
    while i < length:
        if i == n:
            result = result + ' ' + '..'
        else:
            result = result + ' ' + str(num)
        num = num + difference
        i = i + 1
    return result


def check(n, answer, name):
    if answer == n:
        return 'Correct!'
    else:
        string1 = 'is wrong answer ;(. Correct answer was'
        string2 = '\nLet\'s try again'
        template = '{} {} {}. {}, {}!'
        return template.format(answer, string1, n, string2, name)


def repit_task():
    name = brain_games.engine.welcome_user()
    print('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        random_sequence = generating_numbers()
        num, difference, length, n = random_sequence
        print('Question:', progression(num, difference, length, n))
        answer = int(prompt.string('Your answer: '))
        answer_comp = calc_answer_comp(num, difference, n)
        string = check(answer_comp, answer, name)
        if string == 'Correct!':
            counter = counter + 1
            print(string)
        else:
            counter = 0
            print(string)
    string = 'Congratulations'
    template = '{}, {}!'
    print(template.format(string, name))

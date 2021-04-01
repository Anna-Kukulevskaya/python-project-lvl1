import prompt

def welcome_user():
    name = prompt.string('May I have your name? ')
    greeting = 'Hello'
    template = '{}, {}!'
    print(template.format(greeting, name))
print('Welcome to Odd World of Even Steven!')
num_choice = input('Please enter a number: ')


def isOdd(number):
    return number % 2 == 1

def isEven(number):
    return number % 2 == 0

odd_even = isEven(int(num_choice))
even_odd = isOdd(int(num_choice))

if odd_even == True:
    print('That number is Even Steven!')
elif odd_even == False:
    print('That number is indeed Odd')  







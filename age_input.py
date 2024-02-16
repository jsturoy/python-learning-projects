while True:
    print ('Enter your age: ')
    age = input()
    try:
        age = int(age)

    except: 
        print('Please use numberic digits. ')
        continue

    if age < 1:
        print('Please use a positive number. ')
        continue

    break

print(f'Your age is {age}. ')
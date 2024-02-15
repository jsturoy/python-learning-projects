#ask user which temperature they want converted
print('Welcome to the Temperature Conversion Program!')
temp_choice = input('Please type 1 to convert Fahrenheit to Celsius or 2 to convert Celsius to Fahrenheit: ')

#create function to convert F to C and print temp
def convertToFahrenheit(degreesCelsius):
    print('Converting to Fahrenheit now...')
    # Calculate and return the degrees Fahrenheit:
    return int(degreesCelsius) * (9 / 5) + 32
   
#create function to convert C to F and print temp
def convertToCelsius(degreesFahrenheit):
    print('Converting to Celsius now...')
    # Calculate and return the degrees Celsius:
    return (int(degreesFahrenheit) - 32) * (5 / 9)

#if Celsius then send to F to C function
if temp_choice == str('1'):
        print('You have chose to convert to Celsius!') # Message confirming choice for F to C conversiom
        cel_temp = input('What is the temp im Fahrenheit? ') # Setting variable for user temperature input to 'cel_temp'
        fah_conv = convertToCelsius(cel_temp) #create variable to represent value of'cel_temp' converted to F after call to 'convertToCelsius' function
        print('The temperature has been converted to: ' + str(int(fah_conv)) + ' C')

#if Fahrenheit send C to F function   
if temp_choice == str('2'):
        print('You have chosen to convert to Fahrenheit!')# Message confirming choice for C to F conversion
        fah_temp = input('What is the temp in Celsius? ')# setting variable for user temperature input to 'fah_temp'
        cel_conv = convertToFahrenheit(fah_temp) #create variable to represent value of 'fah_temp' converted to C after call to 'convertToFahrenheit' function
        print('The temperature has been converted to: ' + str(int(cel_conv)) + ' F')
        print('Do you know who else hated Fahrenheit?')
        
        


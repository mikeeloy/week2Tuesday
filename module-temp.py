temp_c = input('Enter the temperature today in Celsius degress: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) +' degrees Fahrenheit.'
print(temp_statement)

hours = float(input('How many hours did you work last month? '))
rate = float(input('What is your hourly rate? '))
 
print('Last month, you earned', hours * rate ,'dollars')


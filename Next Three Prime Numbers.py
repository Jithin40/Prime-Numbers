def checkprime (number):
    if (number == 1):
        number = number + 1
    count = 1
    for i in range(1, number):
        if (number % i == 0):
            count += 1
    if (count > 2):
        number1 = number + 1
        return number1
    else:
        return number
value = checkprime(int(input('Enter the Number: ')))
while (value != checkprime(value)):
    value = checkprime(value)
value1 = value + 2
while (value1 != checkprime(value1)):
    value1 = checkprime(value1)
value2 = value1 + 2
while (value2 != checkprime(value2)):
    value2 = checkprime(value2)
print('The Prime Numbers are:',value,value1,value2)

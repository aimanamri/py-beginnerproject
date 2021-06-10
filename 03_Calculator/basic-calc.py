print('''
************************BASIC CALCULATOR****************************************
|   Press 'q' to quit or press 'c' to reset number before input the operator.  | 
|   add      :  +                                                              |
|   subtract :  -                                                              |
|   multiply :  *                                                              |
|   divide   :  /                                                              |
********************************************************************************
''')
def add(num_1,num_2):
    return float(num_1)+float(num_2)

def subtract(num_1,num_2):
    return float(num_1)-float(num_2)

def multiply(num_1,num_2):
    return float(num_1)*float(num_2)

def divide(num_1,num_2):
    if float(num_2) != 0:
        return float(num_1)/float(num_2)
    else:
        print('INVALID INPUT')

while True:

    num_1 = input('Enter num_1 : ').strip()
    if num_1 == 'q':
        print('BYE !')
        break
    num_2 = input('Enter num_2 : ').strip()
    if num_2 == 'q':
        print('BYE !')
        break
    elif num_2 == 'c':
        print('#-----------------------#')
        num_1 = input('Enter num_1 : ').strip()
        if num_1 == 'q':
            print('BYE !')
            break
        num_2 = input('Enter num_2 : ').strip()
        if num_2 == 'q':
            print('BYE !')
            break

    operator = input('Input a math operator  :  ').strip()
    if operator == 'add' or operator == '+':
        print(f'{num_1} + {num_2} = ',add(num_1,num_2))
    elif operator == 'subtract' or operator == '-':
        print(f'{num_1} - {num_2} = ',subtract(num_1,num_2))
    elif operator == 'multiply' or operator == '*':
        print(f'{num_1} x {num_2} = ',multiply(num_1,num_2))
    elif operator == 'divide' or operator == '/':
        print(f'{num_1} ÷ {num_2} = ',divide(num_1,num_2))
    else:
        print('INVALID INPUT')
    print('#-----------------------#')
# Module for calculation
def add(num_1,num_2):
    return float(num_1)+float(num_2)

def subtract(num_1,num_2):
    return float(num_1)-float(num_2)

def multiply(num_1,num_2):
    return float(num_1)*float(num_2)

def divide(num_1,num_2):
    try:
        if float(num_2) != 0:
            return float(num_1)/float(num_2)
    except:
        raise ZeroDivisionError('INVALID INPUT')


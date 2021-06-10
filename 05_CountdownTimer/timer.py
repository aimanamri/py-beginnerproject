import time
'''IN PROGRESSS ---NOT WORKING'''
input_time = int(input('Set timer for how long?'))
print('If everything all right, start now ? (y/n)')
start = input('')

while True:
    if start == 'y':
        # print('START NOW !!!')
        for i in range(input_time,0):
            print(i)
            i-=1
            if i == 0:
                break
    elif start == 'n':
        input_time = input('Set timer for how long?')
        print('If everything all right, start now ? (y/n) ')
        start = input('')
        if start == 'y':
            print('START NOW !!!')

for i in range(input_time*60):
    print(countdown = i-1)

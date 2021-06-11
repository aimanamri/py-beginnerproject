import time

def countdown():
    def confirm():
        start = input('If everything all right, start now ? (y/n) \n') # Confirmation before timer starts. User can reset the timer
        if start == 'y':
            return True
        elif start == 'n':
            return False

    start = False
    INPUT_TIME = input('Set timer for how long (minutes) ?  \n')
    start = confirm()
    if start == True:
        INPUT_TIME=int(INPUT_TIME)*60
        while INPUT_TIME: 
            mins,secs = divmod(INPUT_TIME,60) # Unpack the tuple (quotient,remainder)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r") # the next line printed will overwrite the previous one.
            time.sleep(1)
            INPUT_TIME -= 1 # Break inner loop when timer reaches 00:00
        print('TIMER ENDED')
        return 
        
    elif start == False:
        return countdown()

if __name__ == '__main__':
    countdown()
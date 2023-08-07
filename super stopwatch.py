import time

#Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                     #Press Enter to begin
print('Started')
print('Lap #, Total Time, LapTime')
startTime = time.time()     # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap time

try:
    while True:
        input()
        lapTime = round((time.time() - lastTime)/60, 2)
        totalTime = round((time.time()- startTime)/60, 2)
        print('Lap #%s: %s min (%s min. Laptime)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() #reset the last lap time
        
except KeyboardInterrupt:
    #Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    




from playsound import playsound
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #125 // 60 = 2 ,here 60 evenly divides 125 2 times.
        seconds_left = time_left % 60

        print(f"{minutes_left:02d}:{seconds_left:02d}")#02d addin decimal points

alarm(10)






        
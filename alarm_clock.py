from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


# playsound("sound.mp3")

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        hours_left = time_left // 3600
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in:{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")
    playsound(r"C:\Users\ch.avinash chowdary\Downloads\Alarm_clock-main\Alarm_clock-main\sound.mp3")


hours = int(input("how many hours to wait?"))
minutes = int(input("how many minutes to wait?"))
seconds = int(input("how many seconds to wait?"))
total_seconds = hours*3600+minutes*60+seconds
alarm(total_seconds)

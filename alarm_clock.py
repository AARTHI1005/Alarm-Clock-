import datetime
import time
import os
import platform

def ring_alarm():
    print("⏰ Alarm ringing! Wake up!")
    if platform.system() == "Windows":
        os.system("echo Alarm time! && pause")
    else:
        os.system("say 'Alarm time!'")  # macOS
        # For Linux use: os.system("spd-say 'Alarm time!'")

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            ring_alarm()
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

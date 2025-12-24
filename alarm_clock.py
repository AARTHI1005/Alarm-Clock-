import time

alarm_time = input("Enter alarm time (HH:MM): ")

print("Alarm set for", alarm_time)

while True:
    current_time = time.strftime("%H:%M")

    if current_time == alarm_time:
        print("⏰ Alarm ringing! Wake up!")
        break

    time.sleep(30)   # check every 30 seconds
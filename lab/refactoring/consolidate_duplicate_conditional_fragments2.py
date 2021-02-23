# By Kami Bigdely-Shamloo
# Consolidate duplicate conditional fragments
# This program changes car's gear according to the car speed. Then it
# displays the updated gear on the car's front panel.

def change_gear(str_gear):
    print("Gear changed to", str_gear)


def display_gear(str_gear):
    print("displayed gear:", str_gear)


def process_speed(speed):
    if speed <= 0:
        display_gear('R')
        return
    gear = ""
    if speed > 0 and speed <= 30:
        gear = '1'
    elif speed > 30 and speed <= 50:
        gear = '2'
    elif speed > 50 and speed <= 90:
        gear = '3'
    elif speed > 90:
        gear = '4'
        change_gear(gear)
        display_gear(gear)


if __name__ == "__main__":
    process_speed(40)

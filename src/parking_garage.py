import time
from datetime import datetime

DEPLOYMENT = False # This variable is to understand if we are running this code on the actual hardware

try:
    import RPi.GPIO as GPIO
    import SDL_DS3231
    DEPLOYMENT = True
except:
    import mock.GPIO as GPIO
    import mock.SDL_DS3231 as SDL_DS3231


class ParkingGarage:

    # Pin number declarations
    INFRARED_PIN1 = 11
    INFRARED_PIN2 = 12
    INFRARED_PIN3 = 13
    SERVO_PIN = 16
    LED_PIN = 18

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.INFRARED_PIN1, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN2, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN3, GPIO.IN)
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        self.rtc = SDL_DS3231.SDL_DS3231(1, 0x68)
        self.servo = GPIO.PWM(self.SERVO_PIN, 50)
        self.servo.start(2)  # Starts generating PWM on the pin with a duty cycle equal to 2% (corresponding to 0 degree)
        if DEPLOYMENT:
            time.sleep(1)  # Waits 1 second so that the servo motor has time to make the turn (only if DEPLOYMENT = True)
        self.servo.ChangeDutyCycle(0)  # Sets duty cycle equal to 0% (corresponding to a low signal)
        self.door_open = False
        self.red_light_on = False
        GPIO.output(self.LED_PIN, False)

    def check_occupancy(self, pin: int) -> bool:
        if pin in [self.INFRARED_PIN1, self.INFRARED_PIN2, self.INFRARED_PIN3]:
            return GPIO.input(pin)
        raise ParkingGarageError

    def get_number_occupied_spots(self) -> int:
        count = 0
        for pin in [self.INFRARED_PIN1, self.INFRARED_PIN2, self.INFRARED_PIN3]:
            if self.check_occupancy(pin):
                count += 1
        return count

    def calculate_parking_fee(self, entry_time: datetime) -> float:

        exit_time = self.rtc.read_datetime()

        entry_hour = entry_time.hour
        exit_hour = exit_time.hour

        entry_minute = entry_time.minute
        exit_minute = exit_time.minute

        count = exit_hour - entry_hour
        if exit_minute - entry_minute > 0:
            count += 1

        fee = count * 2.5
        if exit_time.weekday() in [5, 6]:
            fee = fee * 1.25

        return fee

    def open_garage_door(self) -> None:
        self.change_servo_angle(12)
        self.door_open = True

    def close_garage_door(self) -> None:
        self.change_servo_angle(2)
        self.door_open = False

    def turn_on_red_light(self) -> None:
        GPIO.output(self.LED_PIN, True)
        self.red_light_on = True

    def turn_off_red_light(self) -> None:
        GPIO.output(self.LED_PIN, False)
        self.red_light_on = False

    def manage_red_light(self) -> None:
        if self.get_number_occupied_spots() == 3:
            self.turn_on_red_light()
        else:
            self.turn_off_red_light()

    def change_servo_angle(self, duty_cycle):
        """
        Changes the servo motor's angle by passing it the corresponding PWM duty cycle
        :param duty_cycle: the PWM duty cycle (it's a percentage value)
        """
        self.servo.ChangeDutyCycle(duty_cycle)
        if DEPLOYMENT:
            time.sleep(1)
        self.servo.ChangeDutyCycle(0)


class ParkingGarageError(Exception):
    pass

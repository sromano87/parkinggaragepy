import mock.GPIO as GPIO
import mock.RTC as RTC
import time


class ParkingGarage:

    # Pin number declarations
    INFRARED_PIN1 = 11
    INFRARED_PIN2 = 12
    INFRARED_PIN3 = 13
    RTC_PIN = 15
    SERVO_PIN = 16
    LED_PIN = 18

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.INFRARED_PIN1, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN2, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN3, GPIO.IN)
        GPIO.setup(self.RTC_PIN, GPIO.IN)
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        self.rtc = RTC.RTC(self.RTC_PIN)
        self.servo = GPIO.PWM(self.SERVO_PIN, 50)
        self.servo.start(2)  # Starts generating PWM on the pin with a duty cycle equal to 2% (corresponding to 0 degree)
        time.sleep(1)  # Waits 1 second so that the servo motor has time to make the turn
        self.servo.ChangeDutyCycle(0)  # Sets duty cycle equal to 0% (corresponding to a low signal)
        self.door_open = False
        self.light_on = False

    def check_occupancy(self, pin: int) -> bool:
        # To be implemented
        pass

    def get_occupied_spots(self) -> int:
        # To be implemented
        pass

    def calculate_parking_fee(self, entry_time: str) -> float:
        # To be implemented
        pass

    def open_garage_door(self) -> None:
        # To be implemented
        pass

    def close_garage_door(self) -> None:
        # To be implemented
        pass

    def turn_light_on(self) -> None:
        # To be implemented
        pass

    def turn_light_off(self) -> None:
        # To be implemented
        pass

    def change_servo_angle(self, duty_cycle):
        """
        Changes the servo motor's angle by passing it the corresponding PWM duty cycle
        :param duty_cycle: the width of the PWM duty cycle (it's a percentage value)
        """
        self.servo.ChangeDutyCycle(duty_cycle)
        time.sleep(1)
        self.servo.ChangeDutyCycle(0)


class ParkingGarageError(Exception):
    pass

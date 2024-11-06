# parkinggaragepy
_parkinggaragepy_ is a smart system to manage a small parking garage with only three spots.

The system includes the following sensors and actuators:
* Three infrared distance sensors, one for each parking spot;
* A servo motor to open/close the garage door;
* A Real Time Clock (RTC) to handle time operations;
* A red smart lightbulb to indicate when the garage is full.

The communication between the main board and the other components happens through GPIO pins. The communication is already configured in the BOARD mode (i.e., GPIO pins are referred to by their physical number on the board).

## Instructions for You
* You are asked to develop _parkinggaragepy_ by following TDD.
* You DO NOT need to develop a GUI.
* You CANNOT change the signature of the provided methods, move the provided methods to other classes, or change the name of the provided classes. However, you CAN add fields, methods (e.g., methods used by tests to set up the fixture or methods used by the provided methods), or even classes (including other test classes), as long as you comply with the provided API.
* You CAN use the internet to consult Python APIs or QA sites (e.g., StackOverflow).
* You CANNOT use AI tools (e.g., ChatGPT).
* You CANNOT interact with your colleagues. Work alone and do your best!
* The _parkinggaragepy_ requirements are divided into a set of USER STORIES, which serve as a to-do list (see the _Issues_ session).
* You should be able to incrementally develop _parkinggaragepy_ without an upfront comprehension of all its requirements. DO NOT read ahead, and handle the requirements (i.e., specified in the user stories) one at a time in the provided order. Develop _parkinggaragepy_ by starting from the first story’s requirement. When a story is IMPLEMENTED, move on to the NEXT one. A story is implemented when you are confident that your program correctly implements the functionality stipulated by the story's requirement. This implies that all your test cases for that story and all the test cases for the previous stories pass. You may need to review your program as you progress toward more advanced requirements.
* Each time you end a TDD phase, COMMIT.
* If you need to handle error situations (including situations unspecified by the user stories), throw a `ParkingGarageError`.

## API Usage
Take some minutes to understand, in broad terms, how the API works. If you do not fully understand the API, do not worry because further details will be given in the user stories (see the _Issues_ session).

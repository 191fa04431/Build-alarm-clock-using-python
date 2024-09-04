# Python Countdown Alarm
A simple Python script that creates a customizable countdown timer with an audio alarm. Users can set hours, minutes, and seconds for the countdown. The script displays a real-time updating countdown in the terminal and plays a sound when the timer reaches zero.

## Features:
- User-defined countdown duration
- Real-time countdown display in the terminal
- Audio alarm using the 'playsound' library
- Attempts to use ANSI escape codes for screen clearing (may not work in all environments)

## Requirements:
- Python 3.x
- playsound library

## Usage:
1. Install the required library: `pip install playsound`
2. Run the script: `python alarm.py`
3. Enter the desired hours, minutes, and seconds when prompted
4. Wait for the alarm to sound

Note: Ensure you have a 'sound.mp3' file in the same directory as the script for the alarm sound.

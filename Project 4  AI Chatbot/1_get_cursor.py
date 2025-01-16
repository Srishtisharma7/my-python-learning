import pyautogui

# pyautogui: A library used for automating mouse movements, clicks, and keyboard actions. In this case, it helps to get the current cursor position.

# Infinite Loop:
# Continuously monitors and prints the cursor's position as long as the script runs.÷
while True:
    a = pyautogui.position()           # eturns the current position of the mouse as a Point object containing (x, y) coordinates.
    print(a)
    # 1639, 1412
    # 1003 237 to 2187 1258
    # 1026 244
    # to 1131 1321'''

# include a way to exit the loop, such as listening for a keyboard interrupt.

try:
    while True:
        a = pyautogui.position()
        print(a)
except KeyboardInterrupt:
    print("Program exited.")
   
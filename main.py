from PIL import ImageGrab
import ctypes
import keyboard
import time


cell_coords = [
    [777, 409], [875, 409], [1035, 409], [1112, 409],
    [777, 500], [875, 500], [1035, 500], [1112, 500],
    [777, 650], [875, 650], [1035, 650], [1112, 650],
    [777, 744], [875, 744], [1035, 744], [1112, 744]
]


while True:
    if keyboard.is_pressed('s'):
        break


while True:
    image = ImageGrab.grab()
    for i in range(len(cell_coords)):
        x = cell_coords[i][0]
        y = cell_coords[i][1]
        r, g, b = image.getpixel((x, y))
        # color = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
        color = (r+g+b)/3
        if color == 0:
            ctypes.windll.user32.SetCursorPos(x, y)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
            ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

    if keyboard.is_pressed('q'):
        break
    time.sleep(0.1)


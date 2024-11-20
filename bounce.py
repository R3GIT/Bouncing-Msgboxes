import win32api
import win32con
import win32gui
import random
import threading
import time

def bounce_system_message():
    hwnd = win32api.MessageBox(
        0, 
        "ERROR: Something went wrong!", # Message Change it if you want to
        "Critical Error", # Title Change it if you want to
        win32con.MB_ICONERROR | win32con.MB_OK
    )
    
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    hwnd = win32gui.GetForegroundWindow()
    if not hwnd:
        return

    x, y = random.randint(0, screen_width - 300), random.randint(0, screen_height - 100)
    dx, dy = random.choice([-5, 5]), random.choice([-5, 5])

    while True:
        x += dx
        y += dy

        if x <= 0 or x + 300 >= screen_width:
            dx = -dx 
        if y <= 0 or y + 100 >= screen_height:
            dy = -dy 

        
        win32gui.MoveWindow(hwnd, x, y, 300, 100, True)
        time.sleep(0.01)

def spam_bouncing_system_messages():
    while True:
        threading.Thread(target=bounce_system_message, daemon=True).start()
        time.sleep(random.uniform(0.2, 0.5))

spam_bouncing_system_messages()

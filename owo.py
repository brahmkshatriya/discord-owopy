#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import keyboard
import threading
import os
import random

time_randomness = 2

current_dir = os.path.dirname(os.path.abspath(__file__))
profile_path = os.path.join(current_dir, "chrome-profile")
if not os.path.exists(profile_path):
    os.makedirs(profile_path)

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={profile_path}")
driver = webdriver.Chrome(options=options)

driver.get("https://discord.com/app")

working = True
send_messages = False
def loop(message:str, duration:int):
    while working:
        if(send_messages):
            print(message)
            send_message(message)
            time.sleep(duration + random.randint(0, time_randomness))

hunt = threading.Thread(target= lambda : loop("owo h", 15))
battle = threading.Thread(target= lambda : loop("owo b", 20))

def send_message(message):
    print(f"Message : {message}")
    try:
        message_field = driver.find_element(By.XPATH, '//div[@role="textbox"][@contenteditable="true"]')
        message_field.send_keys(message+Keys.RETURN)
    except:
        print("Message field not found.")
        close()
    print("Message sent.")


def close():
    keyboard.unhook_all()
    global working
    working = False
    driver.quit()
    print("Quitting.")

def on_key_event(event):
    global send_messages
    global working
    if event.name == 'f7':
        send_messages = not send_messages
        print(f"on : {send_messages}")

    if event.name == 'f8':
        close()

keyboard.on_press(on_key_event)

print("Press F7 to start/stop sending messages. Press F8 to quit.")
hunt.start()
battle.start()
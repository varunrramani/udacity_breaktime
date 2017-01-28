import webbrowser
import time

i = 0

while (i < 3):
    time.sleep(5)
    if (i == 0):
        webbrowser.open("https://www.youtube.com/watch?v=9sBIknREhqw")
    elif (i == 1):
        webbrowser.open("https://www.youtube.com/watch?v=BdqB0ij5rFs", 0, False)
    elif (i == 2):
        webbrowser.open("https://www.youtube.com/watch?v=gg5AqN1F8L0", 0, False)
    i = i + 1

print ("Done!")

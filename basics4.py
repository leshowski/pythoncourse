import time
import os

while True:
    if os.path.exists("files/continents.txt"):
        with open("files/continents.txt") as content_file:
            print(content_file.read())
    else:
        print("Sorry for the inconvenience")

    time.sleep(3)
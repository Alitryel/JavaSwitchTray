import os

import pystray
import subprocess
import PIL.Image

image = PIL.Image.open("icon.ico")


def os_button(icon, item):
    if str(item) == "Config":
        print("Open config")
    elif str(item) == "Exit":
        icon.stop()


def java_switchers(icon, item):
    if str(item) == "Java 8":
        os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-8"
        subprocess.run(["setx", "JAVA_HOME", os.environ["JAVA_HOME"]], shell=True)


    elif str(item) == "Java 11":
        os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-11.0.2"
        subprocess.run(["setx", "JAVA_HOME", os.environ["JAVA_HOME"]], shell=True)


    elif str(item) == "Java 17":
        os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-17.0.2"
        subprocess.run(["setx", "JAVA_HOME", os.environ["JAVA_HOME"]], shell=True)


    elif str(item) == "Java 19":
        os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-19.0.1"
        subprocess.run(["setx", "JAVA_HOME", os.environ["JAVA_HOME"]], shell=True)


icon = pystray.Icon('ITStart', image, menu=pystray.Menu(
    pystray.MenuItem("Java 8", java_switchers),
    pystray.MenuItem("Java 11", java_switchers),
    pystray.MenuItem("Java 17", java_switchers),
    pystray.MenuItem("Java 19", java_switchers),
    pystray.MenuItem("Config", os_button, enabled=False),
    pystray.MenuItem("Exit", os_button)
))

icon.run()

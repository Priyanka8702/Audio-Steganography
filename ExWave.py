import wave
import argparse
import matplotlib.pyplot as plt
import pyttsx3

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
args = parser.parse_args()
af = args.audiofile
arged = False
if af:
    arged = True

def help():
    print("\033[92mExtract Your Secret Message from Audio Wave File.\033[0m")
    print('''usage: ExWave.py [-h] [-f AUDIOFILE]
    
    optional arguments:
      -h, --help    show this help message and exit
      -f AUDIOFILE  Select Audio File''')

def reveal_message(event):
    if event.button == 1:  # Check for left mouse button click
        plt.close()  # Close the current plot
        secret_message = "The secret message is: Code RED!"
        print(secret_message)  # Print the secret message to console

        # Read the secret message aloud
        engine = pyttsx3.init()
        engine.say(secret_message)
        engine.runAndWait()

def ex_msg(af):
    if not arged:
        help()
    else:
        text = "The sky is blue!"

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.text(0.5, 0.5, text, ha='center', va='center', fontsize=14, fontweight='bold')
        plt.axis('off')  # Turn off axes for a clean display
        plt.connect('button_press_event', reveal_message)  # Connect mouse click event
        plt.show()

try:
    ex_msg(af)
except:
    print("Something went wrong! Try again.")

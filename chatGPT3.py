import openai
import os
import numpy as np
from dotenv import load_dotenv
import sys
import time
load_dotenv()

os.system("title ChatGPT-3 Conversation")
os.system("cls")

ascii_art = r"""
         ________  ________  _________              ________     
        |\   ____\|\   __  \|\___   ___\           |\_____  \    
        \ \  \___|\ \  \|\  \|___ \  \_|___________\|____|\ /_   
         \ \  \  __\ \   ____\   \ \  \|\____________\   \|\  \  
          \ \  \|\  \ \  \___|    \ \  \|____________|  __\_\  \ 
           \ \_______\ \__\        \ \__\              |\_______\
            \|_______|\|__|         \|__|              \|_______|
                                                                 
                                                                 
"""

##ascii art
color_start = np.array([182, 255, 130])  # #b6ff82
color_end = np.array([31, 250, 2])      # #1ffa02

# Generate the gradient array
gradient = np.linspace(color_start, color_end, 80)

# Print the ASCII art with color gradient
for line in ascii_art.split('\n'):
    for i in range(len(line)):
        if line[i] == ' ':
            sys.stdout.write(' ')
        else:
            color = gradient[i]
            sys.stdout.write(f"\x1b[38;2;{int(color[0])};{int(color[1])};{int(color[2])}m{line[i]}\x1b[0m")
    sys.stdout.write('\n')
    sys.stdout.flush()


from colorama import init
init()

BOLD = "\033[1m"
RESET = "\033[0m"
bold_text = "\033[1;97m{}\033[0m"

var=os.getenv('CHAT_KEY')
if var:
    pass
else:
    print("\033[1;31mNo key found - run HELP and follow the instructions\033[97m")

while True:
    prompt = input(bold_text.format(" >> "))
    if prompt == "exit":
        break
    if prompt == "help" or "HELP":
        print("""\033[1;94mSetup can be done by :
  ● Visiting https://beta.openai.com/signup
  ● Personal > View API keys
  ● Clicking "create new secret key"
  ● Copying it and clicking create
  ● Opening the .env file and pasteing the key there
  \033[1;31m
  ● RESTARTING THE SCRIPT\033[97m""")
        break
    openai.api_key = os.getenv('CHAT_KEY')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    print(f"\033[38;2;107;242;65m🖩 ChatGPT: {message}\033[97m")
while True:
    time.sleep(1)

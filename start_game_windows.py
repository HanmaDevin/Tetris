#! /bin/python

import os, time

def pause():
    time.sleep(1)

def exec(cmd):
    return os.system(cmd)

print("Welcome to the Tetris-Game starter script\n")
pause()
print("First we are going to install pygame\n")
if exec("pip --version") != 0:
    exec("winget install pip")

print("Now we are are going to install pygame\n")
pause()
exec("pip install pygame")

print("Now we need to install git, if not already installed\n")
pause()

if exec("git --version") != 0:
    exec("winget install git")

print("You will have to configure git, but i am going to help you\n")
pause()
email = input("You need to type your github email adress: ")
user_name = input("Type your github username: ")

exec("git config --global user.name " + user_name)
exec("git config --global user.email " + email)

print("Almost done, cloning the repository\n")
pause()
repo = "https://github.com/HanmaDevin/Tetris"
exec("git clone " + repo)

print("Only thing to do is to change the directory and start the game\n")
pause()
exec("cd Tetris/game")

print("Have fun with the game")
pause()

exec("python3 main.py")
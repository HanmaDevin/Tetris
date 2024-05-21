#! /bin/python
import subprocess
import os

def run(cmd):
    completed = subprocess.Popen('powershell.exe [cmd]')
    return completed

print("Welcome to the Tetris-Game starter script")
print("First we are going to install pygame")

cmd = "python3 --version" 
run(cmd)
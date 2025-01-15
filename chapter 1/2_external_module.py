#Install an external module and use it to perform an operation of your interest.
import pyttsx3
engine = pyttsx3.init()
engine.say("""I will speak this text
           anything you want multiple strings too""")
engine.say("I love you Srishti")
engine. runAndWait()


import pyjokes
joke = pyjokes.get_joke() #module importing pyjoke
print (joke)

"""MODULES :A module is a file containing code writen by somebody else (usually which can be imported and used in our programs
PIP : Pip is the package manager for python. You can use pip to install a module on your system.
(trple double quotes or triple single quotes)
There are two types of modules in Python.
1. Built in modules {presinstalled in python} eg: os, random,etc.{multiple line comment}"""
# 2. External modules {need to install using pip} eg: tensorflow ,flask ,etc.{single line comment}
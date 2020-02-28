#!/bin/python3

# This file will input data into a file or any command desired


# Import configuration
from config import rootPath, inboxPath, prefixText, sufixText

# Import regex
import re
import os

def writeToFile(path, data):
        f = open(path,"a+") # append
        f.write(prefixText + data + sufixText)
        f.close()

def printData (data):
        writeToFile(inboxPath, data)

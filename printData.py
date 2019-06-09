#!/bin/python3

# This file will input data into a file or any command desired


# Import configuration
from config import rootPath, inboxPath, personPath, placePath, projectPath

# Import regex
import re
import os

def writeToFile(path, data):
        f = open(path,"a+") # append
        f.write("- [ ] " + data + "\n")
        f.close()



def printData (maData):
        if "@" in maData:
                name = re.search('@(.*)@',maData).group(1)
                print(name)
                # This is a person that is being referenced
                # Will create two tasks, one in inbox and other
                # in @person-name
                path = os.path.join(personPath,name + '.md')
                # Replace name with link
                myMatch = '@' + name + '@'
                myReplace = '[' + name + '](' + path + ')'
                maData = maData.replace(myMatch, myReplace)
                # Place data in file
                writeToFile(path,maData)

        if "#" in maData:
                name = re.search('#(.*)#',maData).group(1)
                print(name)
                path = os.path.join(placePath,name + '.md')
                myMatch = '#' + name + '#'
                myReplace = '[' + name + '](' + path + ')'
                maData = maData.replace(myMatch, myReplace)
                writeToFile(path,maData)

        if "%" in maData:
                name = re.search('%(.*)%',maData).group(1)
                print(name)
                path = os.path.join(projectPath,name + '.md')
                myMatch = '%' + name + '%'
                myReplace = '[' + name + '](' + path + ')'
                maData = maData.replace(myMatch, myReplace)
                writeToFile(path,maData)
                
        writeToFile(inboxPath,maData)

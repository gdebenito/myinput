import os

try:
    rootPath = os.getenv('MYINPUT_ROOT_PATH')
    inboxPath = rootPath + "Inbox.md"
except:
    print("MYINPUT_ROOT_PATH env not defined.")
    print("Use: export MYINPUT_ROOT_PATH=/home/" + os.getenv('USER') +" in your .zshrc or .bashrc file.")
    exit()
prefixText= "- [ ] "
sufixText= "\n"

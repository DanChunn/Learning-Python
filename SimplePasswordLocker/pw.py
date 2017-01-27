#! python3
# pw.py - A modified password locker from https://automatetheboringstuff.com/chapter6/
# Used as Python practice, not for actual use.

def simpleStrongPassword(word):
    if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', word):
        return True
    else:
        return False

fileObj = open('dictionary.py', 'a+') #allows read and creates file if it doesn't exist
import sys, pyperclip, pprint, dictionary, re

if hasattr(dictionary, 'PASSWORDS'):
    PASSWORDS = dictionary.PASSWORDS
else:
    PASSWORDS = {}

if len(sys.argv) < 2 or len(sys.argv) > 3: #if incorrect arg #, do nothing
    print('Usage:')
    print('pw.py [ACCOUNT]             * used to retrieve [ACCOUNT] password *')
    print('pw.py [ACCOUNT] [PASSWORD]  * used to store [ACCOUNT] and [PASSWORD] *')
    sys.exit()

elif len(sys.argv) == 2:    # if 2 args then retrieve password to clipboard
    account = sys.argv[1]   # first command line arg is the account name

    if(account in PASSWORDS):
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)
        
elif len(sys.argv) == 3:    # if 3 args then create/modify account with password
    account = sys.argv[1]   # first command line arg is the account name
    password = sys.argv[2]  # second command line arg is the account password
    
    if not (simpleStrongPassword(password)):
       print('Poor password entered.')
       
    if(account in PASSWORDS):
        if(PASSWORDS[account] == password):
            print('You must enter a different password. Try again.')
        else:
            PASSWORDS[account] = password
            print('Password for ' + account +' overwritten.')
            
    else:
        PASSWORDS.setdefault(account,password)
        print('Password for ' + account +' added.')

fileObj = open('dictionary.py', 'w')
fileObj.write('PASSWORDS = ' + pprint.pformat(PASSWORDS) + '\n')
fileObj.close





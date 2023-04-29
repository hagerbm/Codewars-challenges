
# Challenge Description:
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"


# My solution
def to_camel_case(text):
    result=""
    if len(text)>1:
        uppercase_next=False
        
        for c in text:
#             Check if the character is a letter
            if c.isalpha():
#               if uppercase_next flag is ON, uppercase the current letter and reset the flag 
                if uppercase_next==True:
                    c=c.upper()
                    uppercase_next=False
                
#           if the character is a dash or an underscore:
#           discard it from result and turn on the uppercase_next flag
            elif c == '_'or c == '-':
                c=""
                uppercase_next=True
#           concatenate the character into the result
            result+=c
            
    return result

# Other Best Practice Solutions
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

    def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)

def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])

def to_camel_case(text):
    cap = False
    newText = ''
    for t in text:
        if t == '_' or t == '-':
            cap = True
            continue
        else:
            if cap == True:
                t = t.upper()
            newText = newText + t
            cap = False
    return newText
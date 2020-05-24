import os
import sys

class UCFirst:
    def __init__(self, args):
        self.path = args[0]
    
    def make_change(self):
        for name in os.listdir(self.path):
            words = name[:-4].split()
            filename = self.path + name 
            newname = self.path 
            for word in words:
                newname = newname + word[:1].upper() + word[1:] + ' '
            newname = newname[:-1] + name[-4:]
            os.rename(filename, newname)

class ReplaceName:
    def __init__(self, args):
        self.path = args[0]
        self.oldword = args[1]
        self.newword = args[2]
    
    def make_change(self):
        for name in os.listdir(self.path):
            words = name[:-4].split()
            print(str(words))
            filename = self.path + name
            newname = self.path 
            for word in words:
                print(word)
                if word == self.oldword:
                    newname = newname + self.newword + ' '
                else:
                    newname = newname + word + ' '
            newname = newname[:-1] + name[-4:]
            os.rename(filename, newname)


actions = {
    'ucfirst': UCFirst,
    'replace_name': ReplaceName,
}


name, funcname, *args = sys.argv
action = actions[funcname](args)
action.make_change()









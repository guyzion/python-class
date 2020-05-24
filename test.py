import os
import sys

class UCFirst:
    def __init__(self, args):
        self.path = 'music/'
    
    def make_change(self):
        for name in os.listdir(self.path):
            filename = self.path + name 
            newname = self.path + name.title()
            os.rename(filename, newname)

class ReplaceName:
    def __init__(self, args):
        self.path = 'music/'
        self.oldword = args[0]
        self.newword = args[1]
    
    def make_change(self):
        for name in os.listdir(self.path):
            filename = self.path + name
            newname = self.path + name.replace(self.oldword, self.newword)
            os.rename(filename, newname)


class AddNewFile:
    def __init__(self, args):
        self.path = 'music/'
        self.filename = args[0]
    
    def make_change(self):
        open(self.path + self.filename, 'w+')
    
class RenameByFormat:
    def __init__(self, args):
        self.path = 'music/'
        self.fromFormat = args[0]
        self.toFormat = args[1]

    def make_change(self):
        for name in os.listdir(self.path):
            words = name[:-4].split()
            nwords = []
            j = 0
            for i in range(0, len(words)):
                if j > 0 and words[i].isalpha() and all(x.isalpha() or x.isspace() for x in nwords[j-1]):
                    nwords[j-1] = nwords[j-1] + ' ' + words[i]
                else:
                    nwords.append(words[i])
                    j = j + 1
            ffdic = {}
            ffarr = self.fromFormat.split()
            for i in range(0,len(ffarr)):
                ffdic[ffarr[i]] = nwords[i]
            newname = self.path
            for t in self.toFormat.split():
                try:
                    newname = newname + ffdic[t] + " "
                except:
                    newname = newname + t + " "
            newname = newname[:-1] + name[-4:]
            os.rename(self.path + name, newname)

actions = {
    'UCFirst': UCFirst,
    'ReplaceName': ReplaceName,
    'AddNewFile': AddNewFile,
    'RenameByFormat': RenameByFormat,
}

name, funcname, *args = sys.argv
action = actions[funcname](args)
action.make_change()










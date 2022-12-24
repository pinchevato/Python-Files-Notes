#MACROS - doesn't work as .py file cuz there is no fucking god
dirlist = []
for f in dirlist:
    print("working on", f)
    print("done with", f)
    print("moving %s to %s.done" % (f, f))
    print("*" * 40)
#Create Macro, the "2" refers to the line #, so this will work if 'dirlist' is on line 1
macro procdir 2
#Use Macro
dirlist = ['a.txt', 'b.txt', 'c.txt']
procdir

#the editor doesn't work, but you can edit macros
%edit procdir

#if you ever wanna store PERSISTENTLY one of these useless cunts
#the -d variable function deletes the specified
#variable from the persistence store; -z function deletes all stored
#variables; and the -r function reloads all variables from the
#persistence store.
store procdir

#!/usr/bin/env python

#BIG QUESTION: most of this will not execute in IDLE..
#but will  in IPYTHON... WHY?!?!

#string processing the system shell command output
# "!" before a command executes it via shell
ps = !ps -e
ps.grep('chrome')
#return all processes that DON'T include the regular expression
ps.grep('sys', prune=True)
#only return certain fields (columns)
ps.grep('chrome').fields(0)
#turn it into a string
ps.grep('chrome').fields(0).s
#magic command page
%page ps

#'Callback' - grep will take a function as an argument n call that function
import os
file_list = !ls
#return files, not directories
file_list.grep(os.path.isfile)
#return directories nto files
file_list.grep(os.path.isdir)

#hist magic command
hist -n #numbered list
hist -t #translated view - the "REAL" commands - 'behind the scenes' (???)
hist -g hist #searched history for all entries containing "hist" - like $grep

# the "_" refers to the last entry, so this will set a to the output of last line
'foo_string'
a= _

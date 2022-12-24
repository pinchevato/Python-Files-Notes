#prints $uname -sv command but I DON'T UNDERSTAND SYNTAX AT ALL :'(

import subprocess
res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
uname = res.stdout.read().strip()
print(uname)

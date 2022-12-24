from pathlib import Path

vulva = Path("ecommerce")
print("Does path ./ecommerce exist:\n" + str(vulva.exists()))

# Use Path to search!
# W/O argument, Path just uses current directory
butt = Path("/home/chavo/Documents")
# .glob method allows us to search for files/dir's
# but the following only some object info BS idk
print(butt.glob('*'))
# so we need to iterate thru the object
for penis in butt.glob('*'):
    print(penis)

dirr = Path('.')
x=0
for j in dirr.iterdir():
    if j.is_dir():
        x += 1
print("There are " + str(x) +
      " directories in this folder\n\n..n "
      "here's all the fuckin python files.. hmmderrp!")

for j in dirr.glob('*.py'):
    print(j)

#######################################
# FROM: youtu.be/DOgjN7RmHds

# Just importing whole lib cuz idk wtf to use here..
import pathlib
# This Dunder method creates path object for THIS file
this = pathlib.Path(__file__)
print("\nThis file's path & location are " + str(this))
print("The file's pure path is " + str(pathlib.PurePosixPath(__file__)))
print("Who knows wtf the difference is :-|")
print("\nSplit directory into a list:")
print(this.parts)
print("\nParent directory using .parent method:")
print(this.parent)
print("\nParent of parent dir using .parent.parent :")
print(this.parent.parent)
print("\nUsing .parents method w index 3:")
print(this.parents[3])
print("\nUsing .joinpath method to make up whatev path:")
joined_path = this.parent.joinpath('balls')
print(joined_path)
print("\nCheck to see if this dir exists, if not make it w .mkdir method:")
if not joined_path.exists():
    joined_path.mkdir()
print("\nUsing .touch method to create a new file:")
nfile = joined_path.joinpath('scrotum.txt')
print(nfile)
nfile.touch(exist_ok=True)
# If file already exists & we put exist_ok=False, returns Error
# ..but we don't have to pass any arg to the .touch method

print("\nSee code to see wtf all this is:")
print(this.is_dir())
print(this.is_file())
# dunno what a symbolic link is yet
print(this.is_symlink())
# this returns an empty result, not sure why
print(this.drive)
# things you can do w jut the filename
print(this.stem)
print(this.suffix)
print(this.name)
print(this.anchor)

# More methods not using the 'this' obj I created
print("\nUse .cwd method 'current working directory':")
print(pathlib.Path.cwd())
print("Use .home method to print home directory:")
print(pathlib.Path.home())
# According to vid this might be useful if u don't know
# what user is doing.. ??
print("Use .absolute method to add 'data' str to path\n"
      "(dunno how this differs from .joinpath method)")
print(pathlib.Path('data').absolute())
# Takes last part 'setup.py' n attaches it to cwd
print("\nUse .resolve method to make up new shit.\n"
      "Here, using 'anus/../setup.py' ..don't really get it:")
print(pathlib.Path('anus/../setup.py').resolve())
print("\nWe can use .resolve to convert Windows path to\n"
      "Linux path - HE SAYS IT'S REALLY USEFUL\n"
      "..but again don't really get it.. yet:")
print(pathlib.Path('C:/Users/Dingus/pythonshit.py').resolve())

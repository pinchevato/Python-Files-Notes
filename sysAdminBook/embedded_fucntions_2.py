#Very short script that reuses embedded_functions code
from embedded_fucntions import disk_func
import subprocess
def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print("Space used in /tmp directory")
    subprocess.call([tmp_usage, tmp_arg, path])
def main():
    disk_func()
    tmp_space()
if __name__ == "__main__":
    main()

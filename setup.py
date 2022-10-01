from sys import executable
from os import system, name

from subprocess import check_call
import time

def install():
    if name == "nt":
       system('reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000001 /f')
    print(f"Installing Requirements Package...")
    time.sleep(1)
    python = executable
    check_call([python, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    print("Successfully Installed Requirements Package! You're Good To Go")
if __name__ == "__main__":
    install()

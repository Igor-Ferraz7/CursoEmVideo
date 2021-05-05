import time, emoji
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print(emoji.emojize(':boom:'*10,  use_aliases = True))
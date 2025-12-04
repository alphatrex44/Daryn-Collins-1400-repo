s = "()())("
x = 0
for i in s:
    if i =="(":
        x += 1
    if i ==")":
        x += -1
    if x < 0:
        break
if x != 0:
    print(False)
else:
    print(True)
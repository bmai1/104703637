txt = input()
for i in range(len(txt)):
    if txt[i] == ' ':
        print('...', end='')
    else:
        print(txt[i], end='')
print('')
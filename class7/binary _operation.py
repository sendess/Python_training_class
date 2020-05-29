with open('diff_code','rb')as f:
    print(f.read())
    f.seek(0)
    print(f.tell())
    print(f.read().decode('cp437'))

with open('testing.txt', 'w', encoding = "UTF-16") as f:
    f.write('My lawwwwd')
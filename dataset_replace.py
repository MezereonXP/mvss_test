import os


with open('./data/train.txt', 'r', encoding='u8') as f:
        data = f.read()
        data = data.replace("\t", " ")
        with open('./data/train.txt', "w", encoding='u8') as f:
            f.write(data)

with open('./data/val.txt', 'r', encoding='u8') as f:
    data = f.read()
    data = data.replace("\t", " ")
    with open('./data/val.txt', "w", encoding='u8') as f:
        f.write(data)

print('ok')
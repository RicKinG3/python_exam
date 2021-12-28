# -*- coding: utf-8 -*-

# Данно 2 файла .bin  отсортировать их и соединить в другой тож отсортированный
import struct
import random


def show_file(base, size):
    s = []
    size = size // 8
    base.seek(0)
    for i in range(size):
        a = base.read(8)
        a = struct.unpack('q', a)
        s += a
    print(s)


def sort_file(base, size):
    size = size // 8
    base.seek(0)
    for k in range(size):
        gap = size
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))  # minimum gap is 1
            swaps = False
            for i in range(size - gap):
                base.seek(i * 8)
                j = i + gap
                a = base.read(8)
                base.seek(j * 8)
                b = base.read(8)
                if struct.unpack('q', a)[0] > struct.unpack('q', b)[0]:
                    base.seek(j * 8)
                    base.write(a)
                    base.seek(i * 8)
                    base.write(b)
                    swaps = True
    return base


file_1 = open('file_1b.txt', 'wb')
file_1 = open('file_1b.txt', 'rb+')
file_2 = open('file_2b.txt', 'wb')
file_2 = open('file_2b.txt', 'rb+')
file_3 = open('file_3b.txt', 'wb')
file_3 = open('file_3b.txt', 'rb+')
n = 1000

for i in range(n):
    rand = random.randint(-1000, 1000)
    rand1 = random.randint(-1000, 1000)
    file_1.write(struct.pack('q', rand))
    file_2.write(struct.pack('q', rand1))

size_1 = file_1.tell()
size_2 = file_2.tell()

print("file before")
show_file(file_1, size_1)
show_file(file_2, size_2)

print()
print('file after')
sort_file(file_1, size_1)
sort_file(file_2, size_2)
show_file(file_1, size_1)
show_file(file_2, size_2)

file_1.seek(0)
file_2.seek(0)
for i in range(n):
    file_3.write(file_1.read(8))
    file_3.write(file_2.read(8))

size_3 = file_3.tell()
print()
print("file 3 before")
show_file(file_3, size_3)
print()
print("file 3 after")
sort_file(file_3, size_3)
show_file(file_3, size_3)
file_1.close()
file_2.close()
file_3.close()
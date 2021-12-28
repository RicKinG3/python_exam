# -*- coding: utf-8 -*-

# Данно 2 файла .txt отсортировать их и соединить в другой тож отсортированный в обратном порядке
from random import randint

file_1 = open('file_1.txt', 'w')
file_1 = open('file_1.txt', 'r+')
file_2 = open('file_2.txt', 'w')
file_2 = open('file_2.txt', 'r+')
file_3 = open('file_3.txt', 'w')
file_3 = open('file_3.txt', 'r+')
n = 100
for i in range(n):
    s, m = randint(-10, 10), randint(-10, 10)
    s, m = str(s), str(m)
    file_1.write(s)
    file_2.write(m)
size_1 = file_1.tell()
size_2 = file_2.tell()


def show_file(base, size):
    base.seek(0)
    str_all = ' '
    for i in range(size):
        str_all += base.read(i)
    print(str_all)
    return str_all


print("file before")
show_file(file_1, size_1)
show_file(file_2, size_2)
print()


def revers_buble_sort(base, size):
    base.seek(0)
    for i in range(size - 1):
        for j in range(size - i - 1):
            base.seek(j)
            a = base.read(1)

            if a == '-':
                a += base.read(1)
            b = base.read(1)
            if b == '-':
                b += base.read(1)

            base.seek(j)
            if a <= b:
                base.seek(j)
                base.write(b)
                base.write(a)


print("file after")
revers_buble_sort(file_1, size_1)
revers_buble_sort(file_2, size_2)
show_file(file_1, size_1)
show_file(file_2, size_2)

file_1.seek(0)
file_2.seek(0)
file_3.seek(0)
print()
for i in range(size_1):
    a = file_1.read(1)
    b = file_2.read(1)
    if a == "-":
        a += file_1.read(1)

    if b == "-":
        b += file_2.read(1)
    file_3.write(a)
    file_3.write(b)
print("file_3 after file_1 + file_2")
revers_buble_sort(file_3, size_2 + size_1)
show_file(file_3, size_1 + size_2)
file_1.close()
file_2.close()
file_3.close()
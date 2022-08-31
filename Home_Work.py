import math

# 1) Напишите программу, которая посчитает сколько букв «b» в введенной строке текста.

text = input("Input text: ")

print(text.count("b"))

# 2) Считайте строку, которая будет представлять имя человека, введенное с клавиатуры. Проверьте эту строку на валидность. Имеется в виду, что
# например, в имени человека не может быть цифр, оно должно начинаться с большой буквы, за которой должны следовать маленькие.

name = input("Name: ")

first_letter = name[0]
name_without_first_letter = name[1::]

if name.isalpha() and not first_letter.islower() and name_without_first_letter.islower():
    print("Everything is fine")
else:
    print("Name isn't valid")


# 3) Напишите программу, которая вычислит сумму всех кодов символов строки.

summ = 0

for letter in text:
    summ += ord(letter)

print(summ)


# 4) Выведите на экран 10 строк со значением числа Pi. В первой строке должно быть 2 знака после запятой, во второй 3 и так далее.

counter = 0
fractional_part = 2

while counter < 10:
    print(round(math.pi, fractional_part))

    fractional_part += 1
    counter += 1

# 5) Вводится строка из слов, разделенных пробелами. Найти самое длинное слово и вывести его на экран.

list_of_words = text.split(" ")
list_of_lenghts = []

for word in list_of_words:
    list_of_lenghts.append(len(word))

biggest_word = list_of_lenghts.index(max(list_of_lenghts))

print(list_of_words[biggest_word])

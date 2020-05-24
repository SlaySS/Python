import random

file_with_words = "original.txt"

file = open(file_with_words, mode="r", encoding="utf-8")

random_lines = random.choice(file.readlines())
word = random_lines.strip('\n')
print(word)


secret_word = []
for i in word:
    secret_word.append("_")

print(secret_word)

while True:
    letter = input("Веедите букву :")
    if letter in word:
        print("Такая буква есть !")
        secret_word[word.index(letter)] = letter
        print(secret_word)
    else:
        print("Такой буквы нет")


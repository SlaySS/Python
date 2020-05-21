number = list(input('Введите число: '))
a = ''
reverse_a = ''

for i in number:
    a += i
number.reverse()
for i in number:
    reverse_a += i


print(a)
print(reverse_a)

if a == reverse_a:
    print("Palindrom")
else:
    print("Not palindrom")

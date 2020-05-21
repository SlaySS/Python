# spisok = input("Введите список букв латинского алфавита: ")
#
# glasn = [litera for litera in spisok if litera.lower() in 'aeiou']
#
# print('Гласные буквы в вашем списке это: ' + str(glasn))

def count_vowels(str):
    glasn = [litera for litera in str if litera.lower() in 'aeiou']
    return len(glasn)



a = count_vowels('dibnwefvwe')
print(a)
def iq_test(numbers):
    list = [int(i) for i in numbers.split(' ')]
    print(list)
    odd = [i for i in list if int(i) % 2 == 0]
    even = [e for e in list if int(e) % 2 != 0]
    odd_even = len(odd) - len(even)
    if odd_even > 0:
        iq_number = even
    else:
        iq_number = odd
    iq_num = iq_number[0]
    return list.index(iq_num)+1


a = ("51 47 1 33 20 41 43 49 5 37 1 3 19 17 1 17 45 11 21 49 11 9 49 3 13 39 3 39 49 39 17 45 39 25 3 35")

print(iq_test(a))

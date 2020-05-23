roman = dict(I=1, V=5, X=10)


def rim_arabic(rim):
    rim_number = 0
    for i, c in enumerate(rim):
        if i+1 < len(rim) and roman[c] < roman[rim[i+1]]:
            rim_number -= roman[c]
        else:
            rim_number += roman[c]
    return rim_number

print(rim_arabic("XXIX"))

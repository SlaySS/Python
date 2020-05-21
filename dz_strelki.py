def whos_first(p1, p2):
    diff = p1.find('B') - p2.find('B')
    if diff == 0:
        return 'tie'
    if diff > 0:
        return 'p2'
    else:
        return 'p1'


st1 = '   Baff    '
st2 = '   Baff   '

print(whos_first(st1, st2))

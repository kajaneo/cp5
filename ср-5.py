try:
    x=int(input('введите место: '))
except ValueError:
    print('ошибка')
else:
    if x<1 or x>54: print('ошибка')
    else:
        if x%2==0: print('верхнее')
        else: print('нижнее')
        if x<37: print('в купе')
        else: print('боковое')

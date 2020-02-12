def get_summ(one, two, delimiter='&'):
    summ = str(one) + delimiter + str(two)
    return summ

#print(get_summ('Learn', 'python', '+').upper())

def format_price(price):
    return 'Цена: ' + str(int(price)) + ' рублей.'

price_int = (format_price(56.23))
print(price_int)
print(len(price_int))
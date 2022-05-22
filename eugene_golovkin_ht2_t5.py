# не все дополнительные задачи выполнены, но основные да
prices_list = [45.8, 59.1, 56, 98, 105.52, 26, 896.12, 14, 56, 89.6]
new_prices_list = []

for price in prices_list:
    if type(price) == int:
        price = f'{price} руб {0:02d} коп'
        new_prices_list.append(price)
    else:
        x1 = int(price)
        x2 = price
        price2 = f'{x1} руб {int(x2 % 1 * 101):02d} коп'
        new_prices_list.append(price2)

print(new_prices_list, end=' ')





# f"{} руб {} коп"
# print(type(prices_list[0]))
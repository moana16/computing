price = 3575000
total_price = price * 8
print(total_price)

next_price = price * 1.067
print(next_price)

price_upgrade = price
for x in range(10) :
    price_upgrade = price_upgrade * 1.047
    
print(price_upgrade)
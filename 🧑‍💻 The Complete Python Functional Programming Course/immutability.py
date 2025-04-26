def add_tax(amount):
    return amount+amount*tax_rate

def add_discount(amount):
    discount = 10
    return amount *(100-discount)/100

amount = 100
print("Initial amount: ", amount)
amount_with_tax = add_tax(amount)
print("Amount with tax: ", amount_with_tax)
amount_with_discount = add_discount(amount_with_tax)
print("Final amount after tax and discount: ", amount_with_discount)
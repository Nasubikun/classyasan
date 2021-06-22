from classes import Price

p = Price(2980)
print(p.get_price(tax=8,isFloat=True))
# 3,218.4円

from classes import PhoneNumber

pn1 = PhoneNumber("0120123456")
print(pn1.get_phoneNumber())
# 0120-123-456

pn2 = PhoneNumber("08011119999")
print(pn2.get_phoneNumber())
# 080-1111-9999

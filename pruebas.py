from collections import OrderedDict

od = OrderedDict()

od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4



od[list(od.items())[0][0]] = 'ahora'
# tamp = list(od.items())
print(od)

# print(od.items()[1])
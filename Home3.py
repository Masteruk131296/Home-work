
weight=int(input("какой у вас вес в килограммах ? : "))
growth=float(input("какой у вас рост в сантиметрах ?: "))
bmi=int(weight/(growth**2) *(100**2))
print('Ваш индекс массы тела = ', bmi)
first = bmi - 20
scale = '20' + "=" * first + str("|") + "="*(30 - first) + "50"
print (scale)

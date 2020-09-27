def gen(start, stop):
    while True:
        if start > stop:
            return
        yield start
        start += 1

j = gen(0, 1000)
for i in j:
    if i % 3 == 0:
        print('Василий')
    else:
        print(i)
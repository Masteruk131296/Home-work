creds = {'Dennis': '123', 'Jenya': '321','Nastya':'000'}
def auth_requared(func):
    def wrapper_decorator(c, b):
        c = input('Введите логин :')
        b = input('Введите пароль :')
        for key in creds:
            if key == c and creds[key] == b:
                return print('Верно')
        print('Данные введены некоректно,попробуйте снова:')
        return wrapper_decorator(c, b)
    return wrapper_decorator

@auth_requared
def some_func(c, b):
     return (b + c)

some_func('Dennis','123')



# creds = {'Dennis': '123', 'Jenya': '321','Nastya':'000'}
# def wrapper_decorator():
#     c = input('Введите логин :')
#     b = input('Введите пароль :')
#     for key in creds:
#         if key == c and creds[key] == b:
#              return print('Верно')
#     print('Данные введены некоректно,попробуйте снова:')
#     return wrapper_decorator()
#
# wrapper_decorator()




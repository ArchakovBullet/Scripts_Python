global_var =1

def my_vars():
    print('Глобальная переменная global_var\t', global_var)
    local_var = 2
    print('Локальная переменная  local_var\t', local_var)
    global inner_var
    inner_var = 3


my_vars()
print('Вторая глобальная переменная global inner_var\t', inner_var)
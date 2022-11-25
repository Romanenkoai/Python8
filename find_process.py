from import_proces import data_access_read, data_access_write


def find_process():
    data = data_access_read()
    pole = input ('Введите параметр (название колонки): ') 
    
    if not pole in data[0]: 
        print('Такого параметра нет')
        return
    else: pole_i = data[0].index(pole)
    
    finding = input ('Введите запрос: ')

    for i in range(1,len(data)):
        if data[i][pole_i] == finding: print (' | '.join(data[i]))







if __name__ == '__main__':
    data_access_write ([['id', 'full_name', 'date_birth', 'telephone'], ['5', '6', '7', '8'], ['6', 'Zhikh AA', '12.12.1988', '+7999777154']])
    find_process()

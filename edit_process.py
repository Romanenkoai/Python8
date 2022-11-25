from import_proces import data_access_read
from import_proces import data_access_write

def add_record():
    data = data_access_read()
    temp_data = []
    for i in data[0]:
        if i == 'id':
            temp_data.append (str(int(data [len(data)-1][0]) + 1))
            continue           
        temp_data.append(input(f'Введите содержание поля "{i}": '))
    data.append(temp_data)
    data_access_write (data)


if __name__ == '__main__':
    data_access_write ([['id', 'full_name', 'date_birth', 'telephone'], ['5', '6', '7', '8'], ['6', 'Zhikh AA', '12.12.1988', '+7999777154']])
    add_record()
    print (data_access_read())

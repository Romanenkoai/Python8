from pathlib import Path
from data_file_proces import name_input_f

delimeter = 0


input_data =[]


def data_access_read():
    global input_data
    return input_data

def data_access_write(new_data):
    global input_data
    input_data = new_data
    print('Данные перезаписаны')


def import_from_csv (file_name, delimeter = ","):

    global input_data
    input_data =[]
    with open(file_name, "r") as f:
        for line in f:

            data = []
            end_s = 0

            end_s = line.find('\n', end_s+1)
            line = line [0:end_s]
            data = line.split(delimeter)

            input_data.append (data)
    print('Данные перезаписаны')
    return input_data
            


def  import_proces():
    global input_data

    file_name = name_input_f()
    file_extension = Path(file_name).suffix

    if file_extension == ".csv":

        import_from_csv(file_name)
    
    elif file_extension == ".tsv":
        import_from_csv(file_name, '\t')
    
    else: return []


    print(input_data)
    return input_data

if __name__ == '__main__':
    import_proces ()

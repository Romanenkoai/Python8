from pathlib import Path
from data_file_proces import name_input_f


def  export_proces(data):
    file_name = name_input_f()
    file_extension = Path(file_name).suffix

    if file_extension == ".csv":
        delimeter = ','
        with open(file_name, "w") as f:
            for i in data:
                f.write(delimeter.join(i) + '\n') 

    elif file_extension == ".tsv":
        with open(file_name, "w") as f:
            for i in data:
                f.write('\t'.join(i) + '\n') 
    


    else: file_extension = 0
    return file_extension       




if __name__ == '__main__':
    data = [['1', '2', '3', '4'], ['5', '6', '7', '8']]
    export_proces (data)

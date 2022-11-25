# Доделать решение задачи: Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы


from find_process import find_process
from import_proces import import_proces
from export_proces import export_proces
from print_data import print_data
from redactor_menu import redactor_menu


def menu_main():
 
    begin = True
    while begin:
        
        print ('------ \n Введите число для соответствующей задачи или иное для выхода: ')
        print ('   0.\t Отобразить список')
        print ('   1.\t Импорт файла')
        print ('   2.\t Экспорт в файл')
        print ('   3.\t Редактирование')
        print ('   4.\t Поиск записей')

        program = int(input())
        print ()
        
        if program == 0:
            print_data()

        elif program == 1:
            data = import_proces()
            if data != []:
                input('Данные импортированы \nЧтобы продолжить, нажмите Enter.')
            else: input(f'Неизвестный формат \nЧтобы продолжить, нажмите Enter.')

        elif program == 2:
            form = export_proces(data)
            if form != 0:
                input(f'Данные экспортированы в формате {form} \nЧтобы продолжить, нажмите Enter.')
            else: input(f'Неизвестный формат \nЧтобы продолжить, нажмите Enter.')

        elif program == 3:
            redactor_menu()

        elif program == 4:
            find_process()       


        else:
            begin = False

if __name__ == '__main__':
    menu_main()

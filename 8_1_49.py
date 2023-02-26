# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. 
# Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# (*) Усложнение.
# Сделать тесты для функций
# Разделить на model-view-controller

import view
import model


def menu():
    phone_book_main = []
    while True:
        choice = view.show_menu()
        if choice == "":
            print("до новых встреч")
            break
        elif choice == "c":
            rec = model.create_rec(*view.new_rec(mode = "new"))
            phone_book_main.append(rec)
        elif choice == "r":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            view.show_recs(recs)
        elif choice == "u":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            if recs:
                idx = phone_book_main.index(recs[0])
                rec = model.create_rec(*view.new_rec(mode = "update"))
                rec = model.merge(rec, recs[0])
                phone_book_main[idx] = rec
        elif choice == "d":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            if recs:
                idx = phone_book_main.index(recs[0])
                phone_book_main.pop(idx)
        elif choice == "i":
            filename = view.file_name()
            recs = model.import_file(filename)
            phone_book_main.extend(recs)
        elif choice == "e":
            filename = view.file_name()
            model.export_file(filename, phone_book_main)
        elif choice == "s":
            view.show_all_recs(phone_book_main)
        else:
            print("Недопустимый пункт меню")
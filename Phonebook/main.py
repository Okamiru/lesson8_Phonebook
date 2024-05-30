import os

menu = True

phonebookName="phon.txt"


def clear():
  os.system("cls")

def draw():
  print("━" * 25)

# Функция для чтения файла
def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    try:
        with open(filename, 'r', encoding='utf-8') as phb:
            for line in phb:
                record = dict(zip(fields, line.split(',')))
                phone_book.append(record)
        return phone_book
    except FileNotFoundError:
        return (f"Ошибка: Файл '{filename}' не найден.")
    
# Функция для вывода красивого справочника
def print_data(book):
    headers = ["№".ljust(3, ' '), "Фамилия".ljust(10, ' '), "Имя".ljust(10, ' '), "Телефон".ljust(13, ' '), "Описание".ljust(63, ' ')]
    print("-" * 117) # Верхняя граница таблицы
    print(f"| {' | '.join(headers)}   |")
    print("-" * 117) # Разделитель под заголовками
    for i, record in enumerate(book, 1):
        values = [str(i).ljust(3, ' '), record['Фамилия'].ljust(10, ' '), record['Имя'].ljust(10, ' '), record['Телефон'].ljust(13, ' '), record['Описание'].strip().ljust(65, ' ')]
        print(f"| {' | '.join(values)} |")
    print("-" * 117) # Нижняя граница таблицы


# Функция для поиска записи
def findInBook(where, what):
    findedEntryOut = []
    for i in bookInMemory: 
        if what in i[where]:
            findedEntryOut=[i]
    return findedEntryOut


        
# Стандартно при запуске считываем наш справочник phon.txt в bookInMemory. Далее работаем с bookInMemory
bookInMemory=read_txt(phonebookName)


# print(read_txt("phon1.txt"))

# print(read_txt("phon.txt"))

while menu:
    draw()
    print(f"Выбран справочник: {phonebookName} ")
    draw()
    print("┌─────────────────────────┐")
    print("│  Телефонный справочник  │")
    print("├─────────────────────────┤")
    print("│ 1. Открыть справочник   │")
    print("│ 2. Поиск по справочнику │")
    print("│ 4. Добавление записей   │")
    print("│ 5. Сохранить и выйти    │")
    print("│ 6. Выбор справочника    │")
    print("│ 7. Копировать справочник│")
    print("│ 0. Выйти без сохранения │")
    print("└─────────────────────────┘")
    draw()
    choice = input("# Введите команду > ")
    
    
    if choice == "1": # 1. Открыть справочник
      clear()
      menu=False
      draw()
      print_data(bookInMemory)
      draw()
      # print(bookInMemory)
      # draw()
      input("> Нажмите Enter, чтобы продолжить ")
      menu=True



    elif choice == "2": # 2. Поиск по справочнику
      menu=False
      draw()
      print("┌─────────────────────────┐")
      print("│  Поиск по справочнику   │")
      print("├─────────────────────────┤")
      print("│ 1. Поиск по фамилии     │")     
      print("│ 2. Поиск по имени       │")
      print("│ 3. Поиск по номеру      │")     
      print("└─────────────────────────┘")
      draw()
      choice3 = input("# Введите команду > ")
      if choice3 == "1":
        entry=input("> Введите фамилию: ")
        fentry=findInBook('Фамилия', entry)
        if fentry==[]:
          print("# Записей не найдено!")
          input("> Нажмите Enter, чтобы продолжить ")
          clear()
          menu=True
        else:
          print_data(fentry)        
          input("> Нажмите Enter, чтобы продолжить ")
          menu=True
      elif choice3 == "2":
        entry=input("> Введите имя: ")
        fentry=findInBook('Имя', entry)
        if fentry==[]:
          print("# Записей не найдено!")
          input("> Нажмите Enter, чтобы продолжить ")
          menu=True
        else:
          print_data(fentry)        
          input("> Нажмите Enter, чтобы продолжить ")
          menu=True
      elif choice3 == "3":
        entry=input("> Введите номер: ")
        fentry=findInBook('Телефон', entry)
        if fentry==[]:
          print("# Записей не найдено!")
          input("> Нажмите Enter, чтобы продолжить ")
          menu=True
        else:
          print_data(fentry)        
          input("> Нажмите Enter, чтобы продолжить ")
          menu=True




    elif choice == "4": # 4. Добавление записей
      pass
    elif choice == "5": # 5. Сохранить и выйти
      pass
    elif choice == "6": # 6. Выбор справочника 
      pass
    elif choice == "7": # 7. Копировать справочник
      pass
    elif choice == "0": # 0. Выйти без сохранения 
      clear()
      menu=False
      draw()
      print("# Вы уверены, что хотите выйти без сохранения?(Введите Да если уверены)")
      print()
      print("! " * 10)
      print("# ВНИМАНИЕ! ВСЕ ВНЕСЁННЫЕ В СПРАВОЧНИК ИЗМЕНЕНИЯ БУДУТ ОТМЕННЕНЫ!")
      print("! " * 10)
      draw()
      choice2=input("> ")
      if choice2=="Да":
        clear()
        quit()
      else:
         clear()
         menu=True

      
       






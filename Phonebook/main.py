import os
import os.path

menu = True

phonebookName="phon.txt"

# Чистка терминала, просто для красоты.
def clear():
  os.system("cls")

# Разделитель, просто для красоты
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
    
# Функция для записи в файл   
def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}')  
    
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
            findedEntryOut.append(i)
    return findedEntryOut  

# Функция добавления новой записи
def newEntry(book,f,n,p,d):
    add = {'Фамилия': f, 'Имя': n, 'Телефон': p, 'Описание': d}
    book.append(add)


        
# Стандартно при запуске считываем наш справочник phon.txt в bookInMemory. Далее работаем с bookInMemory
bookInMemory=read_txt(phonebookName)


# print(read_txt("phon1.txt"))

# print(read_txt("phon.txt"))
clear()

while menu:
    draw()
    print(f"Выбран справочник: {phonebookName} ")
    draw()
    print("┌─────────────────────────┐")
    print("│  Телефонный справочник  │")
    print("├─────────────────────────┤")
    print("│ 1. Открыть справочник   │")
    print("│ 2. Поиск по справочнику │")
    print("│ 3. Добавление записей   │")
    print("│ 4. Сохранить            │")
    print("│ 5. Выбор справочника    │")
    print("│ 6. Копировать справочник│")
    print("│    или строку           │")
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
          clear()
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
          clear()
          menu=True
        else:
          print_data(fentry)        
          input("> Нажмите Enter, чтобы продолжить ")
          menu=True




    elif choice == "3": # 3. Добавление записей
      menu=False
      clear()
      draw()
      print("")
      choice4 = input("# Режмм добавления новой записи. Введите 1 чтобы продолжить, или 0, чтобы вернуться в основное меню ")
      if choice4 == "1":
        f = input("> Введите фамилию: ")
        n = input("> Введите имя: ")
        p = input("> Введите номер телефона: ")
        d = input("> Введите короткое описание: ")
        draw()
        print(f"Будет добавлена следующая запись: 'Фамилия': {f}, 'Имя': {n}, 'Телефон': {p}, 'Описание': {d})")
        choice5 = input("# Если запись вас устраивает нажмите 1: ")
        draw()
        if choice5 == '1':
          newEntry(bookInMemory,f,n,p,d)
          print("# Запись добавлена!")
          input("> Нажмите Enter, чтобы продолжить ")
          clear()
          menu=True
        else:
          clear()
          menu=True
        
      else:
         menu=True
      
    elif choice == "4": # 4. Сохранить
      write_txt(phonebookName,bookInMemory)


    elif choice == "5": # 5. Выбор справочника 
      menu = False
      phonebookName=input("Введите название книги: ") + ".txt"
      if os.path.exists(phonebookName):
        bookInMemory=read_txt(phonebookName)
      else:
        print("#Такого файла не существует ")
        input("> Нажмите Enter, чтобы продолжить ")
        phonebookName="phon.txt" 
      menu = True

    elif choice == "6": # 6. Копировать справочник
      menu=False
      draw()
      print("# Вы в режиме копирования справочника:")
      print("# Можно копировать как весь справочник, так и конкретную строку")
      print("# Вам необходимо будет выбрать режим копирования, и имя справочника в который будет производиться копирование")
      print("# Если справочника с укзанным вами именем не существует, будет создан новый справочник")
      draw()
      print("# Режмим 1: Копирование всего справочника. ВНИМАНИЕ: Справочник будет перезаписан")
      print("# Режмим 2: Копирование строки.")
      choice6 = input("> Выберите режим 1 или 2: ")
      if choice6 == "1":
        copyBook = input("# Введите имя справочника ") + ".txt"
        write_txt(copyBook,bookInMemory)
        print(f"Копирование выполнено в справочник {copyBook} ")
        input("> Нажмите Enter, чтобы продолжить ")
        clear()
        menu = True
      elif choice6 == "2":
        clear()
        copyBook = input("# Введите имя справочника: ") + ".txt"
        draw()
        print_data(bookInMemory)
        draw()
        while True:
          strNum = int(input("# Введите номер строки для копирования: "))
          try:
            num = int(strNum)
            break 
          except ValueError:
            print("Ошибка. Допускаются только целые числа")

        if os.path.exists(copyBook):
          secondBookInMemory=read_txt(copyBook)
          strNum -= 1 #Так как пользователь вводит номер не с 0 нужно отнять 1 чтобы выбирать верный индекс
          newEntry(secondBookInMemory,bookInMemory[strNum]['Фамилия'],bookInMemory[strNum]['Имя'],bookInMemory[strNum]['Телефон'],bookInMemory[strNum]['Описание'])
          write_txt(copyBook,secondBookInMemory)
          print(f"#Строка {strNum} скопирована, и помещена в файл {copyBook} ")
          input("> Нажмите Enter, чтобы продолжить ")
          menu=True
        else:  
          secondBookInMemory=[]
          secondBookInMemory=[bookInMemory[0]]
          write_txt(copyBook,secondBookInMemory)
          print(f"#Строка {strNum+1} скопирована, и помещена в файл {copyBook} ")
          input("> Нажмите Enter, чтобы продолжить ")
          menu=True

    elif choice == "0": # 0. Выйти без сохранения 
      clear()
      menu=False
      draw()
      print("# Вы уверены, что хотите выйти без сохранения?(Введите Да если уверены)")
      print()
      print("! " * 10)
      # print("# ВНИМАНИЕ! ВСЕ ВНЕСЁННЫЕ В СПРАВОЧНИК ИЗМЕНЕНИЯ БУДУТ ОТМЕННЕНЫ!")
      draw()
      choice2=input("> ")
      if choice2=="Да" or choice2=="1":
        clear()
        quit()
      else:
         clear()
         menu=True

      
       






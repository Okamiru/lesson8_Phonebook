import os

menu = True

def clear():
  os.system("cls")

def draw():
  print("━" * 25)

#Читаем наш файл в phone_book
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
        
  
# print(read_txt("phon1.txt"))

# print(read_txt("phon.txt"))

while menu:
    draw()
    print("┌─────────────────────────┐")
    print("│  Телефонный справочник  │")
    print("├─────────────────────────┤")
    print("│ 1. Открыть справочник   │")
    print("│ 2. Поиск по фамилии     │")
    print("│ 3. Поиск по номеру      │")
    print("│ 4. Добавление записей   │")
    print("│ 5. Сохранить и выйти    │")
    print("│ 6. Выбор справочника    │")
    print("│ 7. Копировать справочник│")
    print("│ 0. Выйти без сохранения │")
    print("└─────────────────────────┘")
    draw()
    choice = input("# Введите команду > ")
    
    
    if choice == "1": # 1. Открыть справочник
      pass
    elif choice == "2": # 2. Поиск по фамилии
      pass
    elif choice == "3": # 3. Поиск по номеру
      pass
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

      
       






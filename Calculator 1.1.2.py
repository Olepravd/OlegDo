#WOC Calculator
#Version 1.1.2
#OD Studio
#2024

print("WOC Calculator\nVersion: 1.1.2\nOlegDo AB\n2024\n")

print("Hello!\nWelcom to WOC Calculator\n")

langcho=1
lang=1
tran=["Watch the operations","1-Sum","2-Subtraction","3-Multiplication","4-Division","5-Settings","6-Help","7-About","8-Finish work","Write the number of the operation","Write the first number","Write the second number","Settings","What languge you want to see? (1=English,2=Russian)","Write the language number","Error S01","The information isn't correct.","Error I01","Please, write correct information"]
trah=["Watch the articles",'1-Article 1 "How use"','2-Article 2 "List of errors"','3-Article 3 "How use help"','4-Finish work',"Write the number of the operation","When you start program, select a move.\n If you select 1-4, then write the first and the second number and see an answer.\n If you select 5, then write a language number and your language will be sated.\n If you select 6, then read “How use help?”\n If you select 7, then read about.\n If you select 8, then the program will exit.","HO1-incorrectly choose in Help.\nSO1-incorrectly choose in Settings.\nIO1- incorrectly choose in Menu.","When you start Help, select a move.\n• If you select 1, read “How use?”. \n• If you select 2, read “List of errors”.\n• If you select 3, then read “How use help?”\n• If you select 4, then the program will exit from Help.","Error H01","The information isn't correct.","Write right information"]
while True:
        for i in range(0,9):
            print(tran[i])

        choise=input(tran[9])
        if choise in ('1','2','3','4'):
            
            a=float(input(tran[10]))
            b=float(input(tran[11]))
            if choise=='1':
                print(a,"+",b,"=",a+b)
            elif choise=='2':
                print(a,"-",b,"=",a-b)
            elif choise=='3':
                print(a,"*",b,"=",a*b)
            elif choise=='4':
              print(a,"/",b,"=",a/b)

        elif choise=='5':
          print(tran[12])
          print(tran[13]) 
          langcho=input(tran[14])
          if langcho in ("1","2"):
                  if langcho=="1":
                      tran=["Watch the operations","1-Sum","2-Subtraction","3-Multiplication","4-Division","5-Settings","6-Help","7-About","8-Finish work","Write the number of the operation","Write the first number","Write the second number","Settings","What languge you want to see? (1=English,2=Russian)","Write the language number","Error S01","The information isn't correct.","Error I01","Please, write correct information"]
                      trah=["Watch the articles",'1-Article 1 "How use"','2-Article 2 "List of errors"','3-Article 3 "How use help"','4-Finish work',"Write the number of the operation","When you start program, select a move.\n If you select 1-4, then write the first and the second number and see an answer.\n If you select 5, then write a language number and your language will be sated.\n If you select 6, then read “How use help?”\n If you select 7, then read about.\n If you select 8, then the program will exit.","HO1-incorrectly choose in Help.\nSO1-incorrectly choose in Settings.\nIO1- incorrectly choose in Menu.","When you start Help, select a move.\n• If you select 1, read “How use?”. \n• If you select 2, read “List of errors”.\n• If you select 3, then read “How use help?”\n• If you select 4, then the program will exit from Help.","Error H01","The information isn't correct.","Write right information"]
                      lang=1
                  elif langcho=='2':
                      tran=["Посмотрите операции","1-Сложение","2-Вычитание","3-Умножение","4-Деление","5-Настройки","6-Помощь","7-О продукте","8-Завершить работу","Напишите номер операции","Напишите первое число","Напишите второе число","Настройки","Какой язык вы хотите видеть? (1=Английский, 2=Русский)","Напишите номер языка","Ошибка S01","Информация не корректна».","Ошибка I01","Пожалуйста, введите корректную информацию"]
                      trah=["Смотреть статьи", "1-Статья 1" ,"Как пользоваться", "2-Статья 2", "Список ошибок", "3-Статья 3","Как пользоваться справкой","4-Завершить работу","Напишите номер операции", "При запуске программы выберите ход.\n Если вы выбрали 1-4, то напишите первую и вторую цифру и увидите ответ.\n Если вы выбрали 5, то напишите номер языка, и ваш язык будет насыщен.\n Если вы выбрали 6, то прочтите 'Как пользоваться справкой?'\n Если вы выбрали 7, то прочтите о.\n Если вы выбрали 8, то программа завершит работу.", "HO1-неправильно выбрано в Справке.\nSO1-неправильно выбрано в Настройках.\nIO1-неправильно выбрано в Меню.", "При запуске Справки выберите ход.\n• Если вы выбрали 1, то прочтите 'Как пользоваться?'. \n• Если вы выбираете 2, читаете «Список ошибок».\n• Если вы выбираете 3, читаете «Как пользоваться справкой?»\n• Если вы выбираете 4, то программа выйдет из справки.","Ошибка H01","Информация неверна.","Введите правильную информацию"]
                      lang=2
          else:
             print(tran[15])
             print(tran[16])
             print(tran[18])
        elif choise =='6':
                while True:
                    print (trah[0])
                    print (trah[1])
                    print (trah[2])
                    print (trah[3])
                    print (trah[4])

                    choise=input(trah[5])
                    if choise in ('1','2','3'):
                        if choise=='1':
                          print(trah[6])
                        elif choise=='2':
                          print(trah[7])
                        elif choise=='3':
                          print(trah[8])

                    elif choise =='4':
                        break
                    elif choise != ('1','2','3','4'):
                         print(trah[9])
                         print(trah[10])
                         print(trah[11])
        elif choise =='7':    
             print("Name: Woc Calculator\nVersion:1.1.2\nCreator:OlegDo AB\nYear:2024")
        elif choise =='8':
            break
        elif choise != ('1','2','3','4','5','6','7','8'):
             print(tran[17])
             print(tran[16])
             print(tran[18])
        print("")



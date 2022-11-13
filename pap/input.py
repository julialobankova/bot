def input_number():
    while True:
        a = input('Введите число: ')
        try:
            return float(a)
        except:
            try:
                x = float(a.strip('j'))
                while True:
                    y = input("Введите реальную часть комплексоного числа ")
                    try:
                        return complex(float(y),x)
                    except:
                        print('Не верный ввод, попробуйе снова ')
            except:
                print('Не верный ввод, попробуйе снова ')

def input_operation():
    while True:
        print('Введите номер операции: ')
        print('1 - "+"')
        print('2 - "-"')
        print('3 - "*"')
        print('4 - "/"')
        op = input()
        if op not in ['1','2','3','4']:
            print("Error")
            continue
        return op



#Введите номер операции:\n 1 - "+"\n 2 - "-"\n 3 - "*"\n  4 - "/"\n
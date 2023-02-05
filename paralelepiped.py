try:
    n1 = float(input("Введите длину: "))
    n2 = float(input("Введите ширину: "))
    n3 = float(input("Введите высоту: "))
    
    n4 = (n1*n2 + n1*n3 + n3*n2)*2
    print("Пл. поверхности --", n4)
except:
    print("Произошла ошибка!")
    


input()

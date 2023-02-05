try:
    n1 = int(input("Введите длину: "))
    n2 = int(input("Введите ширину: "))
    n3 = int(input("Введите высоту: "))
    
    n4 = (n1*n2 + n1*n3 + n3*n2)*2
    print("Пл. поверхности --", n4)
except:
    print("Произошла ошибка!")
    


input()

print("Восклицательный знак в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Делить на ноль нельзя!")
    elif s == '!':
        break
    else:
        print("Неверный знак операции!")
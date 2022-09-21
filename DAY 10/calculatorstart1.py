from art import logo


print(logo)


print('JOASH CALCULATOR')
def add(x,y):
 return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
def modulus(x,y):
    return x%y


def inputMenu():
    print('0. Exit  1.Addition 2.Substraction\n'
          '3. Multiplication 4.Division 5.Modulus Operation ')
    option=int(input('Choose one of the following for calcuation: '))

    if option==1:
        num1=float(input('Enter First Number: '))
        num2=float(input('Enter Second Number: '))
        print(num1,'+',num2,'=',add(num1,num2))
        inputMenu()

    elif option==2:
        num1=float(input('Enter First Number: '))
        num2=float(input('Enter Second Number: '))
        print(num1, '-', num2, '=', substract(num1,num2))
        inputMenu()

    elif option==3:
        num1=float(input('Enter First Number: '))
        num2=float(input('Enter Second Number: '))
        print(num1, '*', num2,'=',multiply(num1,num2))
        inputMenu()

    elif option==4:
        num1=float(input('Enter First Number: '))
        num2=float(input('Enter Second Number: '))
        print(num1,'/',num2,'=',division(num1,num2))
        inputMenu()

    elif option==5:
        num1 = float(input('Enter your First number: '))
        num2 = float(input('Enter your Second number: '))
        print(num1,'%',num2,'=',modulus(num1,num2))
        inputMenu()

    else:
        exit()

inputMenu()
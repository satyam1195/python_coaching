#types of errors->1. logical error(bugs) 2. syntax error
#for solving logical error we use try except
#example1 : ZeroDivisionError
'''try:
    a=int(input("enter your age:"))
    b=0
    c=a/b
    print(c)

except ZeroDivisionError:
    print("can't be divided by zero")
    print("change number")'''



#example2: ValueError
'''try:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    #floor division gives only integer result
    #note put b=r which is a variable and it will give this error
    z=a//b
    print(z)
except ValueError:
    print("please enter numerical values")'''

#example3: list index out of range (IndexError)
'''try:
    a=[10,20,30,40]
    c=a[0]/a[20]
    print(c)
except IndexError:
    print('the value is out of range of the list')'''

#example4: try catch
'''
try:
    a=int(input('enter a:'))
    b=input('enter b:')
    c=a/b
except TypeError:
    print('please enter string value for b')
    try: 
        lst=['a','b','c']
        e=lst[0]/lst[1]
       
    except TypeError:
        print("Unable to perfome task")
        try:
             f=lst[0]/g 
             x=a/0
        except NameError:
            print('Also ')
        finally:
            print("Finished")
            '''
'''try:
    a=int(input('enter a:'))
    b=input('enter b:')
    c=a/b
    lst=[12,12,12]
    e=lst[0]/lst[1]
    f=lst[0]/g 
    x=a/0
except TypeError:
    print('Type error')

except NameError:
    print('3rd Type error')
finally:
    print("Finished")'''







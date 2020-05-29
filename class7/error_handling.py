a = 10
b = 0

#
#try:
 #   c = a / b
 #   print(c)
#except:
#    print("cant divide by 0 dumboo!!!")


#try:
 #   c = a / b
 #   print(c)
#except:
 #   print("cant divide by 0 dumboo!!!")
#else:
  #  print("no error")


try:
    c = a / b
    print(c)
except:
    print("cant divide by 0 dumboo!!!")
else:
    print("no error huda print hune part!!!")
finally:
    print("error vayeni navayeni print hune part !!")

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print('zero division')
except Exception as e:
    print(e)
    
print("out of it")



#try:
 #   c = a / b
 #   print(c)
#except ZeroDivisionError:
 #   raise ZeroDivisionError('Division by Zero ---------------------!!!!!!')

a = int(input("enter a number:  "))
b = int(input("enter a number:  "))
#if b == 0:
#    raise ZeroDivisionError('B is zero')
#else:
 #   c = a / b
 #   print(c)



assert b > 0, 'B is non positive'
c = a / b
print(c)
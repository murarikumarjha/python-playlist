from threading import *
import time
def calc_square(numbers):
    print('calculate square number: ')
    for n in numbers:
        time.sleep(0.2)
        print('square :',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers: ")
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)
arr = [2,3,4,5]

t = time.time()
t1 = Thread(target= calc_square, args=(arr,))
t2 = Thread(target= calc_cube, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah .... Ia am with all my work now!")
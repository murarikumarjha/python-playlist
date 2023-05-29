# from threading import Thread
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
calc_square(arr)
calc_cube(arr)

print("done in : ",time.time()-t)
print("Hah .... Ia am with all my work now!")
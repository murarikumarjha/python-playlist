import time
import multiprocessing
square_number = []
def calc_square(numbers):
    global square_number
    for n in numbers:
        print('square '+ str(n*n))
        square_number.append(n*n)
    print('within a process: result'+ str(square_number))

if __name__ == "__main__":
    arr = [2,3,4,5,6]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    
    p1.start()
    p1.join()
    print('outside  of  process: result'+ str(square_number))
    print("DOne")
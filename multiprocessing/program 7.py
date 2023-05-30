import  multiprocessing 
from multiprocessing import pool
import time
def f(n):
    sum = 0
    for x in range(100):
        sum += x*x
    return sum

if __name__ == '__main__':
    t1 = time.time()
    p = multiprocessing.Pool()
    result = p.map(f,range(1000))
    p.close()
    p.join()

    print("pool took",time.time()-t1)
    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(f(x))

    print('serial processing took ',time.time()-t2)
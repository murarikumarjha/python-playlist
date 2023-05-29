# value in multiprocessing
import multiprocessing, array

def calc_square(number,result,v):
    v.value = 5.67
    for idx, n in enumerate(number):
        result[idx] = n*n

if __name__ == '__main__':
    number = [2,3,4]
    result = multiprocessing.Array('i',3)
    v = multiprocessing.Value("d",0.0)
    p  = multiprocessing.Process(target=calc_square, args= (number,result, v))
    p.start()
    p.join()

    print(result[:])
    print(v.value)

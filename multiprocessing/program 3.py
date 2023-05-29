import multiprocessing, array

def calc_square(number,result):
    for idx, n in enumerate(number):
        result[idx] = n*n

if __name__ == '__main__':
    number = [2,3,4]
    result = multiprocessing.Array('i',3)
    p  = multiprocessing.Process(target=calc_square, args= (number,result))
    p.start()
    p.join()

    print(result[:])

from time import time, sleep
# import multiprocessing as mp
from multiprocessing import Process
import random as rn

def main(b):
    a1 = time()
    for i in range(1, b):
        file_name = 'fille{}.txt'.format(i)
        with open(file_name, 'tw', encoding='utf-8') as f:
            f.write(str(rn.randint(1, 200)) + "\n")
        sleep(1)
        print(f'Файл {file_name} обработан...')
    a2 = time()
    print(a2-a1)

if __name__ == '__main__':
    # lock = Lock()
    for num in range(1, 6):
        Process(target=main, args=(num, )).start()

main(6)
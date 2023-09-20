
from time import time, sleep
from threading import Thread


def main(b):
    a1 = time()
    for i in range(1, b):
        file_name = 'file{}.txt'.format(i)
        with open(file_name, 'tw', encoding='utf-8') as f:
            pass
        sleep(1)
        print(f'Файл {file_name} обработан...')
    a2 = time()
    print(a2-a1)

for i in range(1, 6):
    th = Thread(target=main, args=(i, ))
    th.start()

main(6)







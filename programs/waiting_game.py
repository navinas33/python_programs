import random
import time


def waiting_game():
    target = random.randint(2, 4)
    print(f'\nYour target time is {target}')

    input('  ...Press enter to begin...  ')
    start = time.perf_counter()

    input(f'\n... Press enter again after {target} seconds... ')
    elapsed = time.perf_counter() - start

    print(f'Elapsed time : {elapsed} seconds')
    if elapsed == target:
        print('(Unbelievable Perfect timing..)')
    elif elapsed < target:
        print(f'{target - elapsed} too fast')
    else:
        print(f'{target - elapsed} too slow')


def main():
    waiting_game()


if __name__ == '__main__':
    main()

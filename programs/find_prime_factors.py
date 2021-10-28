def find_prime_factor(value):
    prime_numbers = list()
    divisor = 2
    while(divisor <= value):
        if value % divisor == 0:
            prime_numbers.append(divisor)
            value = value / divisor
        else:
            divisor += 1
    return prime_numbers

def main():
    print(find_prime_factor(60))
    print(find_prime_factor(13))

if __name__ == '__main__':
    main()
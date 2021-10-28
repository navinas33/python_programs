import pickle


def save(items, outfile):
    with open(outfile, 'wb') as file:
        pickle.dump(items, file)


def load(input_file):
    with open(input_file, 'rb') as file:
        return pickle.load(file)


def main():
    save({'name': 'navin', 'age': 25}, 'dict.pickle')
    print(load('dict.pickle'))


if __name__ == '__main__':
    main()

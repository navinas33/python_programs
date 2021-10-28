def sort_words(value):
    temp_list = sorted([word.lower() + word for word in value.split(' ')])
    return ' '.join([word[len(word) // 2:] for word in temp_list])


def main():
    print(sort_words('This is dummy text'))
    print(sort_words('string of words'))
    print(sort_words('string words of words'))
    print(sort_words('banana ORANGE apple'))


if __name__ == '__main__':
    main()

def add(a, b):
    """
    Function to add 2 numbers.
    :param a: First number.
    :param b: Second number.
    :return: Sum of 2 numbers.
    """
    return a + b

def greet(name):
    """
    Function to greet someone.
    :param name: Person's name.
    """
    print(f'Hello {name}')

def main():
    word = 'cat'
    print(word.upper())

    num = add(3, 4)
    print(f'Answer = {num}')

    name = 'Jane'
    greet(name)

    print('----------')
    print(help(add))
    print(greet.__doc__)

if __name__ == '__main__':
    main()

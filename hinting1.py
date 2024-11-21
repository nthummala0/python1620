# Version 1:
# Setting type hinting to variables in a function.
def main():
    a: int = 10
    b: int = 20
    c = a + b
    print(f'Answer = {c}')  # Answer = 30

    a = 10.0
    b = 20.0
    c = a + b
    print(f'Answer = {c}')  # Answer = 30.0

    a = '10'
    b = '20'
    c = a + b
    print(f'Answer = {c}')  # Answer = 1020

if __name__ == '__main__':
    main()

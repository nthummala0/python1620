# Version 2:
# Only setting type hinting in function headers
def add(x: float, y: float) -> float:
    return x + y

def main():
    a = 10
    b = 20
    c = add(a, b)
    print(f'Answer = {c}')  # Answer = 30

    a = 10.0
    b = 20.0
    c = add(a, b)
    print(f'Answer = {c}')  # Answer = 30.0

    a = '10'
    b = '20'
    c = add(a, b)
    print(f'Answer = {c}')  # Answer = 1020

if __name__ == '__main__':
    main()

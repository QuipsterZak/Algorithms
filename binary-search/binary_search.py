def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            print("index of guess is: ", mid)
            return
        elif guess > item:
            high = mid -1
        else:
            low = mid + 1

def generate_numbers(limits):
    return list(range(limits + 1))

def generate_ascii():
    return [chr(code) for code in range(128)]

lst = generate_numbers(500)
ch = generate_ascii()

binary_search(lst, 25)
binary_search(ch, 'z')

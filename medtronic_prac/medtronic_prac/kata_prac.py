def add(a,b):
    return a + b


def even_or_odd(num):
    if not isinstance(num, int):
        raise TypeError("Argument must be an integer")
    return "Odd" if num % 2 == 1 else "Even"

def vowel_count(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([l for l in word if l in vowels ])

    # filter string in list comprehension
    # get length of list
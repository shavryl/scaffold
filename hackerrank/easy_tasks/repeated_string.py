

def count_letters(s:str, n:int) -> int:
    letters = s.count('a')
    if letters == 0:
        return letters

    leftovers = n % len(s)
    result = letters * int(n / len(s)) + s[:leftovers].count('a')

    return result

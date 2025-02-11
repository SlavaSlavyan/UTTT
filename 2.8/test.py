def is_valid_roman(roman):
    # Проверка на наличие недопустимых символов
    valid_characters = "IVXLCDM"
    for char in roman:
        if char not in valid_characters:
            return False

    # Проверка на корректность последовательности римских цифр
    count = 0
    prev_char = ''
    
    for i in range(len(roman)):
        char = roman[i]
        
        # Проверка на количество повторений
        if char == prev_char:
            count += 1
            if (char in 'VLD' and count > 1) or (char in 'IUX' and count > 3):
                return False
        else:
            count = 1
            prev_char = char
        
        # Проверка на допустимые комбинации
        if i > 0:
            if (roman[i-1] == 'I' and char in 'VX') or \
               (roman[i-1] == 'X' and char in 'LC') or \
               (roman[i-1] == 'C' and char in 'DM'):
                continue
            elif (roman[i-1] in 'VLD' and char == roman[i-1]):
                return False

    return True

def roman_to_arabic(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    arabic = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_numerals[char]
        
        if value < prev_value:
            arabic -= value
        else:
            arabic += value
        
        prev_value = value
    
    return arabic

# Пример использования
roman_number = input("Введите римское число: ")

if is_valid_roman(roman_number):
    arabic_number = roman_to_arabic(roman_number)
    print(f"Арабское число: {arabic_number}")
else:
    print("Ошибка: введено некорректное римское число.")
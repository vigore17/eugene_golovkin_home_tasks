translator_dict = {'one': 'один',
                   'two': 'два',
                   'three': 'три',
                   'four': 'четыре',
                   'five': 'пять',
                   'six': 'шесть',
                   'seven': 'семь',
                   'eight': 'восемь',
                   'nine': 'девять',
                   'ten': 'десять'}

def num_translate(number):
    for key in translator_dict.keys():
        if key == number:
            return translator_dict.get(key)

print(num_translate('one'))
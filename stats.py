def sort_on(items):
    return items["num"]

def count_words(text):
    words = text.split()
    return len(words)

def num_chars(text):
    char_dict = {}
    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_dict(dict):
    sorted_items = []
    for key in dict:
        sorted_items.append({'char': key, 'num': dict[key]})
    return sorted(sorted_items, reverse=True, key=sort_on)

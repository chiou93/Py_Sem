# 3.1

def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_dict:
            names_dict[letter] = [i]
        names_dict[letter] += [i]
            
            
    return names_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))

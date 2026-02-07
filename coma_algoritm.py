def coma_converter(value_1):
    value = int(value_1)
    value_len = len(str(value))
    value_mod = value_len % 3
    print(value_mod)

    new_number = ""
    if value_mod == 1 or value_mod == 2:
        count = 0
        for n in list(str(value)):
            count += 1
            if value_mod == count:
                number_1 = str(value)[:value_mod]
                print(number_1)
                number_2 = number_1 + ","
                new_number += number_2
                print(new_number)
    other_number = str(value)[value_mod:]
    print(other_number)
    count_ = 0
    start = 0
    for n in other_number:
        count_ += 1
        if count_ % 3 == 0:
            number_1 = str(other_number)[start:count_]
            new_number += number_1 + ","
            print(new_number)
            start += 3
    result = new_number[:-1]
    return result
print(coma_converter(input("type a number :")))





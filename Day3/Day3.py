import pandas as pd

def letter_to_number(letter):
    if letter.islower():
        number = ord(letter) - ord('a') + 1
    else:
        number = ord(letter) - ord('A') + 27
    return number

def get_intersection(string):
    compa_string = string[:len(string)//2]
    compb_string = string[len(string)//2:]
    comp_intersection = set.intersection(
        set(compa_string),
        set(compb_string))
    intersection_numbers = [letter_to_number(letter) for letter in comp_intersection]
    return sum(intersection_numbers)

comp_df1 = pd.read_csv('input.txt', header=None, names=['input_string'])
comp_df1['priority_sum'] = comp_df1.input_string.apply(get_intersection)

total_priority1 = comp_df1.priority_sum.sum().item()
print(f"q1 priority sum: {total_priority1}")

def string_intersection(string_list):
    string_sets = [set(string) for string in string_list]
    set_intersection = set.intersection(*string_sets)
    return set_intersection.pop()

comp_df1['elf_group'] = comp_df1.index//3
elf_grouped2 = comp_df1.groupby('elf_group').agg(common_item=('input_string', string_intersection))
elf_grouped2['priority'] = elf_grouped2.common_item.apply(letter_to_number)

total_grouped_priority2 = elf_grouped2.priority.sum().item()
print(f"q2 grouped priority sum: {total_grouped_priority2}")

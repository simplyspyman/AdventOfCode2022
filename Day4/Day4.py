# import
import pandas as pd
#

assignment_df = pd.read_csv('input.txt', header=None, delimiter='-|,',
                            names=['elf1_min', 'elf1_max', 'elf2_min', 'elf2_max'])

def check_redundant_range(df):
    elf1_range = set(range(df.elf1_min, df.elf1_max+1))
    elf2_range = set(range(df.elf2_min, df.elf2_max+1))
    if elf1_range.issubset(elf2_range):
        redundant_flag = 1
    elif elf2_range.issubset(elf1_range):
        redundant_flag = 1
    else:
        redundant_flag = 0
    return redundant_flag

def check_overlapping_ranges(df):
    elf1_range = set(range(df.elf1_min, df.elf1_max + 1))
    elf2_range = set(range(df.elf2_min, df.elf2_max + 1))
    overlap_range = set.intersection(elf1_range, elf2_range)
    if len(overlap_range)>0:
        overlap_flag=1
    else:
        overlap_flag=0
    return overlap_flag

assignment_df['redundant_flag'] = assignment_df.apply(check_redundant_range, axis=1)
assignment_df['overlap_flag'] = assignment_df.apply(check_overlapping_ranges, axis=1)

redundant_count = assignment_df.redundant_flag.sum()
overlap_count = assignment_df.overlap_flag.sum()

print(f"there are {redundant_count} pairs of elves with a redundant elf")
print(f"there are {overlap_count} pairs of elves with overlapping ranges")



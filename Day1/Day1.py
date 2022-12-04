# imports
import pandas as pd
import numpy as np

#
def caloric_frame(input_string):
    df = pd.DataFrame({'calorie_amount': input_string.strip().split('\n')})
    df['elf_id'] = np.where(df.calorie_amount=='', 1, 0).cumsum()
    df = df[df.calorie_amount!='']
    df['calorie_amount'] = pd.to_numeric(df.calorie_amount).fillna(0).astype(int)
    return df

def elf_frame(caloric_frame):
    df = caloric_frame.groupby('elf_id')[['calorie_amount']].sum()
    df.sort_values('calorie_amount', ascending=False, inplace=True)
    return df


with open('input.txt', 'r') as f:
    input_string = f.read()
    df_cal = caloric_frame(input_string)
    df_elf = elf_frame(df_cal)
    maximum_cals = df_elf.iloc[0].item()
    print(f"elf {df_elf.iloc[0].index.name} is carrying the most: {maximum_cals}")

    top3_cals = df_elf.iloc[:3].sum().item()
    print(f"elves {df_elf.iloc[:3].index.values} are carrying the most: {top3_cals} in total")
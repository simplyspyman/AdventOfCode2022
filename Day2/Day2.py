# imports
import pandas as pd
# import numpy as np

#
def construct_play1(input_file):
    df = pd.read_csv(input_file, sep=' ', header=None, names=['opp_play', 'me_play'])
    df.index.name = 'round_id'
    df['opp_play_int'] = df.opp_play.map(dict(A=0, B=1, C=2))
    df['me_play_int'] = df.me_play.map(dict(X=0, Y=1, Z=2))
    df['result_int'] = (df.me_play_int - df.opp_play_int) % 3
    df['result'] = df.result_int.map({0:'draw', 1:'win', 2:'lose'})
    df['result_score'] = ((df.result_int+1)%3)*3
    df['play_score'] = df.me_play_int+1
    df['round_score'] = df.result_score + df.play_score
    return df

df_rounds1 = construct_play1('input.txt')
total_score1 = df_rounds1.round_score.sum()
print(f"part1 total score: {total_score1.item()}")

def construct_play2(input_file):
    df = pd.read_csv(input_file, sep=' ', header=None, names=['opp_play', 'result_target'])
    df.index.name = 'round_id'
    df['opp_play_int'] = df.opp_play.map(dict(A=0, B=1, C=2))
    df['result_int'] = df.result_target.map(dict(X=2, Y=0, Z=1))
    df['result'] = df.result_int.map({0:'draw', 1:'win', 2:'lose'})
    df['me_play_int'] = (df.result_int + df.opp_play_int) % 3
    df['result_score'] = ((df.result_int+1)%3)*3
    df['play_score'] = df.me_play_int+1
    df['round_score'] = df.result_score + df.play_score
    return df

df_rounds2 = construct_play2('input.txt')
total_score2 = df_rounds2.round_score.sum()
print(f"part2 total score: {total_score2.item()}")

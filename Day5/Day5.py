# import
import copy
#
with open('input.txt', 'r') as f:
    full_input_string = f.read()
    setup_string, instructions = full_input_string.split('\n\n')

def set_up_stacks(setup_string):
    setup_list = setup_string.split('\n')[::-1]
    stack_number_string = setup_list.pop(0)
    number_of_stacks = max([int(i) for i in stack_number_string.split() if i.isdigit()])
    stacks = [[] for n in range(number_of_stacks)]
    for row in setup_list:
        for col in range(number_of_stacks):
            crate = row[col*4+1]
            if crate.isalpha():
                stacks[col].append(crate)
    return stacks

def apply_instruction9000(instruction_string, stacks):
    instruction_ints = [int(i) for i in instruction_string.split() if i.isdigit()]
    move_n = instruction_ints[0]
    move_from = instruction_ints[1]-1
    move_to = instruction_ints[2]-1
    for i in range(move_n):
        item = stacks[move_from].pop()
        stacks[move_to].append(item)

stacks_init = set_up_stacks(setup_string)
stacks_9000 = copy.deepcopy(stacks_init)
for instruction_string in instructions.strip().split('\n'):
    apply_instruction9000(instruction_string, stacks_9000)
top_crates9000 = ''.join([stack[-1] for stack in stacks_9000])
print(f"the crates at the top for CrateMover9000 are {top_crates9000}")


def apply_instruction9001(instruction_string, stacks):
    stacks_in = stacks.copy()
    crates_in = sum([len(stack) for stack in stacks_in])
    instruction_ints = [int(i) for i in instruction_string.split() if i.isdigit()]
    move_n = instruction_ints[0]
    move_from = instruction_ints[1] - 1
    move_to = instruction_ints[2] - 1
    crates = stacks[move_from][-move_n:]
    stacks[move_from] = stacks[move_from][:-move_n]
    stacks[move_to].extend(crates)
    crates_out = sum([len(stack) for stack in stacks])
    if crates_out!=crates_in:
        stacks = stacks_in.copy()
        raise Exception('CrateCountError: {crates_in} in but {crates_out} out')

stacks_9001 = copy.deepcopy(stacks_init)
for instruction_string in instructions.strip().split('\n'):
    apply_instruction9001(instruction_string, stacks_9001)
top_crates9001 = ''.join([stack[-1] for stack in stacks_9001])
print(f"the crates at the top for CrateMover9001 are {top_crates9001}")
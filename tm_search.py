from turing_machine import TuringMachine
import random
import math

def run_turing(tf, init, final):
    initial_state = init,
    accepting_states = final,
    transition_function = tf
    final_states = {"final"}

    t = TuringMachine("010011 ",
                      initial_state=init,
                      final_states=final,
                      transition_function=tf)

    print("Input on Tape:\n" + t.get_tape())

    while not t.final():
        t.step()

    return t.get_tape()


def create_all_tf(size):
    bin_num = 2 ** (4*(size - 1))
    state_num = size ** (2 * (size - 1))
    num = bin_num * state_num
    seed = random.randint(0, num)
    bin_seed = str(format(bin(seed % bin_num), 4*(size-1)))
    state_seed = seed % state_num
    states = range(size)
    print(num, bin_num, state_num)
    print(seed, bin_seed, state_seed)
    tf = {}
    for i in states[1:]:
        tf[(str(i), "0")] = (str((state_seed % (size ** (2 * i-1))) % size), bin_seed[4*i-4], "R" if bin_seed[4*i-3] == 1 else "L")
        tf[(str(i), "1")] = (str((state_seed % (size ** (2 * i))) % size), bin_seed[4*i-2], "R" if bin_seed[4*i-1] == 1 else "L")
    print(tf)


print(create_all_tf(2))



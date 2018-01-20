# Filename: match.py
# Author: Wei Zhong

import sys

inputs = sys.stdin.read().splitlines()
n = int(inputs.pop(0))
inputs = [[int(char) for char in string.split()] for string in inputs]

professor_pref = inputs[:n]
professor_indx = [-1] * n
student_pref = inputs[n:]
student_indx = [-1] * n

def inv_index(pref):
    index_arr = [0] * len(pref)
    for idx, val in enumerate(pref):
        index_arr[val] = idx
    return index_arr

professor_queue = list(reversed(range(n)))
student_inv_index = [inv_index(ele_arr) for ele_arr in student_pref]

def pretty_tab(prefs, idxs, highlight):
    for i, row in enumerate(prefs):
        for j, col in enumerate(row):
            grn = '\033[0;42m'
            red = '\033[1;31m'
            rst = '\033[0;0m'
            fmt = '{0:4d}'
            if (i , j) == highlight:
                fmt = '{0:3d}'
                print grn,
            if j == idxs[i]:
                fmt = red + fmt
                print fmt.format(col),
            else:
                print fmt.format(col),
            print rst,
        print('')

def debug_print(p, s):
    print(professor_queue, (p, s))
    print('Professor preference')
    pretty_tab(professor_pref, professor_indx, (p, professor_indx[p] + 1))
    print('Student preference')
    pretty_tab(student_pref, student_indx, (s, student_inv_index[s][p]))
    print('')

while len(professor_queue):
    p = professor_queue.pop()
    professor_indx[p] += 1
    s = professor_pref[p][professor_indx[p]]
    if student_indx[s] < 0:
        student_indx[s] = student_inv_index[s][p]
    else:
        t = student_pref[s][student_indx[s]]
        if student_inv_index[s][p] < student_inv_index[s][t]:
            student_indx[s] = student_inv_index[s][p]
            professor_queue.append(t);
        else:
            professor_queue.append(p);
    # debug
    if len(professor_queue):
        p = professor_queue[-1]
        s = professor_pref[p][professor_indx[p] + 1]
    debug_print(p, s)

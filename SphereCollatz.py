#!/usr/bin/env python3

# ---------------------------
# projects/collatz/SphereCollatz.py
# Copyright (C) 2016
# Paul Bass
# ---------------------------


# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)


def cycle_length (num) :
    assert num > 0
    cycle = 1
    while num > 1 :
        if (num % 2) == 0 :
            num = (num // 2)
        else :
            num = (3 * num) + 1
        cycle += 1
    assert cycle > 0
    return cycle


# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    low = i
    high = j

    # Check that i and j are with in the range 0-1000000
    assert i > 0 and i < 1000000
    assert j > 0 and j < 1000000

    # look for low bound and the high bound
    if(i > j):
        low = j
        high = i

    maxC = 1
    test = 1
    for cur in range (low, high + 1):
        test = cycle_length(cur)
        if (test > maxC):
            maxC = test
    assert maxC > 0
    return maxC

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the maxCC cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        if (s.strip()):
            i, j = collatz_read(s)
            v    = collatz_eval(i, j)
            collatz_print(w, i, j, v)

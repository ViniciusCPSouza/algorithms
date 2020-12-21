def insertion(seq, reverse=False):
    if len(seq) <= 1:
        return

    should_switch = lambda key, i: key > seq[i] if reverse else key < seq[i]

    for j in range(1, len(seq)):
        key = seq[j]
        i = j - 1

        while i >= 0 and should_switch(key, i):
            seq[i + 1] = seq[i]
            i -= 1

        seq[i + 1] = key


if __name__ == '__main__':
    seq = [31, 41, 59, 26, 41, 58]

    insertion(seq)

    assert seq == [26, 31, 41, 41, 58, 59]

    seq = [1, 2, 3, 3, 4, 5, 6]

    insertion(seq, reverse=True)

    assert seq == [6, 5, 4, 3, 3, 2, 1]

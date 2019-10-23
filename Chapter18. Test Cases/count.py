def update_counts(letters, counts_dict):
    for c in letters:
        counts_dict[c] = 1
        if c in counts_dict:
            counts_dict[c] = counts_dict[c] + 1

import test

counts_dict = {'a': 3, 'b': 2}
update_counts("aaab", counts_dict)
# 3 more occurrences of a, so 6 in all
test.testEqual(counts_dict['a'], 6)
# 1 more occurrence of b, so 3 in all
test.testEqual(counts_dict['b'], 3)

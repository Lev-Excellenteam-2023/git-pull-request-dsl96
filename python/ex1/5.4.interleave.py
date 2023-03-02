# week 5 כלים שלובים
import numpy as np
def interleave(*iterables):
    return list(np.array(list(zip(*iterables))).flatten())


a =interleave('abc', [1, 2, 3], ('!', '@', '#'))
print(a)


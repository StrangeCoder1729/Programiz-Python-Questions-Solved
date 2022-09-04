# Q34] Python Program to Compute all the Permutation of the String

import itertools  

words = [''.join(p) for p in itertools.permutations("yup")]
print(words)
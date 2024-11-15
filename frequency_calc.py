# First 5 lines from sample_X_merged.bed.gz
chr1	10000	10061	61	.	+
chr1	10000	10086	86	A00738:475:HCY7JDSX5:4:2669:7256:18568_AGGCCTGTTAAT	+
chr1	10000	10095	95	.	+
chr1	10000	10104	104	.	+
chr1	10000	10123	123	A00738:475:HCY7JDSX5:4:1656:30572:34209_TACGGGAAACCT	-

import sys

dictionary = {}
total = 0

for line in sys.stdin:
    item = line.split("\t")
    length = int(item[3])
    if length in dictionary:
        dictionary[length] += 1
    else:
        dictionary[length] = 1

    total += 1

sorted_lengths = sorted(dictionary.items())

with open('query_file.tsv', 'w') as f:
    f.write("Fragment_length\tCount\tNormalized_Frequency\n")
    for length, count in sorted_lengths:
        # Calculate the normalized frequency
        normalized_frequency = count / total
        f.write(f"{length}\t{count}\t{normalized_frequency:.6f}\n")

with open('total.txt', 'w') as f:
    f.write(str(total))


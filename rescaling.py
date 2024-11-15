import sys

length_count = {}

with open('output_with_sampling_lines.tsv', 'r') as f:
    next(f)
    
    for line in f:
        items = line.split('\t')
        length = int(items[0].split()[0])  
        sampling_lines = int(items[-1])
        
        length_count[length] = sampling_lines

for lines in sys.stdin:
    item = lines.split('\t')
    length = int(item[3])  # Assuming the fragment length is in the 4th column (index 3)
    
    if length in length_count:
        length_count[length] -= 1
        
        if length_count[length] > 0:
            print(lines.strip())



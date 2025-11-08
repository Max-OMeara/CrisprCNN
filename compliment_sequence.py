import csv

input_filename = "data/GenomeCRISPR_full05112017_brackets.csv"
output_filename = 'GenomeCRISPR_+_strands.csv'
strand_column_index = 3
sequence_column_index = 7

compliments = {"A":"T","T":"A","C":"G","G":"C","N":"N"}

def revcomp(s: str) -> str:
    return "".join(compliments[b] for b in reversed(s))

with open(input_filename, 'r', newline='') as infile, \
     open(output_filename, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        if row[strand_column_index] == "-":
            sequence = row[sequence_column_index]
            row[sequence_column_index] = revcomp(sequence)
            row[strand_column_index] = "+"
        writer.writerow(row)
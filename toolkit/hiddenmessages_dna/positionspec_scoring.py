## INDICATOR MATRIX ##  | ## COUNT MATRIX ##
# Position x Nucleotide | Nucleotide Counts/Column 
# EXAMPLE #             | EXAMPLE:
# Sequence: A C G T A   | Input: A C G T A  OUTPUT: (Number of Nucs per Column)
# Nucs:   A 1 0 0 0 1   |        T C C T A        A 3 0 0 2 3
# p=[0,1] C 0 1 0 0 0   |        A C G A A        C 0 5 1 0 0
#         G 0 0 1 0 0   |        A C G T G        G 0 0 4 0 2
#         T 0 0 0 1 0   |        T C G A G        T 2 0 0 3 0

## PSSM MATRIX WITH BIOPYTHON #
''''''
from Bio.Seq import Seq
from Bio import motifs
DNA_sequences = [Seq('ACGTA'),
               Seq('TCGTA'),
               Seq('ACGAA'),
               Seq('ACGTG'),
               Seq('TCGAG')]
motif = motifs.create(DNA_sequences)
#print(motif.counts)
#print(motif.degenerate_consensus)
pssm = motif.pssm
consensus = motif.consensus
k = len(motif.consensus)
DNA = Seq('ATGCGATCGGTGTACGTAACTGGGTATCGGACCATGCATGCATGCAGGCTAGGCTGAG')
for i, S in pssm.search(DNA):
    print(i, S, DNA[i:i+k])

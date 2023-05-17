from appx_pattern_matching import ApproximatePatternMatching
from Bio.Seq import Seq
from itertools import product


def approx(dna, k, d):
        '''
        This function approximates the validity of neighbors within d of a given substring of size k and its reverse complimement.
        Args: (str) dna - the DNA sequence, (int) k - length of substrings, (int) d - hamming distance
        Returns: (list) - most common kmer of length k within d mismatches of the original kmer and its reverse compliment 
        '''
        nucleotides = ['A', 'T', 'G', 'C']
        combined_nucs = [''.join(nucleotide) for nucleotide in product(nucleotides, repeat = k)]
        freq_kmers = {}
        for pattern in combined_nucs:
            reverse_kmers = Seq(str(pattern))
            rev_comp = str(reverse_kmers.reverse_complement())
            count = ApproximatePatternMatching.appxmatch(pattern, dna, d)
            count_revcomp = ApproximatePatternMatching.appxmatch(rev_comp, dna, d) 
            totalcount = count + count_revcomp
            if totalcount not in freq_kmers:
                freq_kmers[totalcount] = [pattern]
            else:
                freq_kmers[totalcount].append(pattern)
        #print (freq_kmers[max(freq_kmers)])            
        return freq_kmers[max(freq_kmers)]

test = approx(dna = 'ACGTTGCATGTCGCATGATGCATGAGAGCT', k = 5, d = 3)
from itertools import product
from appx_pattern_matching import ApproximatePatternMatching


class FrequentKmersMismatches():
    def __init__(self):
        #MODULAR
        pass
    def neighborhood(pattern):
        '''
        This function finds the neighborhood of a pattern in a string.
        Args: (str) pattern - the kmer 
        Returns (list) - list of immediate neighbors for the kmer
        '''
        neighborhood = [pattern]
        for i in range(len(pattern)):
            positional_nuc = pattern[i]
            for nucleotide in 'ATGC':
                if nucleotide != positional_nuc:
                    neighbor = pattern[:1] + nucleotide + pattern[i+1:]
                    neighborhood.append(neighbor)
        return neighborhood
    def approx(dna, k, d):
        '''
        This function approximates the validity of neighbors within d of a given substring of size k.
        Args: (str) dna - the DNA sequence, (int) k - length of substrings, (int) d - hamming distance
        Returns: (list) - most common kmer of length k within d mismatches of the original kmer
        '''
        nucleotides = ['A', 'T', 'G', 'C']
        combined_nucs = [''.join(nucleotide) for nucleotide in product(nucleotides, repeat = k)]
        freq_kmers = {}
        for pattern in combined_nucs:
            count = ApproximatePatternMatching.appxmatch(pattern, dna, d)
            if count not in freq_kmers:
                freq_kmers[count] = [pattern]
            else:
                freq_kmers[count].append(pattern)
        print (freq_kmers[max(freq_kmers)])            
        return freq_kmers[max(freq_kmers)]
    test = approx(dna = "GTGAGAGATTGTGGTGAGTCGTGGATTAGAGATTAGTAGTCGTGAGAGTGGATTCGTGAGACGTGAGAGATTCGTGCGTGCGTGAGAAGAGATTCGTGGATTGATTAGAGTGAGTGATTAGTGTGGATTAGTAGAGTGAGTCGTGGTGGTGGTGGATTGTGAGTCGTGGATTAGTAGTCGTGAGTAGAGATTAGTGTGAGTAGTAGAAGTAGTAGTCGTGAGACGTGAGACGTGCGTGAGAGTGAGAAGTAGTGTGAGTGTGGATTAGAGATTGTGAGTAGAAGTCGTGAGTCGTGAGAAGAGATTAGAAGAGTGAGTAGAAGTCGTGGTGAGTCGTGAGACGTGCGTGCGTGGATTAGTAGTAGA", k = 6, d = 3)
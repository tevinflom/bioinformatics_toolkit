from hamming_distance import HammingDistance as hd

class ApproximatePatternMatching(): 
    def __init__(self):
        #MODULAR
        pass
    def appxmatch(pattern, dna, d):
        '''
        This function iterates over all kmers in a DNA string that are are similar up to d mismatches. 
        Args: (str) pattern - kmer pattern to check for, (str) dna - DNA string, d(int) - maximum allowable mismatches
        Returns: (list) positions - starting position of k mers with up to d mismatches with reference kmer 
                (int) count - number of kmers in the DNA string that have at most d mismatches 
        
        '''
        positions = []
        k = len(pattern)
        for pos in range(len(dna) - k+1):
            kmer = dna[pos:pos+k]
            if kmer in dna:
                hamming_d = hd.hamming_2str(pattern, kmer)
                if hamming_d <= d:
                    new_pos = pos
                    positions.append(new_pos)
        count = len(positions)
        print(*positions, f'Count: {count}')
        return positions, count

    test = appxmatch(pattern = 'AAAAA', dna = 'AACAAGCTGATAAACATTTAAAGAG,', d = 2)
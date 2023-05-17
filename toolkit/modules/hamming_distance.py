class HammingDistance():
    def __init__ (self):
        #MODULAR
        pass
    def hamming_2str(seq1, seq2):
        '''
        This function finds the Hamming distance (number of differences) betweem two DNA strings of equal length.
        Args: (str) - seq1, (str) - seq2
        Returns: (int) - distance
        
        '''
        distance = 0
        for nuc in range(len(seq1)):
            if seq1[nuc] != seq2[nuc]:
                distance += 1
        #print(distance)
        return distance
    #test = hamming_2str(seq1 = "GGGCCGTTGGT", seq2 = "GGACCGTTGAC")
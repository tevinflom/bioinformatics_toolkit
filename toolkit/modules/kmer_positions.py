class CountKmers(): 
    def __init__(self): 
        ## MODULAR, use-case specific ##
        pass

    def pattern_positions(dna, pattern):
        ''' 
        This method gives every position of a given pattern in a DNA string.
        Args: (str) dna - DNA sequence, (str) pattern - kmer
        Returns: (str) positions - positions of the occurances in the DNA string
        '''
        positions = []
        start_pos = 0 
        while start_pos < len(dna): 
            pattern_pos = dna.find(pattern, start_pos) 
            if pattern_pos > -1: 
                start_pos = pattern_pos + 1
                new_pos = str(start_pos - 1)
                positions.append(new_pos)
                str_positions = ' '.join(str(new_pos) for new_pos in positions)
            else: 
                break 
        
        print(str_positions) 
        return(str_positions)
    
    test = pattern_positions("AAACATAGGATCAAC", "AA")



    
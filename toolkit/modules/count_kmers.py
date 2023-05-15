class CountKmers(): 
    def __init__(self): 
        ## MODULAR, use-case specific ##
        pass

    def pattern_count(dna, pattern):
        ''' 
        This method counts the number of discrete substrings in a string with overlap. 
        Args: (str) DNA sequence, (str) k-mer
        Returns: (int) count
        '''
        count = 0
        start_pos = 0 
        while start_pos < len(dna): 
            pattern_pos = dna.find(pattern, start_pos) 
            if pattern_pos > -1: 
                start_pos = pattern_pos + 1
                count += 1
            else: 
                break 
        print(count) 
        return(count)
    
    test = pattern_count("GACCATCAAAACTGATAAACTACTTAAAAATCAGT", "AAA")



    
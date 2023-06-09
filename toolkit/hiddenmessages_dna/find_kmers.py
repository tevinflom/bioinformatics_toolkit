import pandas as pd 

class FindKmers():
    def __init__(self):
        pass

    def frequent_words(dna, k):
        '''
        This function finds substrings of length k with overlapping.
        Args: (str) dna - DNA sequence, (int) k - constant length of substring 
        Returns: (series) count - pandas series frequency table containing substrings and occurances of each substring in the DNA
        '''
        substrings = [] 
        for pos in range(len(dna) - k + 1):
            kmer = dna[pos:pos+k]
            substrings.append(kmer)
            #count = pd.Series(substrings).value_counts()
        #print("Kmer | Count")
        #print(count)
        #print("----------")
        #print(f"Kmers: {substrings}")
        #return count
        return substrings

    #test = frequent_words(dna = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT", k = 3)
    
        

import pandas as pd 

class FindKmers():
    def __init__(self):
        pass

    def frequent_words(dna, k):
        substrings = [] 
        for pos in range(len(dna) - k + 1):
            kmer = dna[pos:pos+k]
            substrings.append(kmer)
            count = pd.Series(substrings).value_counts()
        print("Kmer | Count")
        print(count)
        return count

    test = frequent_words(dna = "ACTACGACTACTTGC", k = 3)
    
        

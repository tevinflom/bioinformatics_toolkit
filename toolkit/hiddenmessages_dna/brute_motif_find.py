
"""
THIS SCRIPT IS FROM : 

Created on Tue Apr 10 17:56:59 2018

@author: jennifermichaud
https://github.com/jmmichaud/BioinfoTools/blob/master/BruteMotifEnumeration.py

"""


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

def Neighbors(pattern, d):
    """Inputs a pattern as a text string and a number of allowed mismatches, d. 
    Outputs all permutations of the pattern than have no more than d mismatches 
    of original pattern as a list of strings.
    """
    if d == 0:
        return pattern
    elif len(pattern)== 1:
        return ['A', 'C', 'G', 'T']
    code = ['A', 'C', 'G', 'T']
    neighborhood = []
    suffixneighbors = Neighbors(pattern[1:], d)
    for suff in suffixneighbors: #for each suffix in suffix neighbors adds base if hamming distance is less  or equal to allowed mismatches
        if hamming_2str(pattern[1:], suff) < d: #If suffix neighbor and suffix of pattern have hamming distance less than mismatches, replaces first base of pattern with each base and adds to  list.
            for base in code:
                neighborhood.append(base + suff)
        else: #If suffix neighbor and suffix of pattern have hamming distance more than d, appends each suffix neighbor to first base of pattern.
            neighborhood.append(pattern[0] + suff)

    return neighborhood



def BruteMotifEnumeration(dna, k, d):
    """Inputs a list of DNA fragments as a list of strings (dna), a kmer 
    length (k), and an allowed number of mismatches. (d). Outputs a list of 
    highest occuring motif or motifs of length k found between the dna fragments
    with at most d mismatches for each occurence.
    This brute force algorithm is thorough but computationally expensive. It is 
    only practical for short DNA lengths with low amounts of mismatches.
    """
    patterns = []
    biglist = []
    for x in range(len(dna)): #finds all neighbors of length k with max d mismatches for each dna fragment
        for i in range(len(dna[x])-k+1):
            kmer = dna[x][i:i+k]
            neighbors = Neighbors(kmer, d)
            patterns.extend(neighbors)
        biglist.append(set(patterns))
        patterns = []
    common_patterns = biglist[0]
    for j in range(1, len(dna)): #uses list of neighbors from first dna fragment and uses it to compare to each dna fragment neighbor list. Common neighbors between lists are retained.
        common_patterns.intersection_update(biglist[j])
    return list(common_patterns)



## TEST DATA
    
dtxt_in = """CGGCAATCCGATGGCCGTTATAGGC 
TAGCCTGTGTTTATGCGGCAGTCAA 
TTTTGTTCATACCCAAAGACCTGAT 
TTGCATAGCTTTGTGGATCACAGAC 
ATTTCACTCATTGCGGCATTAAGAC 
CCAGAAGTCCGGCGCGGCGGCAGCC"""
dna_in= [y for y in (x.strip() for x in dtxt_in.splitlines()) if y]
k_in = 5
d_in = 2
##Corr_out = AAGTG GAAGC GTAAA TAAGC GTGAA CAAGC GGTAA AAAGC AGTAA
#
print(" ".join(BruteMotifEnumeration(dna_in, k_in, d_in)))

            
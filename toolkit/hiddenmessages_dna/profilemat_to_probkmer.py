def get_probabilities(kmer, profile_matrix):
    '''
    This fcn finds the probability of a nucleotide being in any given position based on a profile matrix
    Args: (str) - kmer, (dict) - profile matrix in the form at the bottom of this file 
    Returns: (float) - probability of nucleotide at any given position 
    
    '''
    probability = 1 
    for i in range(0, len(kmer)):
        if kmer[i] == 'A':
            probability = probability * profile_matrix['A'][i]
        if kmer[i] == 'T':
            probability = probability * profile_matrix['T'][i]
        if kmer[i] == 'G':
            probability = probability * profile_matrix['G'][i]
        if kmer[i] == 'C':
            probability = probability * profile_matrix['C'][i]
    return probability 

def get_profile(dna, k, profile_matrix):
    '''
    This fcn gives the most probable consensus kmer from the set based on probabilities 
    Args: (str) - DNA sequence, (int) - k length of subsequences, (dict) - profile matrix of the form at the bottom of this file
    Returns: (str) most probable consensus sequence 
    '''
    max_prob = 0 
    for i in range(len(dna)-k+1):
        kmer = dna[i:i+k]
        probability = get_probabilities(kmer, profile_matrix)
        if probability > max_prob:
            max_prob = probability 
            most_prob_kmer = kmer 
    #print(most_prob_kmer)
    return most_prob_kmer

# test = get_profile(dna = 'CACGAATACGGCGACATCATTTATAATTTAACCTTCCACCTACCGAACCACGAACGACCATTTAATGCTACGCAGTAACAGTATTACTTGGGTTTATCAGAAACTGGCCGGTTTGTATCCCGCTTCCTCCCAAAAGAATGGTGATAGAACACGAATCTGTTACCTACGTACTATATGTTCGCACTGATAAGCTTAGTACTCCGCTGGAAACATCAGTTTCGGCGCATATTCAACGAGTTCCCCGACGATGGACTTCTCACCAAGTCCGGAAGCCACTTTTTAGGTGCCCCAGGCTTGTCCACGTCCTCGGCCGGCACGTCGTCGTTCGAGCCATGATGTATAATGTAGAGGACGTGCGGCTTTTCCGTCCCGTGCCTGATAATAACCGCTGCCCTACAATCGGACGAATACTCTGGTTTTGTATGAGTTAAGTCCGCTATTCTGCCATAAATTGACTCGTGTTTATCGGATCTGCATAACGAGGAATTAGTGTTCCCCAGAGACATGCTCGGACCCTTGCGTAGAGGCCGAGAACGCATCTATAACTTCACTAGTCGCCAATCTTGGAAGTGACAGTAAATTGGCTATTATGTACAAACTATTTAATCGGTACAAGGCTACGTCTTATGACCATTCAGTTGTTAAGAAGAATGCTATAATCCAACTGTATCAGAGCACCTTTTGTTGCCGTAACAGAATGGTTAGTAGTAGGGGTAAGCAGCCGGGTCTGTAAGAGTATGGTATGTGTTGTACTAGACTGCGCGGCAAGGACTCAGAGTAGTGCCTAACCGAGCGGAGGTAGGCGTGATACAGACTTCCCGTTTGCCAGCCCACTATGCGACTGCCGCATGTGTCTGCCCCGTACTTGCTCCGTCATTGGTACTGATACACACAACTTTCACATGGACGGTCTAGCCATTAGCCCTCAGGAGCTTTCAAATTTTGCGGCCCGGTAGACATCCACCGGCTTTTTGATGTGTCGTAGCTGCATATGGTCGTT' , k = 15 , profile_matrix = 
# {
# 'A':[0.258, 0.167, 0.258, 0.227, 0.212, 0.333, 0.273, 0.182, 0.197, 0.318, 0.212, 0.227, 0.227, 0.258, 0.227],
# 'C':[0.182, 0.333, 0.258, 0.182, 0.227, 0.258, 0.167, 0.242, 0.182, 0.197, 0.242, 0.273, 0.303, 0.242, 0.258],
# 'G':[0.242, 0.318, 0.227, 0.273, 0.333, 0.212, 0.303, 0.227, 0.348, 0.258, 0.212, 0.182, 0.273, 0.242, 0.242],
# 'T':[0.318, 0.182, 0.258, 0.318, 0.227, 0.197, 0.258, 0.348, 0.273, 0.227, 0.333, 0.318, 0.197, 0.258, 0.273]} )

## MATRIX TEMPLATE EXAMPLE ##
# {
# 'A':[0.2, 0.2, 0.3, 0.2, 0.3],
# 'C':[0.4, 0.3, 0.1, 0.5, 0.1],
# 'G':[0.3, 0.3, 0.5, 0.2, 0.4],
# 'T':[0.1, 0.2, 0.1, 0.1, 0.2]} 
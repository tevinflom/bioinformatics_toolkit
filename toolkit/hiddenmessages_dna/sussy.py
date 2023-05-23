import random 

def hamming(seq1, seq2):
    distance = 0
    for nuc in range(len(seq1)):
        if seq1[nuc] != seq2[nuc]:
            distance += 1
    return distance

def profile_matrix(dna):
    seq_num = float(len(dna))
    nucs = ['A', 'C', 'G', 'T']
    profile_matrix = []
    for i in range(len(dna[0])):
        base_indeces = [seq[i] for seq in dna]
        profile_values = [float(base_indeces.count(nuc))/seq_num for nuc in nucs]
        profile_matrix.append(profile_values)
    return [list(i) for i in zip(*profile_matrix)]
#sanitycheck = print(profile_matrix(dna = "AAAATTTTTGGGGCCCCACTAGACTGGTTAGGAGCGCGTATGC"))
def get_profile_dict(prof_matrix, pos):
    profile_dict = {'A': prof_matrix[0][pos], 'C': prof_matrix[1][pos], 'G': prof_matrix[2][pos], 'T': prof_matrix[3][pos]}
    return profile_dict

def find_probable_kmer(seq, k, prof_matrix):
    max_prob = 0 
    prob_list = [] 
    for subset_pos in range(len(seq) - k+1):
        kmer_prob = 1 
        substring = seq[subset_pos:subset_pos+k]
        for pos in range(len(substring)):
            profile = get_profile_dict(prof_matrix, pos)
            kmer_prob = profile[substring[pos]]
        prob_list.append(kmer_prob)
    subset_pos = prob_list.index(max(prob_list))
    max_prob_kmer = seq[subset_pos:subset_pos + k]
    return max_prob_kmer
sanitycheck = print(find_probable_kmer(seq = 'AAGGCCTATGATGATGATGATGATAGGTAGACGATCGATATAGCGATCGGGATCGGATCGGATCGGATCGAGATTAGGCTAGGCTAAAGTCTCCTAGTAAAGAGACTAGTAGATGATGATGATGATGCTGCGCGCGCGCGTGCTGCTGAGCAACGATTAGGCCG', k = 3, prof_matrix = profile_matrix('AAGGCCTATGATGATGATGATGATAGGTAGACGATCGATATAGCGATCGGGATCGGATCGGATCGGATCGAGATTAGGCTAGGCTAAAGTCTCCTAGTAAAGAGACTAGTAGATGATGATGATGATGCTGCGCGCGCGCGTGCTGCTGAGCAACGATTAGGCCG')))
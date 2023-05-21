'''
I developed this script from the logic in the following tutorial:
https://www.youtube.com/watch?v=UIM2-fF3ssM

'''

def dna_matrix(dna, rowlength):
    dna_matrix = []
    for i in range(0, int(len(dna)/rowlength)):
        step = i + 1
        row = dna[i*rowlength:step*rowlength]
        dna_matrix.append(row)
    return dna_matrix
#sanitycheck = dna_matrix(dna = 'AGTCCTAGCCTTAAGGCT', rowlength = 3)
#print(sanitycheck)
def count_matrix(dna_matrix):
    dna_matrix = [[dna_matrix[j][i] for j in range(len(dna_matrix))] for i in range(len(dna_matrix[0]))]
    count_a = 1 #laplace counting method
    count_c = 1
    count_g = 1
    count_t = 1
    count_list = []
    for row in dna_matrix: 
        for nuc in row:
            if nuc == 'A':
                count_a += 1
            if nuc == 'C':
                count_c += 1
            if nuc == 'G':
                count_g += 1
            if nuc == 'T':
                count_t += 1
        count_list.append(str(count_a)+str(count_c)+str(count_g)+str(count_t))
        count_a = 1 #bring the laplace back 
        count_c = 1
        count_g = 1
        count_t = 1
    count_matrix = [[count_list[j][i] for j in range(len(count_list))] for i in range(len(count_list[0]))]
    return count_matrix
# a = ["ACGTA", "AGCTA","CGTAC"]
# sanitycheck = count_matrix(a)
# print(sanity_check)
def profile_matrix(count_matrix):
    list = []
    total_count = 0 
    for i in range(len(count_matrix)):
        list.append(count_matrix[i][0])
    for i in range(0, len(list)):
        list[i] = int(list[i])
    for num in range(0, len(list)):
        total_count = total_count + list[num]
    profile_matrix = [[int(x)/total_count for x in first] for first in count_matrix]
    #print(profile_matrix)
    return profile_matrix
# a = ["ACGTA", "AGCTA","CGTAC"]
# sanitycheck = profile_matrix(count_matrix(a))
def kmer_profile_val(kmer, profile):
    multiplier = 1
    count = 0 
    for i in kmer:
        global nuc
        if i == 'A':
            nuc = profile[0][count]
        if i == 'C':
            nuc = profile[1][count]
        if i == 'G':
            nuc = profile[2][count]
        if i == 'T':
            nuc = profile[3][count]
        count += 1
        multiplier = multiplier * nuc
    return multiplier 
# sanitycheck = kmer_profile_val('ACCT', profile_matrix(count_matrix(dna_matrix('TTACCTTAACGATGTCTGTCACGGCGTTAGCCCTAACGCGCGTCAGAGGT', 10 ))))
# print(sanitycheck)
def get_first_kmer(k, dna_matrix): 
    first_kmer_list = []
    for i in dna_matrix: 
        first_kmer_list.append(i[0:k])
    return first_kmer_list 
# sanitycheck = ['ACGTA', 'AGCTA', 'CGTAC']
# print(get_first_kmer(k = 3, dna_matrix= sanitycheck))
def get_all_kmers(dna_str, k):
    i = 0 
    kmer_list = []
    for _ in range(0, len(dna_str)-k+1):
        substring = dna_str[i:i+k]
        kmer_list.append(substring) 
        i += 1
    return kmer_list 
# sanitycheck = get_all_kmers(dna_str = "ACGTTCAGTTAC", k = 3)
# print(sanitycheck)
def most_probable_kmer(get_all_kmers, profile_matrix):
    ideal = 0 
    temp_dict = {} 
    for kmer in get_all_kmers:
        value = kmer_profile_val(kmer, profile_matrix)
        temp_dict[value] = kmer
        if value > ideal:
            ideal = value
    return temp_dict[ideal]
# list = ['TACC', 'ACCT', 'CCTT', 'TTAC']
# sanitycheck = most_probable_kmer(list, profile_matrix(count_matrix(dna_matrix('TTACCTTAACGATGTCTGTCACGGCGTTAGCCCTAACGAGCGTCAGAGGT', 10))))
# print(sanitycheck)
def greedy_motif_search(k, dna, rowlength):
    motifs = []

    matrix = dna_matrix(dna, rowlength) 
    first_kmers = get_first_kmer(k, matrix) 
    first_kmers_profile = profile_matrix(count_matrix(first_kmers))
    all_kmers_in_1st_row = get_all_kmers(matrix[0], k)
    motif1 = most_probable_kmer(all_kmers_in_1st_row, first_kmers_profile)
    motifs.append(motif1) 

    dna_matrix_rowtracker = 1 
    for _ in range(0, len(matrix) - 1):
        profile = profile_matrix(count_matrix(first_kmers))
        motif = most_probable_kmer(get_all_kmers(matrix[dna_matrix_rowtracker], k), profile)
        motifs.append(motif) 
        dna_matrix_rowtracker += 1
    return motifs
sanitycheck = greedy_motif_search( k = 3, dna = 'GGCGTTCAGGCAAAGAATCAGTCACAAGGAGTTCGCCACGTCAATCACCAATAATATTCG', rowlength = 5)
print(sanitycheck)



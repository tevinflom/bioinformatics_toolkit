import math 

class MotifEntropy():
    def __init__(self):
        #MODULAR
        pass
    def Entropy(motif_list):
        '''
        This fcn computes the total Shannon entropy of a motif matrix.
        Args: (list) - motif matrix of DNA strings of equal lengths 
        Returns: (float) - Shannon entropy of the whole matrix
        '''
        indiv_entropy = {}
        motif_count = len(motif_list)
        motif_len = len(motif_list[1])
        print(f'This set has {motif_count} sequences of length {motif_len}.')
        for i in range(motif_count):
            if len(motif_list[i]) != motif_len:
                print('Error: All motif sequences must be of the same length.')
                break
        for nuc in 'ATGC':
            vals = [0] * motif_len
            indiv_entropy[nuc] = vals
        total_entropy = 0 
        for key, vals in indiv_entropy.items():
            for seq in motif_list:
                for i in range(len(seq)):
                    if seq[i] == key:
                        indiv_entropy[key][i] += 1
            for int_val in range(len(vals)):
                indiv_entropy[key][int_val] = indiv_entropy[key][int_val] / float(motif_count)
            for value in vals:
                if value > 0:
                    total_entropy += abs(value * math.log(value, 2))
        #print(f'The entropies of each motif sequence are {indiv_entropy}.')
        #print(f'The total entropy of the set is {total_entropy}.')

        return total_entropy
    test_set = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]
    #test = Entropy(motif_list = test_set)
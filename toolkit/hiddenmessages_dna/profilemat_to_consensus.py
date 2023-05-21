class ProfileToConsensus():
    def __self__():
        #MODULAR
        pass
    def profile_to_consensus():
        '''
        This fcn generates a profile matrix and builds a consensus string. 
        '''
        seqs = ['ATCCAGCT',
                'GGGCAACT',
                'ATGGATCT',
                'AAGCAACC',
                'TTGGAACT',
                'ATGCCATT',
                'ATGGCACT']
        k = len(seqs[0])
        profile_matrix = {
            'A':[0]*k,
            'C':[0]*k,
            'G':[0]*k,
            'T':[0]*k
        }
        for seq in seqs:
            for pos, nuc in enumerate(seq):
                profile_matrix[nuc][pos] += 1
        result = [] # saves nucleotide and max count per row 
        for pos in range(k):
            max_count = 0 
            max_nuc = None
            for nuc in ['A', 'C', 'G', 'T']:
                count = profile_matrix[nuc][pos]
                if count > max_count:
                    max_count = count
                    max_nuc = nuc
            result.append(max_nuc)
        consensus_seq = ''.join(result)
        print(consensus_seq)
        print(profile_matrix)
        return profile_matrix

    

    profile_to_consensus()
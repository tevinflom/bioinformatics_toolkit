class CountMatrix():
    def __self__():
        #MODULAR
        pass
    def count():
        '''
        This fcn generates a profile count matrix.
        '''
        seqs = ['ATCCAGCT',
                'GGGCAACT',
                'ATGGATCT',
                'AAGCAACC',
                'TTGGAACT',
                'ATGCCATT',
                'ATGGCACT']
        k = len(seqs[0])
        count_matrix = {
            'A':[0]*k,
            'C':[0]*k,
            'G':[0]*k,
            'T':[0]*k
        }
        for seq in seqs:
            for pos, nuc in enumerate(seq):
                count_matrix[nuc][pos] += 1
        print(count_matrix)
        return count_matrix

    

    count()
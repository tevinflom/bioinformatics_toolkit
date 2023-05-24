class DeaminationSkew():
    def __init__(self):
        # MODULAR 
        pass
    def skew(genome):
        '''
        This function minimizes the statistical skew caused by the
        deamination of cytosine to form thymine in a single stranded DNA string.
        It finds the optimal substring of size i to minimize deamination effects.
        Args: (str) genome - single stranded DNA, reverse strand
        Returns: (str) skew - str from list of skew values for each nucleotide in genome
                 (list) int values of substring lengths i that minimize int value of skew
                
        ''' 
        skew = [0]
        skew_val = 0
        nucleotides = ["G", "C", "A", "T"]
        for nucleotide in genome: 
            if nucleotide == nucleotides[0]:
                skew_val += 1       
            elif nucleotide == nucleotides[1]:
                skew_val -= 1
            else:
                skew_val += 0
            skew.append(skew_val)
        
        #print(*skew)
       # print([int(nucleotide) for nucleotide, pos in enumerate(skew) if pos == max(skew)])
        return skew and [int(nucleotide) for nucleotide, pos in enumerate(skew) if pos == min(skew)]
    #test = skew(genome = 'GCATACACTTCCCAGTAGGTACTG')





            







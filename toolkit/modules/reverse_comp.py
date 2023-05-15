from Bio import SeqIO

class ReverseCompliment(): 
    def __init__(self):
        pass
    def reverse_comp(dna):
        '''
        This function gives the reverse compliment of a DNA string. It is based on the logic of replication, so it is naive.
        Args: (str) DNA - DNA string
        Returns: (str) reverse_compliment - reverse compliment of the DNA string
        '''

        base_pair_convert = dna.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
        base_pair_convert = base_pair_convert.upper() 
        reverse_comp = base_pair_convert[::1]
        print(reverse_comp)
        return(reverse_comp)
      

       

                
        
    test = reverse_comp(dna = "AAATTTGGGCCCATGCATGC")
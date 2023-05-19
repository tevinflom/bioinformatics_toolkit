from hamming_distance import HammingDistance

class MedianString():
    def __init__(self):
        #MODULAR
        pass

    def MedianString(dataset_path, k):
        '''
        This fcn finds the median motif of size k that minimizes hamming distance among all other possible kmers in the set.
        Args: (str) - dataset path, data is each substring in the DNA on its own line in .txt file, (int) - k, desired motif size
        Returns: (str) - median, the median kmer that minimizes distance among all other kmers concatenated from substrings in dataset 
        '''

        with open(dataset_path, 'r') as dataset:
            dna = dataset.readlines()
            possible_kmers = []
            for substring in dna:
                seq = substring.strip('\n')
                for i in range(len(seq) - k+1):
                    pattern = seq[i:i+k]
                    if pattern not in possible_kmers:
                        possible_kmers.append(pattern)

                min_distance = float('inf')
                for kmer in possible_kmers:
                    for i in range(len(seq) - k+1):
                        if min_distance > HammingDistance.hamming_2str(kmer, seq[i:i+k]):
                            min_distance = HammingDistance.hamming_2str(kmer, seq[i:i+k])
                            median = kmer
        print(f'The median motif that minimizes hamming distance among all possible kmers is {median}.')
        return(median)

    test = MedianString(dataset_path = 'dataset.txt', k = 6)
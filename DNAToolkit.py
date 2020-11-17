import collections
from Structures import *

# DNA Toolkit file

# Check the sequence to make sure it is a DNA String
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict


def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T", "U")


def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine. Reversing newly generated string."""
    # return "".join([Complement[nuc] for nuc in seq])[::-1] #reverse
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]


def gc_content(seq):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subsec(seq, k=20):
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res
 
    
def translate_seq(seq, init_pos=0):
    return (DNA_Codons[seq[pos:pos + 3]] for pos in range[init_pos, len(seq) - 2, 3 ])     
      

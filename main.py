from DNAToolkit import *
from utilities import *
import random

#randomizer for DNA String
rmdDNAStr = "".join([random.choice(Nucleotides)
                    for nuc in range(50)])

DNAStr = validateSeq(rmdDNAStr)
longueur = str(len(DNAStr))

print("\nSequence : " + colored(DNAStr))
print("\n[1] + Sequence Length: " + longueur)
print("\n[2] + Nucleotide Frequency: " +
      colored(str(countNucFrequency(DNAStr))))
print("\n[3] + DNA/RNA Transcription: " + colored(str(transcription(DNAStr))))
print("\n[4] + DNA String + Complement + Reverse Complement : ")
print("\n5' " + colored(DNAStr) + " 3'")
print("   " + "|" * len(DNAStr))
print("3' " + colored(reverse_complement(DNAStr)[::-1]) + " 5' (Complement)")
print("5' " + colored(reverse_complement(DNAStr)) + " 3' (reverse_complement)")
print(f"\n[5] + GC Content : {gc_content(DNAStr)}%")
print(
      f"\n[6] + GC Content Subsequence for k=10: {gc_content_subsec(DNAStr, 10)}")

print(
      f"\n[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr)}")

print(
      f"\n[8] + Codon frequency (L): {codon_usage(DNAStr, 'L')}")

gene = input("enter your gene sequence:") #input the gene of interest

codon = []      #makes sets of codon from the gene
for i in range(0,len(gene),3):
    code = gene[i:i+3]
    codon.append(code)

# codon table
codontab = {                      
    'TCA': 'S',    # serine
    'TCC': 'S',    # serine
    'TCG': 'S',    # serine
    'TCT': 'S',    # serine
    'TTC': 'F',    # Phenylalanine
    'TTT': 'F',    # Phenylalanine
    'TTA': 'L',    # leucine
    'TTG': 'L',    # leucine
    'TAC': 'Y',    # Tyrosine
    'TAT': 'Y',    # Tyrosine
    'TAA': '*',    # Stop
    'TAG': '*',    # Stop
    'TGC': 'C',    # Cysteine
    'TGT': 'C',    # Cysteine
    'TGA': '*',    # Stop
    'TGG': 'W',    # Tryptophan
    'CTA': 'L',    # leucine
    'CTC': 'L',    # leucine
    'CTG': 'L',    # leucine
    'CTT': 'L',    # leucine
    'CCA': 'P',    # Proline
    'CCC': 'P',    # Proline
    'CCG': 'P',    # Proline
    'CCT': 'P',    # Proline
    'CAC': 'H',    # Histidine
    'CAT': 'H',    # Histidine
    'CAA': 'Q',    # Glutamine
    'CAG': 'Q',    # Glutamine
    'CGA': 'R',    # Arginine
    'CGC': 'R',    # Arginine
    'CGG': 'R',    # Arginine
    'CGT': 'R',    # Arginine
    'ATA': 'I',    # Isoleucine
    'ATC': 'I',    # Isoleucine
    'ATT': 'I',    # Isoleucine
    'ATG': 'M',    # Methionine
    'ACA': 'T',    # Threonine
    'ACC': 'T',    # Threonine
    'ACG': 'T',    # Threonine
    'ACT': 'T',    # Threonine
    'AAC': 'N',    # Asparagine
    'AAT': 'N',    # Asparagine
    'AAA': 'K',    # Lysine
    'AAG': 'K',    # Lysine
    'AGC': 'S',    # serine
    'AGT': 'S',    # serine
    'AGA': 'R',    # Arginine
    'AGG': 'R',    # Arginine
    'GTA': 'V',    # Valine
    'GTC': 'V',    # Valine
    'GTG': 'V',    # Valine
    'GTT': 'V',    # Valine
    'GCA': 'A',    # Alanine
    'GCC': 'A',    # Alanine
    'GCG': 'A',    # Alanine
    'GCT': 'A',    # Alanine
    'GAC': 'D',    # Aspartate
    'GAT': 'D',    # Aspartate
    'GAA': 'E',    # Glutamate
    'GAG': 'E',    # Glutamate
    'GGA': 'G',    # Glycine
    'GGC': 'G',    # Glycine
    'GGG': 'G',    # Glycine
    'GGT': 'G'     # Glycine
}
               
for code in codon:           #coverts gene sequence into amino acid sequence
    print(codontab[code])

# perferable codon of amino acid synethesis
synechococcus_elongatus = {
    'F': 'TTT',
    'L': 'CTG',
    'I': 'ATC',
    'M': 'ATG',
    'V': 'GTG',
    'S': 'AGC',
    'P': 'CCC',
    'T': 'ACC',
    'A': 'GCC',
    'Y': 'TAC',
    'H': 'CAC',
    'Q': 'CAG',
    'N': 'AAC',
    'K': 'AAA',
    'D': 'GAT',
    'E': 'GAA',
    'C': 'TGC',
    'W': 'TGG',
    'R': 'CGC',
    'G': 'GGC',
    '*': 'TAG'
}

# optimizes the gene sequence
optimized_seq = []
for code in codon:
    aa = codontab[code]
    preferred = synechococcus_elongatus[aa]
    optimized_seq.append(preferred)



optimized_sequence = "".join(optimized_seq)
print("Optimized sequence:", optimized_sequence)
print("Original length:", len(gene))
print("Optimized length:", len(optimized_sequence))

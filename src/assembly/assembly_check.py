from Bio import SeqIO

for record in SeqIO.parse("~/nanopore/pacbio_trial/canu/assembly/r1v1_canu.fasta", "fasta"):
    print(record.id)
    print(len(record.sequence))

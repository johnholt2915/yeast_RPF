Files which were used to perform jobs on NYU's HPC servers.

* Files appended with `_ribo` were used to process ribosome sequencing
data (RPF).
* Files without the `_rna` suffix were used to process RNA sequencing data.

###1. cutadapt_ribo.pbs / cutadapt_rna.pbs
These files
* Removed the adapter sequences.
* Specified a minimum sequence length (`>30` for RNA / `25 >=` and `<=36` for ribosome)
* Removed the adapter sequence `"AGATCGGAAGAGCACACGTC"`

###2. bowtie_ribo.pbs / bowtie_rna.pbs
* Both files are identical except filenames. These files aligned the sequences with rRNA
genes.

###3. tophat_ribo.pbs / tophat_rna.pbs

* Both files are identical except for filenames. They align the unaligned files from `Step 2`
with the annotated yeast genome.

###4. feature_counts.sh
* Counts the number of reads aligned to features of the genome (exons and CDS).
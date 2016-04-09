module load subread

featureCounts -T 4 -t exon -t CDS -g gene_id -a ../GTF/noHead.gtf -o counts_2.txt tophat_out2/accepted_hits.bam

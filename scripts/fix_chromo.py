#!/usr/bin/python

import optparse


def fixGTF(gtf, num):
    """fixGTF takes a gtf file (General Transfer Format) of gene annotations
    of Saccharomyces cerevisiae and fixes the chromosome label for TopHat2
    alignment.
    gtf = a GTF file (9 line tab delimited file)
    num = number of different chromosomes in the FASTA genome file

    The output is a file named 'fixed.gtf'

    NOTICE: 1st line of gtf input file must be in GTF format!
    """
    with open(gtf, 'r') as f:
        new_file = open('fixed.gtf', 'w')
        line = f.readline().split('\t')
        line[0] = 'chr' + line[0]
        # iterate through the different chromosomes (assuming the GTF has all
        # chromosome annotations in a single chunk of the file)
        for i in range(num):
            new_file.write('\t'.join(line))
            line = f.readline().split('\t')
            # the first column of the GFF is the chromosome label that needs
            # fixing
            chromo = line[0]
            # this checks to make sure the line we've just read has same
            # chromosome label needing to be fixed as the first appearance of
            # the label.
            current_Chromo = line[0]
            #fixing the label
            line[0] = 'chr' + chromo
            while current_Chromo == chromo:
                new_file.write('\t'.join(line))
                line = f.readline().split('\t')
                chromo = line[0]
                line[0] = 'chr'+chromo
        new_file.close()
    return 'Fixed the GTF!'


def main(gtf_file, number_chromo):
    fixGTF(gtf_file, number_chromo)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-g', dest='gtf', default='', help='input GTF file')
    parser.add_option('-n', dest='num', help='number of chromosomes')

    (options, args) = parser.parse_args()

    gtf = options.gtf
    num = options.num

    main(gtf, int(num))

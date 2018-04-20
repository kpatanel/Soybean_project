#Kiera Patanella, Programming I Project
"""Objective: to observe differential expression among various cultivars of the soybean Glycine max, some of which 
are inoculated with the soybean mosaic virus"""
#Step one: make a probe-gene dictionary
import sys
gse_file=sys.argv[1]
gene_inten={}
with open(gse_file,'r') as gs:
    next(gs)
    for line in gs:
        f=line.strip().split('\t')
        probe=f[0]
        cults=f[1:]
        with open('first_50_chr1.txt','r') as gsoya:
            for line in gsoya:
                m=line.strip().split('\t')
                gkey=m[5].split(" ")[0]
                vals=m[0]
                if vals==probe:
                    gene_inten[gkey]=cults
                    break

#Step Two: Iterate through dictionary with f string literal to  show genes of interest and their expression across cultivars
with open('project_results.csv','w') as pr:
    header='Uniref_gene' + ',' + 'Rsmv1_inoculated' + ',' + 'Rsmv1_mock' + ',' + 'Ssmv1_inoculated' + ',' + 'Ssmv1_mock' + '\n'
    pr.write(header)
    for gene in gene_inten.keys():
        out=f'{gene},{gene_inten[gene][0]},{gene_inten[gene][1]},{gene_inten[gene][2]},{gene_inten[gene][3]}\n'
        #pr.write(header + '\n' + out)
        pr.write(out)



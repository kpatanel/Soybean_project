# Soybean_project
Programming I class project studying the effects of the soybean mosaic virus on gene expression on 50 genes in chromosome 1. Data obtained from the Gene Expression Omnibus accession GSE90448 (He and Liu, 2016).
Step 1: Execute obtain_gcrma.R to normalize all CEL files.
Step 2: Next, execute project_code.py to create a probe-gene dictionary and align expression values with their proper genes.
Step 3: Finally, execute produce_heatmap.R to generate a heatmap of each gene's expression. 

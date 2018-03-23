#download and install packages
setwd("/Users/kierapatanella/Desktop/Soybean_project")
source("http://bioconductor.org/biocLite.R")
biocLite("DESeq")
library("DESeq")
biocLite("DESeq2")
library("DESeq2")
biocLite("affy")
biocLite("oligo")
biocLite("limma")
library("affy")
library("pheatmap")
gm_data<-read.csv("project_results.csv", header=TRUE, row.names=1)
gm_data<-as.matrix(gm_data)
storage.mode(gm_data)="numeric"
condition<-factor(c("RSmv1_inoculated", "Rsmv1_mock", "Ssmv1_inoculated", "Ssmv1_mock"))
colData<-data.frame(row.names = colnames(gm_data), condition)
colData
pheatmap(gm_data, cluster_rows=FALSE, show_rownames=TRUE, cluster_cols=TRUE)

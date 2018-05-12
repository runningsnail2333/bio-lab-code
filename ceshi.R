setwd('C:\\Users\\Administrator\\Desktop\\123')
data1 <- read.delim("merged.without_SNP.without_NA.head100",header =T,sep="\t")
data3 <- data1[,-match(c("TCGA.D8.A27L.01A","TCGA.A7.A26J.01A"),names(data1))]
#data3 <- subset(data2,select =-c(TCGA-D8-A27L-01A,TCGA-A7-A26J-01A))
data3


colnames(data3)
row.names(data3)
row.names(data1)
nrow(data1)
ncol(data1)

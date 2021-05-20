data("esoph")
#search()
head (esoph, n=10)
colnames (esoph) 
dim(esoph) # dimension of df
length (esoph$tobgp)
sd (esoph$ncases)  # standard deviation
summary(esoph)
mean (subset(esoph$ncases, esoph$tobgp == "28+"))
plot (esoph$ncases, esoph$ncontrols)
hist(esoph$ncases, xlab="Nr of cases", main="Esoph data", col="orange")
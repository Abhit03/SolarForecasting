c = read.csv("BangaloreZenith.txt")
d = split(c, day)

rev = d

for(i in 1:99)
{rev[[i]][7:19, 12] <- d[[i]][19:7, 12]}

e = do.call(rbind, rev)

for(i in 1:99)
{
fit = lm(ghi ~ Cos.zenith, data = d[[i]])
fit2 = lm(ghi ~ Cos.zenith, data = rev[[i]])
fi$corfit1[i] = cor(fitted(fit), d[[i]]$ghi)
fi$corfit2[i] = cor(fitted(fit2), rev[[i]]$ghi)
}
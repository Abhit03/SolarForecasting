filenames=list.files(path = "~/documents/7820", full.names=TRUE)
filetrain <- filenames[1:9]
filetest <- filenames[10]

##Creating the dat variable joining all the rows from all 9 years in training files
dat <- data.frame()
for(i in 1:length(filetrain))
{
	f <- read.csv(file = filetrain[2], skip = 1)
	dat <- rbind(dat, f)
}

##Creating the doc variable to add date and time variables 
doc <- dat

doc$datetime = paste(doc[, 1], doc[, 2], sep = " ")
doc$datetime <- strptime(doc$datetime, format='%m/%d/%Y %H:%M')

doc$hour <- strftime(doc$datetime, format = "%H")
doc$hour <- as.integer(doc$hour)
doc$hour <- doc$hour + 1


doc$day <- strftime(doc$datetime, format = "%j")
doc$day <- as.integer(doc$day)
doc$week <- doc$day%/%7
doc$week <- doc$week + 1

doc$month <- strftime(doc$datetime, format = "%m")
doc$year <- strftime(doc$datetime, format = "%Y")

##Creating a GHI taining dataset containg the required columns for building the model
ghitrain <- data.frame(id = 1:nrow(doc))

ghitrain$datetime <- doc$datetime
ghitrain$hour <- doc$hour
ghitrain$day <- doc$day
ghitrain$week <- doc$week
ghitrain$month <- doc$month
ghitrain$year <- doc$year

ghitrain$ghi <- doc$GHI..W.m.2.

##tools for inference
which(ghitrain$ghi > 0 & ghitrain$hour == 6)     ## 5 AM
which(ghitrain$ghi > 0 & ghitrain$hour == 19)    ## 6 PM

##tools for checking
varlist <- sapply(doc, function(x) length(unique(x)))
##tools for subsetting
ghisub <- subset(ghitrain, ghi > 0)

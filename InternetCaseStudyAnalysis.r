

#1-	The team wants to analyze each variable of the data collected through data summarization to get a basic understanding of the dataset and to prepare for further analysis.
#2-	A unique page view represents the number of sessions during which that page was viewed one or more times. A visit counts all instances, no matter how many times the same visitor may have been to your site. So the team needs to know whether the unique page view value depends on visits.
#3-	Find out the probable factors from the dataset, which could affect the exits. Exit Page Analysis is usually required to get an idea about why a user leaves the website for a session and moves on to another one. Please keep in mind that exits should not be confused with bounces. 
#4-	Every site wants to increase the time on page for a visitor. This increases the chances of the visitor understanding the site content better and hence there are more chances of a transaction taking place. Find the variables which possibly have an effect on the time on page.
#5-	A high bounce rate is a cause of alarm for websites which depend on visitor engagement. Help the team in determining the factors that are impacting the bounce.

getwd()

setwd("C:/Users/adity/Documents/R/Rubics python + R code/Internet")
#Read the data
InternetData<-read.csv("InternetData.csv")
str(InternetData)
 

 
#1: Understand the data
summary(InternetData)

#2: Do the unique page views depends on the visits?
UniquePgAnalysis<-aov(Uniquepageviews~Visits, data=InternetData)
summary(UniquePgAnalysis) 

#3: Exit page analysis
ExitPgAnalysis<-aov(Exits~Timeinpage+Continent+Sourcegroup+Bounces+Uniquepageviews+Visits, data=InternetData)
summary(ExitPgAnalysis)


#4: Time on page depends on?
TimeOnPg<-aov(Timeinpage~Exits+Continent+Sourcegroup+Bounces+Uniquepageviews+Visits, data=InternetData)
summary(TimeOnPg)


#5: Bounce rate

summary(InternetData)
BounceRate_Reg<-lm(Bounces~Timeinpage+Continent+Exits+Sourcegroup+Uniquepageviews+Visits, data=InternetData)
summary(BounceRate_Reg)

# predicting-the-opening-weekend-gross-of-movies

In this repository, I am sharing preliminary work of web scraping three websites and my initial attempts of exploring the data by utilizing regression models.

Initially to getter data I used Scrapy to scrap data from IMDB, NUMBERS and Box Office Mojo. You can see the spiders in the attached folder. Afterwards, by merging the three data their venn diagram resulted in a data set with 2687 movie title spanning between 1974 and 2016.  

I have selected the following features for future modeling:

- First movie star listed (categorical)
- Director (categorical)
- Opening Gross (value)
- Theaters (value)        
- Title
- Release date (categorical)         
- Budget (value)

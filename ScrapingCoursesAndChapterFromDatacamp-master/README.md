This is a spider to scrape all courses and their chapters from Datacamp

# Why scrape datacamp?
This is a awkward story. 

I was searching for a course from Datacamp. My browser froze all the time, and I was tired of waiting for hiting the 'more' button to load the other courses which cannot be filled in one page. So I thought why not scrape all courses and put them in a csv file so that I could cluster them and tag them. That's why I wrote this scraper.

# How to implement?
The process is easy and handy:

1. Run firstSpider.py file
2. Run outputCsv.py file

# What you need to offer and what you get? 
## Input
The link to the [main course page of Datacamp](https://www.datacamp.com/courses/all)
![Datacamp page preview](https://github.com/BrandonJia/WebScraping/blob/master/ScrapingCoursesAndChapterFromDatacamp-master/Capture.PNG)
## Output 
After several seconds, a CSV file named datacampCourses.csv which includes all courses offered by Datacamp and their chapters.
[Here is the results](https://github.com/BrandonJia/WebScraping/blob/master/ScrapingCoursesAndChapterFromDatacamp-master/datacamp_courses.csv)

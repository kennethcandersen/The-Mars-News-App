# Web Scraping Challenge: The Mars News App

<a href="https://github.com/kennethcandersen/web-scraping-challenge/blob/main/screenshot_of_final_app.png" target="_blank"><img width="900" alt="Final App Screenshot" src="https://github.com/kennethcandersen/web-scraping-challenge/blob/main/screenshot_of_final_app.png"></a>

**EXECUTIVE SUMMARY**

This app scrapes the latest data regarding Mars exploration and presents it in one convenient user interface, demonstrated in the image above.


**REPOSITORY NAVIGATION**

* [*Scraping code in Jupyter Notebook*](https://github.com/kennethcandersen/web-scraping-challenge/blob/main/Missions_to_Mars/mission_to_mars.ipynb) contains test code for scraping the various elements needed for the app, before converting to one python function (see next item).
* [*Scraping function in Python*](https://github.com/kennethcandersen/web-scraping-challenge/blob/main/Missions_to_Mars/scrape_mars.py) contains the complete tested code for scraping data for the app. This function is called by the app (see next item). 
* [*Mission to Mars App*](https://github.com/kennethcandersen/web-scraping-challenge/blob/main/Missions_to_Mars/mission_to_mars_app.py) contains the Python code for running the full application. It calls the scraping function (above).

**OBJECTIVE**

Create an app that automatically concentrates and displays the latest data on Mars exploration from four different websites into one convenient user interface. 


**STEPS, TOOLS & LANGUAGES USED**

1. Create an unstructured database in Mongo. An unstructured database makes sense since the project requires collecting a heterogenous set of data, including images, text and data formatted in a table. 
2. Create and test the scraping code in Jupyter Notebook. The code uses Splinter, ChromeDriverManager, BeautifulSoup, and Pandas. The scraped data is exported directly to the Mongo database using Pymongo. 
3. Convert the scraping code created in Notebook into one Python file as a function that can be called by the app. 
4. Create the app in a Python file using Flask that calls the scraping function, then launches the HTML page that renders the data (see next item).
5. Create an HTML file with Bootstrap and CSS that renders the data in a convenient user interface. 

=======



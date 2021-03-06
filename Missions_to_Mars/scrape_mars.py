#!/usr/bin/env python
# coding: utf-8

# Import dependencies

from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json

##########################################################################
#                            Scrape Article
##########################################################################

def scrape_mars():
    """ 
    PURPOSe: Called by the mission_to_mars_app.py to refresh the data that it renders.

    INPUT: nothing

    RETURNS: Dictionary with a heterogenous collection suitable for a Mongo
    database:
        1. Mars article: header, teaser and url for latest article 
        from https://redplanetscience.com
        2. Mars featured image: url from https://spaceimages-mars.com/
        3. Mars fact table: data scraped from https://galaxyfacts-mars.com/
        4. 

    """
    # Set up dictionary to collect various data elements and return at end of function
    scrape_results = {}           

    # Setup splinter for the whole project
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Setup url and launch browser
    article_url = 'https://redplanetscience.com'             
    browser.visit(article_url)

    # Use BeautifulSoup to extract the article's 
    # Header and Teaser, and assign them to variables

    soup = bs(browser.html, 'html.parser')

    article_headers = soup.find_all('div', class_='content_title')
    first_article_header = article_headers[0].text

    article_teasers = soup.find_all('div', class_='article_teaser_body')
    first_article_teaser = article_teasers[0].text

    #print(f"\n-----Article successfully extracted-----\n")

    scrape_results['Article_Header'] = first_article_header
    scrape_results['Article_Teaser'] = first_article_teaser

    ##########################################################################
    #                         Scrape Featured Image
    ##########################################################################

    # Setup url and launch browser
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)


    # Use BeautifulSoup to read the url and extract the featured image url

    soup = bs(browser.html, 'html.parser')

    featured_images = soup.find_all('img', class_='headerimage fade-in')

    featured_image_url = f"{image_url}{featured_images[0]['src']}"

    #print(f"\n-----Featured Image URL successfully extracted-----\n")
    
    scrape_results['Featured_Image'] = featured_image_url
    
##########################################################################
#                         Scrape Fact Table
##########################################################################

    # Setup url and launch browser
    mars_facts_table_url = 'https://galaxyfacts-mars.com/'
    browser.visit(image_url)


    # Use Pandas to read the url and extract the table
    mars_facts_df = pd.read_html(mars_facts_table_url)[0]
    mars_facts_df.columns = ['', 'Mars', 'Earth']  # Clean up column names
    mars_facts_df = mars_facts_df.iloc[1:]                                # Get rid of first row
    mars_facts_df.set_index('', inplace=True)      # Replace numbered index

    # Export the table to html file
    html_str = mars_facts_df.to_html(col_space="30%", classes='mars_table', justify='center')

    #print(f"\n-----Mars Fact Table successfully extracted & exported to file-----\n")
    
    scrape_results['Mars_Fact_Table'] = html_str

    ##########################################################################
    #                      Scrape Hemisphere Images
    ##########################################################################

    # Setup url and launch browser
    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)

    # Use BeautifulSoup to read the url and extract the description section 
    #for each of the 4 "Products" (Hemispheres)
    soup = bs(browser.html, 'html.parser')
    products = soup.find_all('div', class_= 'description')


    # Iterate over the text for each "Product" (Hemisphere) and extract the title and url for the 
    #high res tiff file.

    hemisphere_images = []                            # Set up list for results, as instructed

    for product in products:                          # Iterate over the projects on the page
        
        temp_dict = {}                                # Set up temporary dictionary for results
        
        # Get image title
        hemisphere_image_title = product.find('h3').text      # Extract title from the <h3> tags
        temp_dict['image_title'] = hemisphere_image_title     # Add Image Title to dictionary
        
        
        # Get url for high resolution jpg file
        hemisphere_url = product.find_all('a', class_='itemLink product-item')[0]['href'] # Get link for product page
        hemisphere_url_complete = f"{hemispheres_url}{hemisphere_url}"
        
        browser.visit(hemisphere_url_complete)                         # Send browser to product page
        soup = bs(browser.html, 'html.parser')                                 # Parse product page
        temp_dict['hemi_info_url'] = hemisphere_url_complete 
        # Drill down into text to get the .tif url
        hemisphere_image_url = soup.find('div', {'class' :'downloads'}).find('ul').find_all('a')[0]['href']                               
        hemisphere_image_url_complete = f"{hemispheres_url}{hemisphere_image_url}"  # Piece together the full url
        temp_dict['image_url'] = hemisphere_image_url_complete                            # Add url to dictionary
        
        # Append dictionary to list
        hemisphere_images.append(temp_dict)

    #print(f"\n-----Hemisphere Titles & Image URLs successfully extracted-----\n\n")

    scrape_results['Mars_Hemisphere_Images'] = hemisphere_images

    #   Close browser
    browser.quit()
    #print(f"\n-----Browser closed and scrape is complete!-----\n\n")

    #print(scrape_results)
    return scrape_results

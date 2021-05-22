import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def mars_latest_news():
    browser = init_browser()
    
    mars_news_url = "https://redplanetscience.com/"
    browser.visit(mars_news_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_news_title = soup.select_one('div', class_='list_text')

    print(mars_news_title)

    news = mars_news_title.find('div', class_='content_title')
    print(news.text)

    news_p = mars_news_title.find('div', class_='article_teaser_body')
    print(news_p.text)
    
    browser.quit()

def featured_image():
    image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(image_url)

    space_image = browser.find_by_tag('button')[1]
    space_image.click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image = soup.find('img', class_='fancybox-image').get('src')
    print(featured_image)

    image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + featured_image
    print(image_url)
    
    browser.quit()

def mars_facts():
    facts_url = "https://galaxyfacts-mars.com/"

    tables = pd.read_html(facts_url)
    print(tables)

    df = tables[0]
    df.columns=["Mars - Earth Comparison", "Mars", "Earth"]
    mars_df = df.drop(index=0)
    print(mars_df)

    html_table = mars_df.to_html()
    print(html_table)
    
    browser.quit()

def mars_hemispheres():
    hems_url = "https://marshemispheres.com/"
    browser.visit(hems_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    titles = []

    titles_search = soup.find_all('div', class_="collapsible results")
    hemispheres = titles_search[0].find_all('h3')

    for mars in hemispheres:
        titles.append(mars.text)

    titles

    images_search = soup.find('div', class_="collapsible results")
    search_image = images_search.find_all('img', class_='thumb')
    image_urls = []

    for img in search_image:
        img_source = img['src']
        img_full_url = hems_url + img_source
        image_urls.append(img_full_url)
    print(image_urls)

    titles = []

    titles_search = soup.find_all('div', class_="collapsible results")
    hemispheres = titles_search[0].find_all('h3')

    for mars in hemispheres:
        titles.append(mars.text)

    print(titles)

    images_search = soup.find('div', class_="collapsible results")
    search_image = images_search.find_all('img', class_='thumb')
    image_urls = []

    for img in search_image:
        img_source = img['src']
        img_full_url = hems_url + img_source
        image_urls.append(img_full_url)

    print(image_urls)

    dictionary_zip = zip(titles, image_urls)

    hemisphere_image_urls = []

    for title, img in dictionary_zip:
        
        mars_dict = {}
        mars_dict['title'] = title
        mars_dict['img_url'] = img
        hemisphere_image_urls.append(mars_dict)

    hemisphere_image_urls
    
    browser.quit()







import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)

def scrape ():
    
    browser = init_browser()
    mars_data = {}

    local_nasa_file = "News_Nasa_Mars_Exploration_Program.html"
    nasa_html = open(local_nasa_file, "r").read()
    news_soup = BeautifulSoup(nasa_html, "html.parser")
    news_list = news_soup.find('ul', class_='item_list')
    first_item = news_list.find('li', class_='slide')
    first_title = first_item.find('div', class_='content_title').text
    first_para = first_item.find('div', class_='rollover_description_inner').text
    mars_data['first_title']=first_title
    mars_data['first_para']=first_para

    # jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # browser.visit(jpl_url)
    # jpl_html = browser.html
    # jpl_soup = BeautifulSoup(jpl_html, 'html.parser')
    # jpl_feature_link = jpl_soup.find('a', class_="button fancybox")['data-fancybox-href']
    # featured_image_url = f'https://www.jpl.nasa.gov{jpl_feature_link}'
    # mars_data['featured_image_url']=featured_image_url
    
    # weather_url = 'https://twitter.com/marswxreport?lang=en'
    # browser.visit(weather_url)
    # weather_html = browser.html
    # weather_soup = BeautifulSoup(weather_html, 'html.parser')
    # weather_tweet = weather_soup.find('div', class_='js-tweet-text-container')
    # mars_weather = weather_tweet.find('p').text
    # mars_data['mars_weather'] = mars_weather

    # facts_url = 'https://space-facts.com/mars/'
    # browser.visit(facts_url)
    # facts_html = browser.html
    # facts_soup = BeautifulSoup(facts_html, 'html.parser')
    # facts_table = facts_soup.find('table', class_='tablepress')
    # df = pd.read_html(str(facts_table))
    # mars_data['df']=df

    # hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # browser.visit(hemi_url)
    # hemi_html = browser.html
    # hemi_soup = BeautifulSoup(hemi_html, 'html.parser')
    # hemi_list = hemi_soup.findAll('div', class_='item')
    # title = hemi_list.find_all('a', class_='itemLink')
    # links = []
    # url = 'https://astrogeology.usgs.gov'
    # for t in title:
    #     link = t['href']
    #     item_path = f'{url}{link}'
    #     links.append(item_path)
    # links = set(links)
    # hemi_dicts = []
    # for url in links:
    #     hemi_dict = {}
    #     browser.visit(url)
    #     hemi_link_html = browser.html
    #     hemi_link_soup = BeautifulSoup(hemi_link_html, 'html.parser')
    #     hemi_link_title = hemi_link_soup.find('div', class_='content').find('h2').text.strip()
    #     hemi_link_url = hemi_link_soup.find('div', class_='downloads').find('li').find('a')['href']
    #     hemi_dict['title']=hemi_link_title
    #     hemi_dict['img_url']=hemi_link_url
    #     hemi_dicts.append(hemi_dict)
    # mars_data['hemi_dicts']=hemi_dicts
    
    browser.quit()

    return mars_data
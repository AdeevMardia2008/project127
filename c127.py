from selenium import webdriver
from bs4 import BeautifulSoup
import csv

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser=webdriver.Chrome("C:\Users\atira\Desktop\chromedriver")
browse.get(START_URL)
time.sleep(10)

def scrape():
    header=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_data"]
    planet_data=[]

    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,"html.phaser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].content[0])
                else:
                    try:
                        temp_list.append(li.tag.content[0])
                    except:temp_list.append("")
            planet_data.append(temp_list)

        browser.find_element_by_xpath("//*[@id="results"]/ul[10]/li[1]/a").click()
    
    with open("scraper_2.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(planet_data)

scrape()
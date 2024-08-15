from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import csv
import requests
import os
import base64


class FarmData():

    def __init__(self, url, delimeter, newLineDelimeter):
        self.url = url
        self.delimeter = delimeter
        self.soup = None
        self.brand_column_name_mapping = {"Brand Name": "FarmName", "Product Name": "FarmName", "Brand": "FarmName", "Brands": "FarmName"}  #for farm names                         
        self.data = []
        self.ordering_col = ["FarmName", "City", "State", "Logo", "Website"]  #Description has to be added later
        self.newFarmIndicator = newLineDelimeter
    

    def openlink(self):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        req = Request(self.url, headers=headers)
        html = urlopen(req)
        self.soup = BeautifulSoup(html, 'html.parser')


    def farm_name(self):

        table = self.soup.find('table')
        website_column_names = list(map(lambda th: th.get_text(strip=True), table.find_all('th')))
        self.column_names = [self.brand_column_name_mapping.get(i, i) for i in website_column_names]
        rows = table.find_all('tr')[1:] #skip over the first <tr> tag
        for i in rows:
            if 'segment-breakout' in i.get('class', []):  # skip "segment-breakout" rows
                continue
            text = i.find_all('td')
            row_values = [i.get_text(strip=True) for i in text]
            self.data.append((row_values, text))
    

    def parsing_link_contents(self): #City, State, Logo, Website contents found from accessing second url

        for row_values, text in self.data:
            city, state, logo, website = None, None, None, None
            for i in text:
                a_tag = i.find('a')
                second_url = a_tag['href'] if a_tag else None
                if second_url:
                    city, state = self.city_state_scraping(second_url)
                    logo = self.logo_scraping(second_url)
                    website = self.website_scraping(second_url)
            row_values.extend([city, state, logo, website])


    def city_state_scraping(self, url):

        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=headers)
        html = urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        city_state_tag = soup.find_all('span', class_='cornucopia-edit')
        city_state_text = []
        for i in city_state_tag:
            city_state_text.append(i.get_text())
        m1 = re.compile(r'\b([A-Za-z\s]+),\s([A-Z]{2})\b') #takes only city, state format from the list
        for i in city_state_text:
            match = m1.search(i)
            if match:
                city_state = match.group(0)
                m2 = re.match(r'^(.*?),\s*([A-Z]{2})$', city_state) #separates city and state
                if m2:
                    city = m2.group(1).strip()
                    state = m2.group(2).strip()
                    return city, state
        else:
            return None, None


    def logo_scraping(self, url):

        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=headers)
        html = urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        img_class = soup.find('div', class_='scorecard-image')
        if img_class:
            img_tag = img_class.find('img')
            if img_tag:
                src_tag = img_tag['src']  #img source link
                if src_tag.startswith('data:image'):  #checks for base64
                    string_match = re.search(r',(.+)', src_tag)
                    if string_match:
                        src_tag = string_match[1].strip()
                    return src_tag
                else:
                    return None
            else:
                return None
        else:
            return None


    def website_scraping(self, url):

        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=headers)
        html = urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        link_tag = soup.find('a', class_='eip-disable-link')
        if link_tag:
            get_url = link_tag['href']  #gets the url
            return get_url
        else:
            return None
        

    def cleaningTags(self):

        df = pd.DataFrame([row[0] for row in self.data], columns=self.column_names + ["City", "State", "Logo", "Website"])
        for i in set(self.brand_column_name_mapping.values()):
            if i not in df.columns:
                df[i] = np.nan 
        self.df = df[self.ordering_col]
    
    def pd_dataframe(self):
        return self.df


    def write_to_file(self, file_name):  #writes to a txt file

         with open(file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter= self.delimeter, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(self.ordering_col)  # Write header
            f.write(self.newFarmIndicator)
            for row in self.df.fillna('NULL').values:  #NULL for NaN values
                row_values = list(row[:-1])  # Exclude the last item in the row
                last_value = row[-1] if row[-1] != 'NULL' else ''  # Last item or empty string
                writer.writerow(row_values + [last_value + self.newFarmIndicator])


    def run(self, outputPath, outputFileName):
        self.openlink()
        self.farm_name()
        self.parsing_link_contents()
        self.cleaningTags()
        df = self.pd_dataframe()    
        self.write_to_file(os.path.join(outputPath, outputFileName))


def main():
    beef_url = 'https://www.cornucopia.org/scorecard/organic-beef-scorecard/'
    beef_outputFileName = 'beef_farmdata.txt'
    egg_url = 'https://www.cornucopia.org/scorecard/eggs/'
    egg_outputFileName = 'egg_farmdata.txt'

    dairyUrl = 'https://www.cornucopia.org/scorecard/dairy/'
    dairyFarmOutputFileName = "dairy_farmdata.txt"
    
    poultryUrl = 'https://www.cornucopia.org/scorecard/organic-poultry-scorecard/'
    poultryFarmFileName = "poultry_farm.txt"
    yogurtUrl= 'https://www.cornucopia.org/scorecard/organic-yogurt-scorecard/'
    yogurtFarmFileName = "yogurt_farm.txt"
    plantBasedBeveragesUrl = 'https://www.cornucopia.org/scorecard/plant-based-beverages/'
    plantBasedBeveragesFarmOutputFileName = "plant_farm.txt"
    snackbarUrl = 'https://www.cornucopia.org/scorecard/snack-bar-scorecard/'
    snackbarFarmOutputFileName = "snackbar_farm.txt"
    cottageCheeseUrl = 'https://www.cornucopia.org/scorecard/cottage-cheese/'
    cottageCheeseFarmFileName = "cottagecheese_farm.txt"
    cerealUrl = 'https://www.cornucopia.org/scorecard/cereal/'
    cerealFarmFileName = "cereal_farm.txt"
    soyUrl = 'https://www.cornucopia.org/scorecard/soy/'
    soyOutputFarmFileName = "soy_farm.txt"

    delimiter = '|'  #for each row value
    newLineDelimeter = '^_'  #for each row
    
    outputPath = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir"


    #beef for testing
    beef_data = FarmData(beef_url, delimiter, newLineDelimeter)
    #beef_data.run(outputPath, beef_outputFileName)


    
    #egg for testing
    egg_data = FarmData(egg_url, delimiter, newLineDelimeter)
    #egg_data.run(outputPath, egg_outputFileName)

    dairy_data = FarmData(dairyUrl, delimiter, newLineDelimeter)
    #dairy_data.run(outputPath, dairyFarmOutputFileName)
    poultry_data = FarmData(poultryUrl, delimiter, newLineDelimeter)
    #poultry_data.run(outputPath, poultryFarmFileName)
    yogurt_data = FarmData(yogurtUrl, delimiter, newLineDelimeter)
    #yogurt_data.run(outputPath, yogurtFarmFileName)
    plant_data = FarmData(plantBasedBeveragesUrl, delimiter, newLineDelimeter)
    #plant_data.run(outputPath, plantBasedBeveragesFarmOutputFileName)
    snackbar_data = FarmData(snackbarUrl, delimiter, newLineDelimeter)
    snackbar_data.run(outputPath, snackbarFarmOutputFileName)
    cottagecheese_data = FarmData(cottageCheeseUrl, delimiter, newLineDelimeter)
    cottagecheese_data.run(outputPath, cottageCheeseFarmFileName)
    cereal_data = FarmData(cerealUrl, delimiter, newLineDelimeter)
    cereal_data.run(outputPath, cerealFarmFileName)
    soy_data = FarmData(soyUrl, delimiter, newLineDelimeter)
    soy_data.run(outputPath, soyOutputFarmFileName)
    

if __name__ == '__main__':
    main()
    
#until we figure out description
''' 
    def description(self, url):
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=headers)
        html = urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
'''
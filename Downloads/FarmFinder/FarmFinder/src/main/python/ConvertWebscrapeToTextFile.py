from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import csv

class ScorecardData():

    def __init__(self, url, delimeter, newBrandIndicator):
        self.url = url
        self.delimeter = delimeter
        self.newBrandIndicator = newBrandIndicator
        self.soup = None
        self.brand_column_name_mapping = {
            "StarRating": "StarRating",
            "Score": "Score",
            "Products": "Products", "Product offerings": "Products",  #Products and PRoduct offerings under same colunn
            "Market area": "BrandMarketArea", "Market Area": "BrandMarketArea",
            "Certified Organic": "Organic", "Organic": "Organic",
            "Plant Base": "PlantBased",
            "Parent Company": "ParentCompany", "Company": "ParentCompany",
            "Company Type": "CompanyType", 
            "Participated in Survey?": "ParticipatedInSurvey",
            "Description": "Description",
            "Brand Name": "BrandName", "Product Name": "BrandName", "Brand": "BrandName", "Brands": "BrandName" #Brand, Product Name and Brand Name under same column
        }
        self.data = []

        self.ordering_col = [
            "StarRating", "Score", "Products", "BrandMarketArea", "Organic", "PlantBased", "ParentCompany",
            "CompanyType", "ParticipatedInSurvey", "Description", "BrandName"]


    def openlink(self):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        req = Request(self.url, headers=headers)
        html = urlopen(req)
        self.soup = BeautifulSoup(html, 'html.parser')


    def scrapingData(self):

        table = self.soup.find('table')
        website_column_names = list(map(lambda th: th.get_text(strip=True), table.find_all('th')))
        self.column_names = [self.brand_column_name_mapping.get(i, i) for i in website_column_names]

        rows = table.find_all('tr')[1:] #skips over the frst <tr> tag
        for i in rows:
            if 'segment-breakout' in i.get('class', []):  # skip "sgment-breakout" rows
                continue
            text = i.find_all('td')
            row_values = [i.get_text(strip=True) for i in text]
            if row_values:
                a_tag = i.find('a')
                second_url = a_tag['href'] if a_tag else None
                description = self.description(second_url) if second_url else None
                #organicStatus = self.organicStatus(second_url) if second_url else None
                star_rating = self.star_rating(second_url) if second_url else None

                row_values.append(description)
                #row_values.append(organicStatus)
                row_values.append(star_rating)
                
                self.data.append(row_values)   
            



    def description(self, url):   #additional web request needed to access a link within a link for description

        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=headers)
        html = urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        div_tag = soup.find('div', class_='entry')
        if div_tag:
            p_tags = div_tag.find_all('p', recursive=False)  # only gets the <p> tag for description
            if p_tags:  
                description = ' '.join([p.get_text(strip=True) for p in p_tags])
                return description
        return None
    '''
    def organicStatus(self, url):   #additional web request needed to access a link within a link for organicStatus for cereal

        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=headers)
        html = urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        span_tag = soup.find('span', id='cornucopia_scorecard_data_4', class_='cornucopia-edit')
        if span_tag:
            description = span_tag.get_text(strip=True)
            return description
        return None
    '''
    def star_rating(self, url):   #additional web request needed to access a link within a link for rating

        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=headers)
        html = urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        div_tag = soup.find('div', class_='scorecard-score-label')
        if div_tag:
            m = re.search(r'\d+', div_tag.get_text())
            if m:
                return m.group(0) 
            else:
                return None
        return None

    
    def cleaningTags(self):
    
        df = pd.DataFrame(self.data, columns=self.column_names + ['Description', 'StarRating'])

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
            f.write(self.newBrandIndicator)
            for row in self.df.fillna('NULL').values:
                row_values = list(row[:-1])  # Exclude the last item in the row
                last_value = row[-1] if row[-1] != 'NULL' else ''  # Last item or empty string
                writer.writerow(row_values + [last_value + self.newBrandIndicator])
    def run(self, outputPath, outputFileName):
        self.openlink()
        self.scrapingData()
        self.cleaningTags()
        df = self.pd_dataframe()      
        self.write_to_file(outputPath + "\\"+ outputFileName)
        print(df)
def main():
    eggUrl = 'https://www.cornucopia.org/scorecard/eggs/'
    eggOutputFileName = "EggScorecardsWebscrapedTextFile.txt"
    dairyUrl = 'https://www.cornucopia.org/scorecard/dairy/'
    dairyOutputFileName = "DairyScorecardsWebscrapedTextFile.txt"
    beefUrl = 'https://www.cornucopia.org/scorecard/organic-beef-scorecard/'
    beefOutputFileName = "BeefScorecardsWebscrapedTextFile.txt"
    poultryUrl = 'https://www.cornucopia.org/scorecard/organic-poultry-scorecard/'
    poultryFileName = "PoultryScorecardsWebscrapedTextFile.txt"
    yougurtUrl= 'https://www.cornucopia.org/scorecard/organic-yogurt-scorecard/'
    yogurtFileName = "YogurtScorecardsWebscrapedTextFile.txt"
    plantBasedBeveragesUrl = 'https://www.cornucopia.org/scorecard/plant-based-beverages/'
    plantBasedBeveragesOutputFileName = "PlantBasedBeveragesScorecardsWebscrapedTextFile.txt"
    snackbarUrl = 'https://www.cornucopia.org/scorecard/snack-bar-scorecard/'
    snackbarOutputFileName = "SnackBarScorecardsWebscrapedTextFile.txt"
    cottageCheeseUrl = 'https://www.cornucopia.org/scorecard/cottage-cheese/'
    cottageCheeseFileName = "CottageCheeseScorecardsWebscrapedTextFile.txt"
    cerealUrl = 'https://www.cornucopia.org/scorecard/cereal/'
    cerealFileName = "CerealScorecardsWebscrapedTextFile.txt"
    soyUrl = 'https://www.cornucopia.org/scorecard/soy/'
    soyOutputFileName = "SoyScorecardsWebscrapedTextFile.txt"
    outputPath = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir"
    

    delimeter = '|'
    newLineDelimeter = '^_'

    eggScorecardWebscrapeToTextFile = ScorecardData(eggUrl, delimeter, newLineDelimeter)
    dairyScorecardWebscrapeToTextFile = ScorecardData(dairyUrl, delimeter, newLineDelimeter)
    beefScorecardWebscrapeToTextFile = ScorecardData(beefUrl, delimeter, newLineDelimeter)
    poultryScorecardWebscrapeToTextFile = ScorecardData(poultryUrl, delimeter, newLineDelimeter)
    yogurtScorecardWebscrapeToTextFile = ScorecardData(yougurtUrl, delimeter, newLineDelimeter)
    plantBasedBeveragesScorecardWebscrapeToTextFile = ScorecardData(plantBasedBeveragesUrl, delimeter, newLineDelimeter)
    snackbarScorecardWebscrapeToTextFile = ScorecardData(snackbarUrl, delimeter, newLineDelimeter)
    cottageCheeseScorecardWebscrapeToTextFile = ScorecardData(cottageCheeseUrl, delimeter, newLineDelimeter)
    cerealScorecardWebscrapeToTextFile = ScorecardData(cerealUrl, delimeter, newLineDelimeter)
    soyScorecardWebscrapeToTextFile = ScorecardData(soyUrl, delimeter, newLineDelimeter)
    #eggScorecardWebscrapeToTextFile.run(outputPath, eggOutputFileName)
    #dairyScorecardWebscrapeToTextFile.run(outputPath, dairyOutputFileName)
    #beefScorecardWebscrapeToTextFile.run(outputPath, beefOutputFileName)
    #poultryScorecardWebscrapeToTextFile.run(outputPath, poultryFileName)
    #yogurtScorecardWebscrapeToTextFile.run(outputPath, yogurtFileName)
    #plantBasedBeveragesScorecardWebscrapeToTextFile.run(outputPath, plantBasedBeveragesOutputFileName)
    #snackbarScorecardWebscrapeToTextFile.run(outputPath, snackbarOutputFileName)
    #cottageCheeseScorecardWebscrapeToTextFile.run(outputPath, cottageCheeseFileName)
    #cerealScorecardWebscrapeToTextFile.run(outputPath, cerealFileName)
    #soyScorecardWebscrapeToTextFile.run(outputPath, soyOutputFileName)
main()   

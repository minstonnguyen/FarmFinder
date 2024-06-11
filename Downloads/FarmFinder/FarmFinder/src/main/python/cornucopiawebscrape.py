from urllib.request import Request, urlopen
from bs4 import BeautifulSoup # type: ignore
import re

class HTMLToFileScorecard:
    COLUMN_NAME_ARRAY = ['ScorecardID','ScorecardName']
    def __init__(self, url, outputDir, fileName): 
        #to do, check input parameters check if valid, check if directory exists, wrap all of this in a try catch
        self.url = url
        self.outputDir = outputDir
        self.fileName = fileName
    def run(self):
        link = self.url
        soup = self.__openlink(link)
        scorecard_list = scorecardScrapingData(soup)
        container = self.__scorecardTableCleaning(scorecard_list)
        self.__writeToTextFile(container, self.outputDir, self.fileName)
    def __openlink(self, site):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        req = Request(site, headers=headers)
        html = urlopen(req)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    def __scorecardTableCleaning(self,scorecard_list):
        cleaning = list(filter(lambda x: re.search(r'scorecard', x, re.IGNORECASE), scorecard_list))
        container = tuple(cleaning)
        return container
    def __writeToTextFile(self, container, outputDir, fileName): # needs a try catch finally, close in the finally
        fullQualifiedPath = outputDir + '/' + fileName
        finalTextFileOutput = open(fullQualifiedPath,"w")
        for item in HTMLToFileScorecard.COLUMN_NAME_ARRAY:
            finalTextFileOutput.write(item + ',')#solve edge case
        finalTextFileOutput.write('\n')
        for item in container:
            finalTextFileOutput.write(item + "\n")
        finalTextFileOutput.close() 
#opens the url and returns a soup object



#method 
def scorecardScrapingData(soup):

    scorecard_list = []
    class_tag = soup.find('main', {'class': 'main'})
    scorecards = class_tag.find_all('h3')
    for i in scorecards:
        scorecard_list.append(i.text) 
    return scorecard_list

#this method removes unneccessary scorecards


def main():
    link = "https://www.cornucopia.org/scorecards/"
    outputPath = "C:\\Users\\minston\\Downloads\\FarmFinder\\workingDir"
    outputFileName = "Test.txt"
    scorecardToTextFileInstance = HTMLToFileScorecard(link, outputPath, outputFileName)
    scorecardToTextFileInstance.run()
main()



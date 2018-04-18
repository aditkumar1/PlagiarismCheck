import requests
import urllib
import time

#This function send the query string to Faroo API to check plagiarism
def isPlagiarized(searchQuery):
    apikey='2CJIbhzsHU4nlSqBVZ2OP3fimb4_'
    searchUrl = 'http://www.faroo.com/api?'
    searchParameters={'q':'','start':1,'length':10,'kwic':'true','l':'en','src':'web','i':'true','f':'json','key':apikey}
    searchParameters['q']=searchQuery.lower()
    encodedURLParams= urllib.parse.urlencode(searchParameters)
    resp = requests.get(url=searchUrl, params=encodedURLParams)
    print(searchUrl+encodedURLParams)
    print(resp)
    data = resp.json()
    results= data['results']
    plagiarized=False
    for result in results:
        for key,value in result.items():
            if (key in'title') or (key in 'kwic') or (key in 'content'):
                if(searchQuery.lower() in value.lower()):
                    plagiarized=True
                    break;
    return plagiarized

#This function splits the document sequentially into substrings containing n words
def calculatePlagiarism(document,n):
    restrictedCharacters='/=():;'
    if(len(document)==0):
        return '0%'
    for char in restrictedCharacters:
        document = document.replace(char,"")
    document.replace('.',' ')
    noOfCharactersForDivision= n
    words = document.split()
    searchQueryStringList = []
    for i in range(0, len(words), noOfCharactersForDivision):
        searchQueryStringList.append(" ".join(words[i:i+noOfCharactersForDivision]))
    totalSearchQueryStrings= len(searchQueryStringList)
    plagiarizedCount=0
    for searchQuery in searchQueryStringList:
        if(isPlagiarized(searchQuery)):
            plagiarizedCount=plagiarizedCount+1
        time.sleep(1)
    plagiarizedPercent=(plagiarizedCount/totalSearchQueryStrings)*100
    return str(plagiarizedPercent)+'%'

def main():
    #This is a sample document
    doc='''Wikipedia was launched on January 15, 2001, by Jimmy Wales and Larry Sanger.[10] 
    Sanger coined its name,[11][12] a portmanteau of wiki[notes 3] and encyclopedia. 
    There was only the English-language version initially, but similar versions in other languages quickly developed, 
    which differ in content and in editing practices. With 5,615,178 articles,[notes 4] the 
    English Wikipedia is the largest of the more than 290 Wikipedia encyclopedias. Overall, 
    Wikipedia comprises more than 40 million articles in 299 different languages[14] and, as of February 2014, 
    it had 18 billion page views and nearly 500 million unique visitors each month'''
    print(calculatePlagiarism(doc,3))

if __name__ == "__main__":
    main()

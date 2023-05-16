import requests
from bs4 import BeautifulSoup

url_list = ["https://www.example.org/","https://www.example.com/"]

#the_word = input()


total_words = []
for url in url_list:
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content.lower(), 'lxml')
    words = soup.get_text().split(); 
    
    word_count = {};
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
        

    print('\nUrl: {}\ncontains {} of word: {}'.format(url, word_count, word))
    print(words)


#print(total_words)
total_count = len(total_words)


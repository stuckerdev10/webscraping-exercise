#!/usr/bin/env python
# coding: utf-8

# In[115]:


from bs4 import BeautifulSoup
import requests


# In[116]:


def getHTML(url):
    response = requests.get(url)
    return response.text


# In[121]:


html = getHTML("http://books.toscrape.com/catalogue/page-1index.html")


# In[120]:


soup = BeautifulSoup(html, 'html.parser')
print(soup)


# In[114]:


books = soup.find('ol', attrs = {'class': 'row'})


# In[ ]:





# In[123]:


book_url_list = []
book_data = []

for i in range(2, 51):
    
    html = getHTML("http://books.toscrape.com/catalogue/page-" + str(i) + ".html")
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.find('ol', attrs = {'class': 'row'})
    for book in books.find_all_next('article', attrs = {'class': 'product_pod'}):
        book_entry = {}

        title_dirty = book.find('h3').find('a').get('title')
        book_entry['Title'] = title_dirty

        rating_dirty = book.find('p')
        rating_list = rating_dirty.get('class')
        rating = rating_list[1]
        if rating == 'One':
            rating = 1
        elif rating == 'Two':
            rating = 2
        elif rating == 'Three':
            rating = 3
        elif rating == 'Four':
            rating = 4
        elif rating == 'Five':
            rating = 5
        book_entry['Rating'] = rating


        price = book.find('p', attrs = {'class': 'price_color'}).string[2:] #the index clears the symbols from the number
        book_entry['Price'] = price

        book_data.append(book_entry)


    print(book_data)   


# In[125]:


from csv import DictWriter

keys = book_data[0].keys()
with open('book_data.csv', 'w', encoding = 'utf-8') as csvfile:
    dictwriter = DictWriter(csvfile, keys)
    dictwriter.writeheader()
    dictwriter.writerows(book_data)


# In[ ]:





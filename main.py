from bs4 import BeautifulSoup
import json

data=[];

# Open the local HTML file and read its contents
with open('index.html', 'r', encoding="utf8") as file:
    html_content = file.read()

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

content_divs = soup.find_all('div', class_='collapse')

for div in content_divs:
    elem={'title':'','content':[] };
    title = div.find('div', class_='collapse-title')
    elem['title']=title.get_text()
    print(title.get_text())
    items = div.find_all('a')    
    print(elem)
    for index,item in enumerate(items):
        elem1={}
        content = item.find_all('p')        
        for index1,j in enumerate(content):
            # print(index,":",j.get_text())                             
            elem1['id']=index+1
            if index1 == 0:                       
                elem1['heading']=j.get_text()
            if index1 == 1:                       
                elem1['description']=j.get_text()
        print(elem1)
        elem['content'].append(elem1)

    if len(elem['content']) > 0:
        data.append(elem)

with open('my_file.json', 'w') as f:
    json.dump(data, f)
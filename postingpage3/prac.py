import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://prod.danawa.com/list/?cate=112758&15main_11_02',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select('div > div.prod_info > p > a')
image = soup.select('div > div.thumb_image > a.thumb_link') #href
price = soup.select('p.price_sect > a > strong')
spec = soup.select('div > div.prod_info > dl > dd > div')

print(spec)


#productItem16078997 > div > div.prod_info > dl > dd > div
#productItem16112300 > div > div.prod_info > dl > dd > div



#productInfoDetail_15986543 > p.price_sect > a > strong
#productInfoDetail_16112300 > p.price_sect > a > strong




#productItem15986543 > div > div.thumb_image > a.thumb_link
#productItem16112300 > div > div.thumb_image > a.thumb_link




#productItem16628417 > div > div.prod_info > p > a
    #adReaderProductItem15684065 > div > div.prod_info > p > a
    #adReaderProductItem16358381 > div > div.prod_info > p > a
    #productItem15986543 > div > div.prod_info > p > a
    #productItem16078997 > div > div.prod_info > p > a
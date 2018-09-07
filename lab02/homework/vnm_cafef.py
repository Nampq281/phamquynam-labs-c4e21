from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

raw_data = conn.read()

html_page = raw_data.decode("utf-8")
f_conn = open('vnm.html', 'wb')
f_conn.write (raw_data)
f_conn.close()

soup = BeautifulSoup(html_page, "html.parser")

#content
table = soup.find("table", {"id":"tableContent"})
tr_list = table.find_all("tr")

print(type(tr_list))
for tr in tr_list:
    td_list = tr.find_all("td")
    for td in td_list:
        content = td.string
        

data_list = []


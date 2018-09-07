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
table = soup.find("table", {"id":"tableContent"})
table_vnm = []
list_of_rows = []
for row in table.find_all('tr')[1:]:
    list_of_cells = []
    for cell in row.find_all('td'):
        text = cell.text.replace('&nbsp;','' )
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
table_vnm.append((list_of_rows, list_of_cells))
print(table_vnm)

#chua hoan thien

# pyexcel.save_as(records=table_vnm, dest_file_name= "vnm.xlsx")
# print("done")



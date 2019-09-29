from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver.get("https://101.qq.com/detail.shtml?ADTAG=cooperation.glzx.web&name=Darius&line=top")

page = driver.page_source
file = open('xinzhao.html','w',encoding='utf-8')
file.write(page)
file.close()
#print(page)
driver.get("http://www.baidu.com")
page = driver.page_source
newfile = open('baidu.html','w',encoding='utf-8')
newfile.write(page)
newfile.close()

driver.close()
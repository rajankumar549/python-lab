from bs4 import BeautifulSoup as Bs
from urllib import request as req
from lxml import html
#from xml import etree
import xml.etree.cElementTree as etree
import requests as r
from xml.dom.minidom import parseString
link="https://www.flipkart.com/search?q=nokia"
page=r.get(link)
html_string=page.content
document_root = html.fromstring(html_string)
print(etree.tostring(document_root, encoding='unicode'))
""""
print(html_string)
doc = parseString(html_string)
paragraph = doc.getElementsByTagName("p")[0]
content = paragraph.firstChild.data
print(content)"""


"""data=etree.XML(page[])
print(etree.tostring(data,pretty_print=True))
#buyers = data.xpath('body//html()')
print(etree.tostring(data))
#print(page)
# #soup=Bs(page.content)
#print(soup)"""


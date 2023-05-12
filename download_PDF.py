import urllib.request
import re

webpageName = "https://cs.nju.edu.cn/lwz/networks/index.htm"
webpage = urllib.request.urlopen(webpageName)

html = webpage.read().decode('utf-8')

print("Looking for links...")
findLink = re.compile(r'<a href="(.*?)">')
findpdf = re.compile(r'(.*?\.pdf)')
L = re.findall(findLink, html)

pdfLinks = []
for l in L:
    t = re.findall(findpdf, l)
    if len(t) == 1:
        t[0] = t[0].replace(" ", "%20")
        pdfLinks.append(t[0])

print(pdfLinks)

savePath = "out"

urlPath = "https://cs.nju.edu.cn/lwz/networks/"

for i in pdfLinks:
    try:
        urllib.request.urlretrieve(urlPath + i, savePath + "/" + i)
    except:
        print("fail to download " + i)

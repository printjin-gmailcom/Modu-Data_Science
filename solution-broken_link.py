import urllib.request, urllib.parse
import bs4 as BeautifulSoup

# 사용자와 인터넷에게 말을 건다.
base = input("Enter the URL: ")
try:
    page = urllib.request.urlopen(base)
except:
    print("Cannot open %s" % base)
    quit()

# soup을 준비한다.
soup = BeautifulSoup.BeautifulSoup(page)

# link를 (name, url)로 구성된 tuple로 추출한다.
links = [(link.string, link["href"]) 
         for link in soup.find_all("a")
         if link.has_attr("href")]

# 각 링크를 연다.
broken = False
for name, url in links:
    # base와 대상 link를 결합한다.
    dest = urllib.parse.urljoin(base, url)
    try:
        page = urllib.request.urlopen(dest)
        page.close()
    except:
        print("Link \"%s\" to \"%s\" is probably broken." % (name, dest))
        broken = True

# 좋은 소식!
if not broken:
    print("Page %s does not seem to have broken links." % base)
        

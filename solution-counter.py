import urllib.request, re
from collections import Counter

# 사용자와 인터넷에게 말을 걸자.
url = input("Enter the URL: ")
try:
    page = urllib.request.urlopen(url)
except:
    print("Cannot open %s" % url)
    quit()

# 페이지를 읽고 부분적으로 정규화한다.
doc = page.read().decode().lower()

# 텍스트를 단어로 자른다.
words = re.findall(r"\w+", doc)

# 카운터를 만들고 답을 출력한다.
print(Counter(words).most_common(10))

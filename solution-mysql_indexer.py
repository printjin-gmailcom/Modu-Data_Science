import nltk, pymysql

infilename = input("Enter the name of the file to index: ")

# 여러분의 MySQL 설정에 맞게 아래 라인을 수정하라.
conn = pymysql.connect(user="dsuser", passwd="badpassw0rd", db="dsbd")
cur = conn.cursor()

QUERY = "INSERT INTO indexer (word,position,pos) VALUES "
wpt = nltk.WordPunctTokenizer()

offset = 1
with open(infilename) as infile:
    # 텍스트를 한줄 한줄씩 점진적으로 처리하자.
    # 어차피 한 단어가 두 줄에 걸쳐 있지는 않다! 
    for text in infile:
        # 단어를 토큰화하고 품사 태그를 붙인다.
        pieces = enumerate(nltk.pos_tag(wpt.tokenize(text)))
        
        # 쿼리를 만든다. 이스케이프 문자 처리하는 것을 잊지 말자! 
        words = ["(\"%s\",%d,\"%s\")" % (conn.escape_string(w), 
                                         i + offset, 
                                         conn.escape_string(pos)) 
                 for (i, (w, pos)) in pieces]
        
        # 쿼리를 실행한다.
        if words:
            cur.execute(QUERY + ','.join(words))

            # 단어 포인터를 업데이트한다.
            offset += len(words)

# 변경사항을 등록한다.
conn.commit()
conn.close()

import glob
from wordcloud import WordCloud
from wordcloud import STOPWORDS

stopwords = set(STOPWORDS)
stopwords.add("know")
stopwords.add("one")

# alice.txt, dostoevky.txt, constiution.txt. 만 선택
for file in glob.glob("*.txt"):
    texts = ''
    print(file)
    print("*" * 50)
    f = open(file)
    text = f.read()  
    print(text[:200])  
    print("-" * 50)
    texts += text  
    f.close()
    


wc = WordCloud(stopwords=stopwords).generate(texts) 

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
plt.imshow(wc)
plt.axis("off")
plt.show()

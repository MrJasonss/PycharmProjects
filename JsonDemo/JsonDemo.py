import json
import re
import jieba
import pandas as pd



f = open("poet.song.100000.json", encoding='utf-8')
result = json.load(f)

eachCommentList = [];
for item in result:
    if item is not None:
        eachCommentList.append(item)
    # print(eachCommentList)
comments = ''
for k in range(len(eachCommentList)):
    comments = comments+(str(eachCommentList[k]).strip())

pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comments = ''.join(filterdata)

segment = jieba.lcut(cleaned_comments)
words_df=pd.DataFrame({'segment':segment})

stopwords=pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')#quoting=3全不引用
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]







# encoding: utf-8
from gensim.models import word2vec

model = word2vec.Word2Vec.load("./book.model")
#
posit= u"時代"
#print(model.__dict__['wv'][ posit ])
print("posit=", posit)
results = model.wv.most_similar(positive=[posit], topn=10 )
for result in results:
    print(result)

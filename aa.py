import gensim
import numpy as np
import textract
from nltk import word_tokenize
def file_sim(path1,path2):

    def open_docx(path_to_docx):
        text = textract.process(path_to_docx)
        text1 = text.decode("utf-8").lower()
        text1=text1.split('\n')
        return text1

    def delete_symbol(text1,sym):
        for i in range(len(text1)):
            str_words=text1[i].split()
            for j in str_words:
                #print(j)
                if j.count(sym):
                    for char in sym:
                        str_words.replace(char,"")
            text1[i]=' '.join(str_words)
        return text1
    def edit_symbol(text0,last,new):
        for i in range(len(text0)):
            str_words = text0[i].split()
            for j in range(len(str_words)):
                str_words[j] = str_words[j].replace(last, new)
            text0[i] = ' '.join(str_words)

    def max_word(text):
        arr = []
        s2 = 0
        for i in text:
            s2 += len(i.split())
        arr.append(s2)
        arr.append(text)
        return arr

    def obraborka(text):
        delete_symbol(text,'\t')
        edit_symbol(text,'ё','е')
    def replace_x(text) :
        for i in range(len(text)):
            for j in range(len(text0)):
                if text[i].replace(' ','') == text[j].replace(' ',''):
                    text[i]=''
        text = [x for x in text if x != '']
        return text

    def simmiliarity(text1,text2):
        if max_word(text1)[0]>max_word(text2)[0]:
            text_max,text_min=max_word(text1)[1],max_word(text2)[1]
        else:
            text_max, text_min = max_word(text2)[1], max_word(text1)[1]

        docs=[[w.lower() for w in word_tokenize(s)]
              for s in text_max ]
        dictionary = gensim.corpora.Dictionary(docs)

        corpus = [dictionary.doc2bow(do) for do in docs]


        tf_idf = gensim.models.TfidfModel(corpus)

        arr_simmiliarity_sentence=[]
        for j  in range(len(text_min)):
            sims = gensim.similarities.Similarity('C:/Similiarity/sims', tf_idf[corpus],
                                                  num_features=len(dictionary))
            query_sentence=[w.lower() for w in word_tokenize(text_min[j])]
            query_sentence_bow = dictionary.doc2bow(query_sentence)
            query_sentence_tf_idf = tf_idf[query_sentence_bow]
            sims=sims[query_sentence_tf_idf]
            arr_simmiliarity_sentence.append(max(sims))

        return np.mean(arr_simmiliarity_sentence)

    global text0
    text0=open_docx('C:/Users/Alex/PycharmProjects/untitled3/titul.docx')
    text1=open_docx(path1)
    text2=open_docx(path2)


    obraborka(text0)
    obraborka(text1)
    replace_x(text1)
    obraborka(text2)
    replace_x(text2)
    text1 = [x for x in text1 if x != '']
    text2 = [x for x in text2 if x != '']

    return simmiliarity(text1,text2)




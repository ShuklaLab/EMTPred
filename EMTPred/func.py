import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# function to convert sequence strings into k-mer words, default size = 5 (pentamer words)
def getKmers(sequence, size=5):
    return [sequence[x:x+size].lower() for x in range(len(sequence) - size + 1)]

#Processing file
def getSeq(file):
    fh=open(file)
    myfile=fh.readlines()
    fh.close()
    seq=[]
    for i in range(1,len(myfile),2):
        seq.append(myfile[i].strip())
    return seq

def EMTPred(file):
    rnaseq = pd.read_table('rnaseq.tab')
    hairpin = pd.read_table('hairpin.tab')
    df_hairpin=pd.merge(hairpin, rnaseq)
    hairpin_data=df_hairpin[['seq_hairpin','sig']]
    hairpin_data.columns = ['sequence','class']
    hairpin_data['words'] = hairpin_data.apply(lambda x: getKmers(x['sequence'], 5), axis=1)
    hairpin_data = hairpin_data.drop('sequence', axis=1)
    hairpin_texts = list(hairpin_data['words'])
    for item in range(len(hairpin_texts)):
        hairpin_texts[item] = ' '.join(hairpin_texts[item])
    y_data = hairpin_data.iloc[:, 0].values  
    cv = CountVectorizer(ngram_range=(3,3))
    ngram_X = cv.fit_transform(hairpin_texts)
    mdl=LogisticRegression().fit(ngram_X, y_data)
    cv = CountVectorizer(ngram_range=(3,3))
    ngram_X = cv.fit_transform(hairpin_texts)
    mdl=LogisticRegression().fit(ngram_X, y_data)
    
    seq=getSeq(file)
    df=pd.DataFrame(seq)
    df['words'] = hsa.apply(lambda x: getKmers(x['seq'], 5), axis=1)
    df = df.drop('seq', axis=1)
    df_texts = list(df['words'])
    for item in range(len(df_texts)):
        df_texts[item] = ' '.join(df_texts[item])
    ngram_df = cv.transform(df_texts)
    predictions = mdl.predict(ngram_hsa)
    return(predictions)
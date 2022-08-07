from finbert.finbert import predict
from transformers import AutoModelForSequenceClassification
import argparse
import os
import csv
lst = []
i = 2

def prediction(path,filename):
    with open(path,'r') as f:
    	text = f.read()
    model = AutoModelForSequenceClassification.from_pretrained('/home/oussama/Bureau/Sentiments_analyses/models/classifier_model/finbert-sentiment',num_labels=3,cache_dir=None)
    output = filename[0:len(filename)-3]+'csv'
    predict(text,model,write_to_csv=True,path=os.path.join('/home/oussama/Bureau/Sentiments_analyses/output/',output))
    ch1='/home/oussama/Bureau/Sentiments_analyses/output/'+output
    ff= open (ch1,'r')
    myReader = csv.reader(ff)
    
    
    return myReader

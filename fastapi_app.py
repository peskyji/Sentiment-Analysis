from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import pickle
from nltk.stem import PorterStemmer
import pandas as pd
import re
import json
import joblib

# create an object of FastAPI
app = FastAPI()

# create objects to receive input from client
class Input(BaseModel):
    reviews : str = None

# create route for index page
@app.get("/")
def homepage():
    # print("Hi this is index page")
    return {'a':'b'}

# create another route for calculation
def load_models():
    tfidf, lr, xgb, cnb = None, None, None, None
    try:
        tfidf =  joblib.load('Models/tfidf.joblib')
        print(tfidf)
    except Exception as exp:
        print(f"problem in loading tfidf - {str(exp)}")
    try:
        lr =  joblib.load('Models/lr.joblib')
        print(lr)
    except Exception as exp:
        print(f"problem in loading lr - {str(exp)}")
    try:
        xgb =  joblib.load('Models/xgb.joblib')
        print(xgb)
    except Exception as exp:
        print(f"problem in loading xgb - {str(exp)}")
    try:
        cnb =  joblib.load('Models/cnb.joblib')
        print(cnb)
    except Exception as exp:
        print(f"problem in loading cnb - {str(exp)}")
    
    return tfidf, lr, xgb, cnb

def preprocessing_task(review):
    ps = PorterStemmer()
    review = re.sub(r'[^A-Za-z\s]', '', review)
    print("Special Characters removed from review")
    review = re.sub(r' +', ' ', review)
    print("extra spaces removed")
    review = review.lower()
    print("Word Stemming stated...")
    review = " ".join([ps.stem(word) for word in review.split()])
    print("Stemming Completed")
    return review



@app.post("/predict")
async def prediction(data:Input):
    data = dict(data)
    print(data)
    tfidf, lr, xgb, cnb = load_models()
    print("models loaded")
    try:
        review = preprocessing_task(data['reviews'])
    except Exception as exp:
        print(f"problem in preprocessing - {str(exp)}")
    try:
        X =  tfidf.transform(pd.Series(review))
        print("vector created")
    except Exception as exp:
        print(f"problem in transforming to tfidif vectors - {str(exp)}")
        # print("vector created")
    try:
        lr_prob =  lr.predict_proba(X)[0]
    except Exception as exp:
        print(f"problem lr prediction - {str(exp)}")
    try:
        xgb_prob =  xgb.predict_proba(X)[0]
    except Exception as exp:
        print(f"problem xgb prediction - {str(exp)}")
    try:
        cnb_prob =  cnb.predict_proba(X)[0]
    except Exception as exp:
        print(f"problem cnb prediction - {str(exp)}")
    try:
        prob = {
                    'lr':[float(lr_prob[0]), float(lr_prob[1])], 
                    'xgb':[float(xgb_prob[0]), float(xgb_prob[1])],
                    'cnb':[float(cnb_prob[0]), float(cnb_prob[1])]
                }
        print(prob)
    except Exception as exp:
        print(f"problem in forming return response message - {str(exp)}")
    # return {'success':'True'}
    return json.dumps(prob)




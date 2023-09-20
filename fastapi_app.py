from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from nltk.stem import PorterStemmer
import pandas as pd
import re
import json

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

def preprocessing_task(review):
    ps = PorterStemmer()
    review = re.sub(r'[^A-Za-z\s]', '', review)
    # print("Special Characters removed from review")
    review = re.sub(r' +', ' ', review)
    # print("extra spaces removed")
    review = review.lower()
    # print("Word Stemming stated...")
    review = " ".join([ps.stem(word) for word in review.split()])
    # print("Stemming Completed")
    return review

@app.post("/predict")
async def prediction(data:Input):
    data = dict(data)
    print(data)
    print(type(data))
    # try:
    #     tfidf = pickle.load(open('Models/tfidf.pkl', 'rb'))
    # except:
    #     print("problem in loading tfidf")
    # try:
    #     lr = pickle.load(open('Models/lr.pkl', 'rb'))
    # except:
    #     print("problem in loading lr")
    # try:
    #     xgb = pickle.load(open('Models/xgb.pkl', 'rb'))
    # except:
    #     print("problem in loading xgb")
    # try:
    #     cnb = pickle.load(open('Models/cnb.pkl', 'rb'))
    # except:
    #     print("problem in loading cnb")
    # try:
    #     review = preprocessing_task(data['reviews'])
    # except:
    #     print("problem in preprocessing")
    # try:
    #     X = tfidf.transform(pd.Series(review))
    # except:
    #     print("problem in transforming to tfidif vectors")
    # # print("vector created")
    # try:
    #     lr_prob = lr.predict_proba(X)[0]
    # except:
    #     print("problem lr prediction")
    # try:
    #     xgb_prob = xgb.predict_proba(X)[0]
    # except:
    #     print("problem xgb prediction")
    # try:
    #     cnb_prob = cnb.predict_proba(X)[0]
    # except:
    #     print("problem cnb prediction")
    # try:
    #     prob = {
    #                 'lr':[float(lr_prob[0]), float(lr_prob[1])], 
    #                 'xgb':[float(xgb_prob[0]), float(xgb_prob[1])],
    #                 'cnb':[float(cnb_prob[0]), float(cnb_prob[1])]
    #             }
    #     print(prob)
    # except:
    #     print("problem in forming return response message")
    return {'success':'True'}
    # return json.dumps(prob)




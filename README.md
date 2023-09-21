# Sentiment Analyzer for Movie Reviews
[![Site](https://img.shields.io/static/v1?label=visit%20Website&message=Movie%20Counsel%20Page&color=yellow)](https://movie-counsel.streamlit.app)
[![Linkedin](https://img.shields.io/static/v1?label=visit&message=My%20Linkedin%20Page&color=blue&logo=linkedin)](https://www.linkedin.com/in/shailesh-bisht-b42a73184/)
[![Hosted-on](https://img.shields.io/static/v1?label=API%20hosted%20on&message=Render&color=orange&logo=render)](https://render.com/)
[![python](https://img.shields.io/static/v1?label=Python&message=%3E=3.9&color=brown&logo=python)]()
[![Sentiment](https://img.shields.io/static/v1?label=Sentiment&message=Analysis&color=purple&logo=python)]()
<br>

## Overview

Sentiment Analyzer for Movie Reviews is a comprehensive tool designed to evaluate the sentiment of movie reviews. This project is an integral part of the [Movie Counsel](https://movie-counsel.streamlit.app) web application, which empowers users to explore and discover movies tailored to their preferences.

**Key Features:**

- Sentiment Analyzer is implemented as a robust API using the FastAPI framework.
- The API is hosted on the Render cloud platform, ensuring scalability, reliability, and ease of deployment.
- Sentiment analysis models are trained on a vast dataset comprising approximately 180,000 movie reviews sourced from IMDB.
- The reviews are scrapped from IMDB for both Hollywood and Bollywood releases from 2019 to September 2023 with help of Beautiful Soup.

## Data Preprocessing

The heart of any sentiment analysis model is the quality of its training data. Therefore, the dataset undergoes a rigorous preprocessing phase to optimize its quality for analysis.

**Data Cleaning and Preprocessing Tasks Include:**

- Correcting data formats to ensure uniformity and consistency with help of Pandas.
- Assigning review labels, i.e., classifying reviews as positive or negative based on the accompanying ratings.
- Removing special characters and symbols from the text, facilitating more accurate sentiment analysis.
- Applying word stemming techniques to further enhance the quality of the text data with help of nltk.
- visit the Google Colab notebooks in this [📁](https://drive.google.com/drive/folders/11Cm5Co2d-X9SrE8r7ANPu4-as3F_ik5Q?usp=drive_link) for detailed analysis.

## Model Building

Sentiment Analyzer leverages state-of-the-art machine learning algorithms to create an accurate and robust sentiment classification model.

**Model Building Highlights:**

- Combination of machine learning algorithms, including Logistic Regression, Complement Naive Bayes, and XGBoost, to achieve precise sentiment classification.
- Incorporation of pretrained models such as roBERTa to expedite the training process and enhance overall performance.
- Continuous model evaluation and refinement to ensure the highest level of sentiment analysis accuracy.
- visit the Google Colab notebooks in this [📁](https://drive.google.com/drive/folders/11Cm5Co2d-X9SrE8r7ANPu4-as3F_ik5Q?usp=drive_link) for detailed analysis.

## Web API

To make sentiment analysis accessible and user-friendly, Sentiment Analyzer provides a comprehensive web API. Users can interact with the API to gain insights into the sentiment of movie reviews.

**Key API Features:**

- Accepts HTTP POST requests containing movie reviews as input.
- Returns the probability of both negative and positive sentiments predicted by each model.
- Enables users to integrate sentiment analysis capabilities into their own applications and projects.

- Request
```
{
  "reviews": "This movie was absolutely fantastic! I loved every moment of it."
}
```
- Response - model:[negative score, positive score]
```
{
    "logistic_regression": {[0.15, 0.85]},
    "complement_naive_bayes": {[0.18, 0.82]},
    "xgboost": {[0.13, 0.87]}
}
```
## Installation
To set up and use Sentiment Analyzer in your own project, follow these steps:

- Clone this repository to your local machine.
```
    git clone https://github.com/peskyji/Sentiment-Analysis.git
```
- Install the required dependencies for python 3.8 or above.
```
    pip install -r requirements.txt
```
- Run the FastAPI application
```
uvicorn fastapi_app:app --reload
```
- Visit FastAPI [documentation](https://fastapi.tiangolo.com/) for more details

<br>

## Acknowledgments
I would like to express my gratitude to the open-source community and the developers of FastAPI for their invaluable contributions.

Happy sentiment analyzing!


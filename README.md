# Medical Insurance Price Prediction

The increasing costs and complexities in the healthcare sector underscore the necessity for efficient predictive models to anticipate medical insurance prices. This project explores the application of machine learning techniques for forecasting medical insurance premiums, aiming to provide stakeholders with invaluable insights for pricing strategies and risk management.


## About Dataset:
The dataset includes information about individuals, such as:
- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region
- Medical charges

Download Dataset: [Download](https://www.kaggle.com/datasets/mirichoi0218/insurance)
## Insights:


- Exploring the dataset
- EDA
- Data Visualization 
- Detecting and removing outliers
- Encoding
- Prediction using Linear Regression
- Prediction using SVR (Use of Standard Scalar)
- Prediction using Gradient Boosting Regressor
- Prediction using Random Forest Regressor
- Performing Hyper tuning for above mentioned models
- Feature Importance
- Preparing model for deployment
- Deployed model using Flask
## Results:

### Comparing Models

|Model |  Train_Accuracy  | Test_Accuracy|CV Score|
|:-----|:--------:|------:|-------:|
| Linear Regression | 0.73 | 0.79 | 0.74|
| SVR  |-0.090   | -0.084   |-0.098
| Random Forest Regressor |0.92  |0.88    |0.84
| Gradient Boosting Regressor | 0.871| 0.891  |0.860
| XGB Regressor | 0.867 | 0.895  |0.862

From the above table we can observe that XGBoost Regressor is the best model with cv score 0.862.

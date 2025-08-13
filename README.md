# Medical Insurance Price Prediction

The increasing costs and complexities in the healthcare sector underscore the necessity for efficient predictive models to anticipate medical insurance prices. This project explores the application of machine learning techniques for forecasting medical insurance premiums, aiming to provide stakeholders with invaluable insights for pricing strategies and risk management.


<img width="1000" height="800"  src="https://github.com/Nikhil2818/Medical-Insurance-Cost-Prediction/blob/main/Screenshot%20(174).png" />


## About Dataset:
The dataset includes information about individuals, such as:
- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region
- Medical charges

Download Dataset: [Download](https://www.kaggle.com/datasets/harishkumardatalab/medical-insurance-price-prediction)
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

  <img width="800" height="800"  src="https://github.com/Nikhil2818/Medical-Insurance-Cost-Prediction/blob/main/Screenshot%20(175).png" />
## Results:

### Comparing Models

|Model |  Train_Accuracy  | Test_Accuracy|CV Score|
|:-----|:--------:|------:|-------:|
| Linear Regression | 0.74 | 0.77 | 0.74|
| SVR  |-0.090   | -0.05   |-0.09
| Random Forest Regressor |0.99  |0.95    |0.97
| Gradient Boosting Regressor | 0.996| 0.956  |0.992
| XGB Regressor | 0.996 | 0.961  |0.993

From the above table we can observe that XGBoost Regressor is the best model with cv score 0.993.

Medical Insurance Price Predictor: [Click here](https://medical-insurance-cost-prediction-2.onrender.com)

<img width="1000" height="800"  src="https://github.com/Nikhil2818/Medical-Insurance-Cost-Prediction/blob/main/Screenshot%20(172).png" />

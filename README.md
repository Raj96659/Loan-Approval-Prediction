# Loan Approval Prediction Using Machine Learning

## 1. Introduction

<p>Loans are an essential part of modern life, helping individuals manage education, housing, and other expenses. 
Banks need to ensure that loans are granted to eligible applicants while minimizing defaults. Traditionally, this process is manual and time-consuming. 
This project uses Machine Learning to automate loan approval prediction based on applicant data.</p>

## 2. Objective

<li>Predict whether a loan applicant will be approved or not.</li>
<li>Reduce manual decision-making for banks.</li>
<li>Identify key factors that affect loan approval, such as income, credit history, education, and property area.</li>

## 3. Dataset

<l1>Source: Encoded_Loan_Data.csv (preprocessed with encoded categorical features).</l1>
<li>Features:</li>

Feature	               Description
Gender_Encode	        Male=1, Female=0
Married_Encode	      Yes=1, No=0
Dependents	          Number of dependents
Education_Encode	    Graduate=1, Not Graduate=0
Self_Employed_Encode	Yes=1, No=0
ApplicantIncome	      Applicant’s income
CoapplicantIncome	    Co-applicant’s income
LoanAmount	          Loan amount requested
Loan_Amount_Term	    Term in months
Credit_History	      1=Good, 0=Bad
Property_Area_Encode	Rural=0, Semiurban=1, Urban=2
Loan_Status_Encode	  Approved=1, Not Approved=0

Dataset contains encoded features for Machine Learning.

4. Data Preprocessing

Missing values handled using appropriate imputation.

Outliers identified using boxplots and handled if necessary.

Categorical variables encoded (Label/Ordinal Encoding).

Numeric variables scaled using MinMaxScaler for better model performance.

5. Exploratory Data Analysis (EDA)

Univariate Analysis: Distribution of individual features using histograms and countplots.

Bivariate Analysis: Scatterplots and correlation matrices to see relationships between features and target.

Observations:

Credit History and ApplicantIncome have strong impact on loan approval.

Property Area shows some variation in approvals across regions.

6. Model Selection

Four models were trained and evaluated on the dataset:

Model	Training Accuracy	Test Accuracy	F1-Score	Recall
Logistic Regression	81.34%	79.44%	86.74%	97.58%
KNN	79.43%	75.56%	84.29%	95.16%
SVM	82.06%	80.00%	87.05%	97.58%
Random Forest	81.35%	79.44%	86.74%	97.58%

Observations:

All models performed reasonably well.

SVM had slightly higher test accuracy, but Logistic Regression was chosen for deployment due to interpretability, simplicity, and high recall, which is important for approving eligible applicants.

7. Model Training

Selected Model: Logistic Regression

Train-Test Split: 70%-30%

Scaling: MinMaxScaler on numeric features.

Final Evaluation Metrics on Test Data:

Accuracy: 79.44%

Precision: 78.06%

Recall: 97.58%

F1-score: 86.74%

Pickled Model: Saved as logistic.pkl for deployment.

Pickled Scaler: Saved as log_scale.pkl.

8. Deployment (Streamlit App)

Interactive app allows user input for all features.

Automatically encodes categorical features and scales numeric features.

Predicts loan approval using the trained Logistic Regression model.

Displays Loan Approved / Not Approved with a simple interface.

9. Conclusion

Machine Learning can efficiently predict loan approvals using applicant data.

Logistic Regression provides a balance between performance and interpretability.

High Recall ensures most eligible applicants are correctly approved, reducing manual errors.

The deployed Streamlit app allows banks or users to easily test loan eligibility.

10. Future Work

Include more features like debt-to-income ratio, past defaults, or property value.

Explore ensemble methods to further improve accuracy.

Use real-time deployment with database integration.

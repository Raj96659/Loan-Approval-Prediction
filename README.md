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

## 4. Data Preprocessing

<li>Missing values handled using appropriate imputation.</li>
<li>Outliers identified using boxplots and handled if necessary.</li>
<li>Categorical variables encoded (Label/Ordinal Encoding).</li>
<li>Numeric variables scaled using MinMaxScaler for better model performance.</li>

## 5. Exploratory Data Analysis (EDA)

<li>Univariate Analysis: Distribution of individual features using histograms and countplots.</li>
<li>Bivariate Analysis: Scatterplots and correlation matrices to see relationships between features and target.</li>

<h5>Observations:</h5>

<li>Credit History and ApplicantIncome have strong impact on loan approval.</li>
<li>Property Area shows some variation in approvals across regions.</li>

## 6. Model Selection

<h5>Four models were trained and evaluated on the dataset:</h5>

<p>Observations:</p>

<p>All models performed reasonably well.
SVM had slightly higher test accuracy, but Logistic Regression was chosen for deployment due to interpretability, simplicity, and high recall, which is important for approving eligible applicants.</p>

## 7. Model Training

<li>Selected Model: Logistic Regression</li>

<li>Train-Test Split: 70%-30%</li>

<li>Scaling: MinMaxScaler on numeric features.</li>

<li>Final Evaluation Metrics on Test Data:</li>
<li>Accuracy: 79.44%</li>
<li>Precision: 78.06%</li>
<li>Recall: 97.58%</li>
<li>F1-score: 86.74%</li>
<li>Pickled Model: Saved as logistic.pkl for deployment.</li>
<li>Pickled Scaler: Saved as log_scale.pkl.</li>

## 8. Deployment (Streamlit App)

<li>Interactive app allows user input for all features.</li>
<li>Automatically encodes categorical features and scales numeric features.</li>
<li>Predicts loan approval using the trained Logistic Regression model.</li>
<li>Displays Loan Approved / Not Approved with a simple interface.</li>

## 9. Conclusion

<li>Machine Learning can efficiently predict loan approvals using applicant data.</li>
<li>Logistic Regression provides a balance between performance and interpretability.</li>
<li>High Recall ensures most eligible applicants are correctly approved, reducing manual errors.</li>
<li>The deployed Streamlit app allows banks or users to easily test loan eligibility.</li>

## 10. Future Work

<li>Include more features like debt-to-income ratio, past defaults, or property value.</li>
<li>Explore ensemble methods to further improve accuracy.</li>
<li>Use real-time deployment with database integration.</li>

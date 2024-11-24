import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score
from sklearn.preprocessing import PowerTransformer, RobustScaler
from sklearn.ensemble import StackingRegressor, GradientBoostingRegressor
from sklearn.linear_model import HuberRegressor
from sklearn import metrics
from xgboost import XGBRegressor
from sklearn.svm import SVR

# Load and preprocess data
df = pd.read_csv('C:\\Users\\venka\\OneDrive\\Documents\\GitHub\\Projects\\Air Quality Prediction\\Air-Quality-Prediction\\Data\\Real-Data\\Real_Combine.csv')
df_processed = df.copy()

# Handle missing values
for column in df_processed.columns:
    if df_processed[column].dtype in ['int64', 'float64']:
        df_processed[column] = df_processed[column].fillna(df_processed[column].median())
    else:
        df_processed[column] = df_processed[column].fillna(df_processed[column].mode()[0])

# Feature Engineering
X = df_processed.iloc[:, :-1]
Y = df_processed.iloc[:, -1]

# Enhanced feature engineering based on previous importance analysis
X['VV_squared'] = X['VV'] ** 2
X['SLP_VV'] = X['SLP'] * X['VV']
X['T_VV'] = X['T'] * X['VV']
X['Tm_squared'] = X['Tm'] ** 2
X['H_VV'] = X['H'] * X['VV']  # New interaction
X['T_H'] = X['T'] * X['H']    # New interaction
X['VV_cube'] = X['VV'] ** 3   # New polynomial feature

# Handle outliers with RobustScaler
robust_scaler = RobustScaler()
X_robust = robust_scaler.fit_transform(X)
X_robust = pd.DataFrame(X_robust, columns=X.columns)

# Train-test split
y_quartiles = pd.qcut(Y, q=4, labels=False)
X_train, X_test, y_train, y_test = train_test_split(
    X_robust, Y, test_size=0.2, random_state=42, stratify=y_quartiles
)

# Define base models
xgb1 = XGBRegressor(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.03,
    subsample=0.9,
    colsample_bytree=0.9,
    reg_alpha=0.1,
    reg_lambda=0.1,
    random_state=42
)

xgb2 = XGBRegressor(
    n_estimators=300,
    max_depth=3,
    learning_rate=0.02,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.15,
    reg_lambda=0.15,
    random_state=43
)

gbr = GradientBoostingRegressor(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.03,
    subsample=0.8,
    random_state=44
)

# Define meta-regressor
meta_regressor = HuberRegressor(epsilon=1.35)

# Create stacking ensemble
estimators = [
    ('xgb1', xgb1),
    ('xgb2', xgb2),
    ('gbr', gbr)
]

stack = StackingRegressor(
    estimators=estimators,
    final_estimator=meta_regressor,
    cv=5
)

# Fit the ensemble
stack.fit(X_train, y_train)

# Make predictions
predictions = stack.predict(X_test)

# Model evaluation
mae = metrics.mean_absolute_error(y_test, predictions)
mse = metrics.mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = metrics.r2_score(y_test, predictions)

# Print metrics
print("Model Performance Metrics:")
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")

# Individual model performance
models = {'XGBoost1': xgb1, 'XGBoost2': xgb2, 'GradientBoosting': gbr}
for name, model in models.items():
    model.fit(X_train, y_train)
    model_pred = model.predict(X_test)
    model_r2 = metrics.r2_score(y_test, model_pred)
    print(f"\n{name} R²: {model_r2:.3f}")
    
# Cross-validation for ensemble
cv_scores = cross_val_score(stack, X_train, y_train, cv=5, scoring='r2')
print("\nEnsemble Cross-validation R² scores:", cv_scores)
print(f"Average CV R² score: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

# Visualizations
plt.figure(figsize=(20, 10))

# Plot 1: Actual vs Predicted
plt.subplot(2, 3, 1)
plt.scatter(y_test, predictions, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
         color='red', linestyle='--')
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted (Ensemble)")

# Plot 2: Residuals
residuals = y_test - predictions
plt.subplot(2, 3, 2)
plt.scatter(predictions, residuals, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel("Predicted")
plt.ylabel("Residuals")
plt.title("Residual Plot")

# Plot 3: Error Distribution
plt.subplot(2, 3, 3)
sns.histplot(residuals, kde=True)
plt.title("Prediction Error Distribution")
plt.xlabel("Prediction Error")

# Plot 4: Model Comparison
plt.subplot(2, 3, 4)
model_names = ['XGBoost1', 'XGBoost2', 'GradientBoosting', 'Ensemble']
model_scores = []
for name, model in models.items():
    model_scores.append(metrics.r2_score(y_test, model.predict(X_test)))
model_scores.append(r2)
plt.bar(model_names, model_scores)
plt.title("Model Performance Comparison")
plt.xticks(rotation=45)
plt.ylabel("R² Score")

# Save the model
with open('ensemble_model.pkl', 'wb') as file:
    pickle.dump({
        'model': stack,
        'scaler': robust_scaler,
        'feature_names': X.columns.tolist()
    }, file)

plt.tight_layout()
plt.show()

# Feature importance analysis (from XGBoost1 as representative)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': xgb1.feature_importances_
})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("\nTop 15 Feature Importance:")
print(feature_importance.head(15))
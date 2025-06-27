# 📦 Amazon Delivery Time Prediction

An end-to-end **machine learning system** to predict **Amazon delivery times** based on features such as traffic, location, time, and product category. Includes an interactive Streamlit UI for real-time predictions and MLflow tracking for model management.

---
## Demo ScreebShot

![Picture](https://github.com/Manav2507/Amazon-Delivery-Time-Prediction/blob/main/4_1.png)
![Picture](https://github.com/Manav2507/Amazon-Delivery-Time-Prediction/blob/main/4_2.png)

## 🧠 Domain
**E-Commerce & Logistics**  
Use AI to streamline deliveries, optimize agent performance, and improve customer satisfaction.

---

## 🎯 Problem Statement

Delivery time estimation is critical to the logistics and customer experience in e-commerce. This project builds predictive models that estimate delivery durations based on order, agent, traffic, and weather conditions.

---

## 🚀 Project Highlights

### ✅ Business Use Cases

- 📍 **Delivery Route Optimization**: Predict delays based on traffic/weather.
- 🔁 **Resource Scheduling**: Assign deliveries to agents based on predicted load.
- 🧑‍🔧 **Agent Performance Analysis**: Evaluate based on predicted vs actual delivery times.
- 🔮 **Dynamic ETA Predictions**: Display real-time delivery estimates to customers.

---

## ⚙️ Tech Stack

| Layer              | Tools / Libraries                            |
|--------------------|-----------------------------------------------|
| Programming        | Python                                        |
| ML Libraries       | Scikit-learn, XGBoost, TensorFlow/Keras       |
| EDA & Visualization| Pandas, NumPy, Matplotlib, Seaborn            |
| Hyperparameter Tuning | GridSearchCV, RandomizedSearchCV         |
| Model Tracking     | MLflow                                        |
| Web App            | Streamlit                                     |
| Deployment         | Local / AWS (optional)                        |

---

## 📂 Dataset Overview

**File**: `amazon_delivery.csv`  
Realistic delivery data with over 10 features:

| Feature               | Description                            |
|------------------------|-----------------------------------------|
| `Order_ID`             | Unique ID per order                     |
| `Agent_Age`, `Agent_Rating` | Delivery agent profile          |
| `Store_Lat/Long`       | Store location                         |
| `Drop_Lat/Long`        | Delivery destination                   |
| `Order_Time`, `Pickup_Time` | Timing of order and pickup     |
| `Traffic`, `Weather`   | Environmental factors                  |
| `Vehicle`, `Category`  | Delivery vehicle & product category     |
| `Delivery_Time`        | Target variable (in minutes)            |

---

## 🧪 Project Workflow

### 🧹 1. Data Cleaning & Feature Engineering
- Removed nulls and outliers
- Converted time-based columns to datetime
- Calculated **Haversine distance** between pickup and drop
- Encoded categorical features like traffic and weather

### 📊 2. Exploratory Data Analysis (EDA)
- Delivery time distribution by category, vehicle, traffic
- Impact of weather, distance, and traffic on time
- Correlation heatmaps & pairplots

### 🤖 3. Model Development
Trained and compared multiple regressors:

| Model               | Notes                             |
|---------------------|-----------------------------------|
| Linear Regression   | Baseline                          |
| Ridge/Lasso         | Regularization                    |
| Random Forest       | Non-linear baseline               |
| XGBoost             | Best performer (low RMSE)         |
| Neural Network      | Deep learning model (Keras)       |

### 🎯 4. Hyperparameter Tuning
- Performed **GridSearchCV** and **RandomizedSearchCV**
- Tuned key params: `max_depth`, `n_estimators`, `alpha`, etc.

### 📈 5. Model Evaluation

| Metric     | Description                           |
|------------|----------------------------------------|
| RMSE       | Root Mean Squared Error               |
| R² Score   | Model explanatory power               |
| MAE        | Mean Absolute Error                   |

Best models:
- ✅ **XGBoost Regressor**
- ✅ **Keras Neural Network**

### 📘 6. MLflow Tracking

Logged all experiments with:
- Model version
- Hyperparameters
- Metrics (RMSE, R², MAE)
- Artifacts (plots, models)

### 🌐 7. Streamlit UI

Built a functional **Streamlit web application** to:
- Accept user inputs (category, traffic, distance, etc.)
- Return **predicted delivery time**
- Display model summary and confidence score


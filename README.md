### **📌 Amazon Delivery Time Prediction**  

**Domain:** E-Commerce & Logistics  
**Skills:** Python, Machine Learning, Regression Modeling, MLflow, Streamlit  

---

## **📖 Project Overview**  
This project predicts **Amazon delivery times** based on factors like **distance, traffic, and goods category*. It aims to enhance logistics efficiency by providing accurate delivery time estimates.  

A **Streamlit-based UI** allows users to input **order details** and receive estimated delivery times.

---

## **🔍 Business Use Cases**  
✔️ **Optimized Delivery Logistics** → Predict delivery times to improve customer experience.  
✔️ **Dynamic Traffic & Weather Adjustments** → Adjust estimates based on live conditions.  
✔️ **Agent Performance Evaluation** → Analyze delivery efficiency and identify improvement areas.  
✔️ **Operational Efficiency** → Optimize **resources & scheduling** based on delivery trends.  

---

## **⚙️ Tech Stack Used**  
- **Programming:** Python  
- **Data Processing:** Pandas, NumPy
- **Machine Learning Models:** Linear Regression - Lasso and Ridge, Random Forest, XGBoost, Neural Networks  
- **Hyperparameter Tuning:** GridSearchCV, RandomizedSearchCV  
- **Model Tracking:** MLflow  
- **Visualization:** Matplotlib, Seaborn  
- **Deployment:** Streamlit  

---

## **📂 Dataset Details (`amazon_delivery.csv`)**  
| Feature | Description |
|---------|------------|
| **Order_ID** | Unique ID for each order |
| **Agent_Age** | Age of the delivery agent |
| **Agent_Rating** | Rating of the delivery agent |
| **Store_Latitude/Longitude** | Store location coordinates |
| **Drop_Latitude/Longitude** | Delivery location coordinates |
| **Order_Date/Time** | When the order was placed |
| **Pickup_Time** | When the agent picked up the order |
| **Weather** | Weather conditions during delivery |
| **Traffic** | Traffic conditions during delivery |
| **Vehicle** | Type of vehicle used |
| **Area** | Delivery location (Urban/Metropolitan) |
| **Category** | Product category (Electronics, Apparel, etc.) |
| **Delivery_Time** | Actual time taken for delivery (Target variable) |

---

## **🚀 Project Workflow**  
### **1️⃣ Data Preparation & Cleaning**  
🔹 Load and preprocess dataset  
🔹 Handle missing values, duplicates, and inconsistent data  
🔹 Standardize categorical features like **Weather & Traffic**  

### **2️⃣ Exploratory Data Analysis (EDA)**  
📊 Distribution of delivery times  
📊 Impact of **traffic & weather** on delivery times  
📊 Relationship between **distance & delivery time**  
 
### **3️⃣ Model Development & Training**  
✅ **Models Used:**  
✔️ Linear Regression  
✔️ Random Forest Regressor  
✔️ Gradient Boosting Regressor (XGBoost)  
✔️ Neural Network (TensorFlow/Keras)  

📌 **Hyperparameter Tuning:**  
- GridSearchCV  
- RandomizedSearchCV  

### **5️⃣ Model Tracking & Evaluation**  
📌 **MLflow** for logging:  
- **Hyperparameters** (e.g., `max_depth`, `n_estimators`)  
- **Performance Metrics** (`RMSE`, `R² Score`, `MAE`)  
- **Model Versions**  

### **6️⃣ Streamlit Deployment**  
💻 **User Inputs:** Distance, Traffic, Weather, etc.  
📈 **Outputs:** Estimated Delivery Time  

---

## **🏆 Key Results**  
✔️ **Multiple regression models** tracked using MLflow.  
✔️ **Feature Importance Analysis** revealed that **traffic & distance** significantly impact delivery time.  
✔️ **Neural Network & XGBoost** performed best, achieving the lowest RMSE.  
✔️ **A functional Streamlit UI** was built to provide delivery time predictions.  

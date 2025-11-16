# Linear Regression

A simple **Linear Regression** implementation in Python for learning and educational purposes.

---

## 📘 Overview

This project demonstrates a linear regression model to predict a continuous target variable from input features. It includes:

- Data loading and preprocessing  
- Model training  
- Evaluation using common regression metrics (MSE, RMSE, R²)  
- Visualization of predictions vs actual values  

---

## 🚀 Features

- Support for **simple and multiple linear regression**  
- Model evaluation metrics: MSE, RMSE, R²  
- Visualization with `matplotlib`, seaborn (if included)  
- Easy to extend to more advanced regression techniques  

---

## 💡 Why This Project Matters

- **Learning purpose**: Understand how linear regression works from scratch or using scikit-learn.  
- **ML pipeline practice**: Practice data preparation, model training, and evaluation.  
- **Extendable**: Can easily add polynomial regression, regularization, or multiple features.  

---

## 🛠 Usage

1. **Clone the repository**  
   ```bash
    git clone https://github.com/huyendt1610/LinearRegression.git
    cd LinearRegression
    ```
2. **Set up Python environment**  
    ```bash
    python -m venv venv
    source venv/bin/activate   # hoặc `venv\Scripts\activate` trên Windows
    pip install -r requirements.txt
    ```

3. **Run the training script / notebook**
   Choose each notebook (ex: BuildingPipeline_GermanCreditData.ipynb) -> Rull All


4. **See results**  
    - Predictions will be printed, logged
    - Visualizations of predictions vs actual values 

## 📦 Requirements

- Python 3.7+  
- numpy  
- pandas  
- scikit-learn  
- matplotlib
- seaborn 
- statsmodels

*(Install dependencies `pip install -r requirements.txt`.)*
## 📈 Model Evaluation

Metric:

| Metric | Description |
|---|---|
| **MSE (Mean Squared Error)** | Average squared difference between predicted and actual values |
| **RMSE (Root MSE)** | Squared root of MSE, in the same unit with target. |
| **R² (Coefficient of Determination)** | Measures how well the model explains variance in the data (0 to 1) |

## 📂 Project Structure

LinearRegression/
├── data/                # Dataset (csv, dat)
├── algorithms/                
│   └── LinearRegression.ipynb
│   └── LogisticRegression.ipynb
│   └── RidgeAndLasso.ipynb
├── notebooks/           # Nếu sử dụng Jupyter Notebook
│   └── LogisticRegression_LoanPrediction.ipynb
│   └── BuildingPipeline_GermanCreditData.ipynb
│   └── ....
├── requirements.txt     # Thư viện cần cài
└── README.md            # File này

## ✏️ How to Contribute

Contributions are welcome! You can:

- Improve or add notebooks/scripts  
- Add regularization methods (Ridge, Lasso)  
- Experiment with different datasets  
- Enhance visualizations (residual plots, regression lines)

Steps to contribute:

1. Fork the repository  
2. Create a new branch: `git checkout -b feature-name`  
3. Commit changes and push: `git push origin feature-name`  
4. Open a Pull Request  

---

## 🤝 License

This project is licensed under the **MIT License**.  


---

## 📚 References & Learning Resources

- [Basic Machine Learning](https://machinelearningcoban.com/)  
- [Application of Linear Regression](https://phamdinhkhanh.github.io/deepai-book/ch_ml/prediction.html)  

📈 Demand Forecasting Pipeline — Refactored from Production
This project builds a robust time series forecasting framework tailored for structured retail sales data. It originated as a real production model used by a mid-sized company to manage demand forecasting across thousands of unique product-location pairs. The original system relied on Holt-Winters (Triple Exponential Smoothing), but this refactored version integrates SARIMA to improve adaptability and seasonality handling.

🎯 Problem Statement
The dataset contains monthly sales grouped by sucursal (store), producto (SKU), and año. Sales patterns vary widely: some series are sparse, noisy, or skewed by outliers, while others exhibit strong seasonal behavior.
Forecasting demand accurately is vital for optimizing inventory, reducing loss, and improving logistical planning — especially when scaling across dozens of locations and thousands of SKUs.

⚙️ Model and Approach
- Forecasting method: AutoARIMA (preliminary test) and SARIMA (target refinement)
- Data processing module:
- Cleans and restructures monthly records
- Filters out non-informative series
- Fills missing values based on temporal logic
- Applies seasonal outlier correction per block
- Training set: Years 2017–2018
- Validation set: Year 2019

🧪 Experiment Results
| Phase        | MAE   | RMSE  | Mean Sales |
|--------------|-------|-------|------------|
| Raw Data     | 8.15  | 25.37 | ≈9.76      |
| Cleaned Data | 9.24  | 38.55 | ≈9.76      |


Initial expectations were that cleaning would lead to stronger performance, but instead the metrics worsened — revealing that previous predictions were diluted by null series or noise. The cleaned dataset exposes the model’s true behavior more accurately, which creates new opportunities for tuning and improvement.

🔬 Next Steps
- Analyze per-series errors and identify segment-level issues (e.g. store clusters or SKU categories)
- Apply logarithmic transformation to reduce right-side skew and amplify relative performance
- Manually tune SARIMA parameters (p,d,q,P,D,Q) and compare against AutoARIMA
- Explore alternate models: ETS, Prophet, ML-based regressors

🔧 How to Use It
This pipeline is modular and scalable. It includes:
- A preprocessing module (limpiar.py)
- A forecast module using StatsForecast
- Training and validation pipelines
- Error tracking and evaluation tools
Users can adapt the data cleaning and modeling strategy depending on their industry context — retail, logistics, manufacturing, or ecommerce — and plug in any model they prefer.

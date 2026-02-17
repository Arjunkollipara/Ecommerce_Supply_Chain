Supply Chain Optimization and Demand Forecasting  

(Olist Brazilian E-commerce Dataset)



Project Overview:

This project is an academic capstone work focused on analyzing and optimizing supply chain operations using the Olist Brazilian E-commerce dataset. The goal of this project is to apply demand forecasting, inventory optimization, and delivery performance analysis techniques to improve operational efficiency.



The project is currently under development. Milestones 1, 2, and 3 have been completed. Milestone 4 (Dashboard and Strategy Implementation) is in progress.



Dataset:

The dataset used in this project is the Olist Brazilian E-commerce Public Dataset available on Kaggle.



It contains:

\- 100,000+ orders

\- 9 relational CSV files

\- Data from 2016 to 2018

\- Customer, seller, product, payment, and delivery information



The raw dataset is not included in this repository due to size limitations. To reproduce this project:

1\. Download the dataset from Kaggle:

&nbsp;  https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

2\. Place all CSV files inside the `data/raw/` directory.

3\. Run the notebooks in order.



Tools Used

\- Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)

\- Jupyter Notebook

\- Microsoft Excel (for intermediate transformations)

\- Power BI (for dashboard development - Milestone 4)



Project Structure:

quickkart-supply-chain-optimization/

│

├── notebooks/

│   ├── M1\_Order\_Analysis.ipynb

│   ├── M2\_Delivery\_Forecasting.ipynb

│   ├── M3\_Inventory\_Optimization.ipynb

│

├── data/

│   ├── raw/

│   ├── processed/

│

├── powerbi/

│   ├── M4\_SupplyChain\_Dashboard.pbix

│

├── reports/

│   ├── M1\_Report.pdf

│   ├── M2\_Report.pdf

│   ├── M3\_Report.pdf

│

├── requirements.txt

└── README.md



Milestone Breakdown:



Milestone 1 – Order Pattern Analysis

\- Integrated 9 relational datasets

\- Performed data cleaning and preprocessing

\- Analyzed order trends, seasonality, and geographic distribution

\- Identified top product categories by volume and revenue



Milestone 2 – Delivery Performance and Forecasting

\- Calculated delivery delays and on-time performance metrics

\- Identified problematic regions and routes

\- Implemented Moving Average and Exponential Smoothing forecasting models

\- Evaluated forecasts using MAE, RMSE, and MAPE

\- Generated 30-day demand forecasts for selected categories



Milestone 3 – Inventory Optimization

\- Selected high-demand products for detailed inventory analysis

\- Calculated EOQ for each product

\- Determined safety stock and reorder points

\- Performed ABC classification based on revenue contribution

\- Estimated cost savings and ROI from optimized inventory policies



Milestone 4 – Dashboard and Strategy (In Progress)

\- Developing Power BI dashboard with:

&nbsp; - Order analytics

&nbsp; - Delivery performance visualization

&nbsp; - Demand forecasting view

&nbsp; - Inventory KPIs

\- Preparing final supply chain strategy document



Key Analytical Methods Used



\- Time series aggregation and trend analysis

\- Moving Average (7-day and 30-day)

\- Exponential Smoothing

\- Economic Order Quantity (EOQ) model

\- Safety Stock and Reorder Point calculation

\- ABC inventory classification

\- Cost-benefit and ROI estimation



How to Run the Project



1\. Install required Python packages:

&nbsp;  pip install -r requirements.txt



2\. Download and place dataset in data/raw/



3\. Open Jupyter Notebook and run notebooks in the following order:

&nbsp;  - M1\_Order\_Analysis.ipynb

&nbsp;  - M2\_Delivery\_Forecasting.ipynb

&nbsp;  - M3\_Inventory\_Optimization.ipynb



Note



This project is intended for academic demonstration purposes. The models and assumptions (ordering cost, lead time, holding cost rate, etc.) are simplified for analytical understanding and may require refinement for real-world implementation.



Future Improvements



\- Complete interactive Power BI dashboard

\- Explore advanced forecasting methods (e.g., ARIMA)

\- Automate data pipeline instead of manual Excel transformation

\- Integrate real-time KPI monitoring



Contributions



Suggestions and improvements are welcome. Feel free to open an issue or submit a pull request.




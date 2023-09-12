# Aquifer-TimeSeries-Analysis-Visualization
Aquifer Time Series Analysis and Visualization
![Untitled](https://github.com/stevengash/Aquifer-TimeSeries-Analysis-Visualization/assets/99188129/cdfa4b29-335f-46b4-aaa8-af88b8714e81)
This repository contains Python code for analyzing and visualizing Aquifer data, specifically data from the Aquifer of Petrignano in Italy. The analysis includes data cleaning, visualization, and initial exploratory data analysis. It also provides a foundation for further time series analysis and forecasting.
Overview
The code is organized into several sections, each with a specific purpose. Here's a brief overview of what each section does:
Data Loading and Preprocessing
•	We start by importing the necessary Python libraries, including Pandas, NumPy, Matplotlib, and Statsmodels.
•	The dataset is loaded from a CSV file, which should be replaced with your file path.
•	Rows with missing values in the 'Rainfall_Bastia_Umbra' column are removed.
•	Unnecessary columns are dropped, and the remaining columns are renamed for clarity.
•	The 'date' column is converted to a datetime format.
•	A summary of the cleaned dataset is displayed, including its shape, missing values, and date range.
Data Visualization
•	We use Seaborn and Matplotlib for data visualization.
•	Various time series plots are created to visualize different aspects of the data, including rainfall, depth to groundwater, temperature, drainage volume, and river hydrometry.
•	Each plot is labeled and includes appropriate titles and axis labels for clarity.
![Untitled](https://github.com/stevengash/Aquifer-TimeSeries-Analysis-Visualization/assets/99188129/acfda27b-4427-40c9-b6fa-e95fbf1cbf48)
![Untitled](https://github.com/stevengash/Aquifer-TimeSeries-Analysis-Visualization/assets/99188129/26f4e981-dbff-4029-b170-5877506197f2)
![Untitled](https://github.com/stevengash/Aquifer-TimeSeries-Analysis-Visualization/assets/99188129/f527ab55-8e26-4545-8e9a-db9e776a594f)
Time Series Decomposition
•	Time series decomposition is performed on the 'depth_to_groundwater' column using the additive model with a seasonal period of 365 days.
•	The decomposition results in three components: trend, seasonal, and residual.
•	Plots of these components are created for visual inspection
![Untitled](https://github.com/stevengash/Aquifer-TimeSeres-Analysis-Visualization/assets/99188129/fb7fc21e-5038-4e46-9046-d14c3e02f8e2)
Autocorrelation and Partial Autocorrelation
•	Autocorrelation and partial autocorrelation plots are generated for the 'depth_to_groundwater' time series.
•	These plots help identify potential autoregressive and moving average components in the data, which can be useful for modeling.
![Untitled](https://github.com/stevengash/Aquifer-TimeSeries-Analysis-Visualization/assets/99188129/444c6f20-0dd2-4553-b066-803a239df325)
Rolling Mean
•	Rolling mean calculations are applied to the 'rainfall' and 'depth_to_groundwater' columns with a window size of 30 days.
•	Smoothed time series plots are created to visualize the original data along with the rolling means.
Correlation Heatmap
•	A correlation matrix is computed to analyze the relationships between different variables in the dataset.
•	A heatmap is generated to visualize the correlations, making it easier to identify potential dependencies between variables.
![Untitled](https://github.com/stevengash/Aquifer-TimeSeries-Analysis-Visualization/assets/99188129/0de53a8f-c222-4b36-88b9-6ad76bea7236)
Note
Please note that this repository focuses on data analysis and visualization, providing a foundation for further time series forecasting models. Building forecasting models would require additional steps such as data pre-processing, feature engineering, model selection, and evaluation, which are not covered in this README.
For the dataset used in this code, you can find it here. Make sure to replace the file path in the code with the location of your dataset if you use a different one.
Feel free to adapt and expand upon this code to suit your specific analysis and forecasting needs.


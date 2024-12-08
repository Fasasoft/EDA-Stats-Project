# EDA-Stats-Project
## Project Goals
The primary objective of this project is to analyze a given dataset to uncover meaningful insights using Exploratory Data Analysis (EDA). By utilizing statistical and visualization techniques, we aim to:

- Understand the structure and quality of the dataset.
- Identify patterns, trends, and relationships within the data.
- Detect and address data anomalies and outliers.
- Provide actionable insights to aid further decision-making and analysis.

## Insights from EDA
Through detailed analysis, the following key insights were uncovered:

- **Summary Statistics**: A comprehensive overview of data distribution, including mean, median, and standard deviations of numeric columns, highlighted central tendencies and variability in solar irradiance and temperature metrics.
- **Data Quality Checks**: Identified missing values, outliers, and anomalies, especially in critical columns like GHI, DNI, DHI, and sensor readings (ModA, ModB).
- **Time Series Patterns**: Visualization of variables like GHI, DNI, and temperature over time revealed diurnal and seasonal trends, as well as anomalies in solar irradiance peaks and temperature fluctuations.
- **Correlation Analysis**: Correlation matrices highlighted significant relationships between solar irradiance components (GHI, DNI, DHI) and temperature metrics (TModA, TModB). Wind speed and direction showed moderate relationships with solar irradiance.
- **Wind and Temperature Analysis**: Wind roses illustrated wind speed and direction trends, while temperature and relative humidity analyses revealed their combined influence on solar radiation metrics.
- **Distribution Visualizations**: Histograms and bubble charts offered deeper insights into frequency distributions and complex relationships among multiple variables.

## Steps to Reproduce Results

To replicate the results from this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Fasasoft/EDA-Stats-Project.git
   cd EDA-Stats-Project
   ```

2. **Set Up the Environment**:
   - Ensure you have Python installed (preferably version 3.8 or later).
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Locate the Dataset**:
   - Place your dataset (`path_to_dataset.csv`) in the root of the project directory or update the path in the notebook.

4. **Run the Jupyter Notebook**:
   - Start Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Navigate to the `notebooks` folder and open `eda.ipynb`.
   - Run each cell sequentially to perform the EDA.

5. **Explore Visualizations**:
   - Inspect the visualizations and statistical outputs generated within the notebook for insights.

6. **Modify and Extend**:
   - Customize the notebook to explore additional hypotheses or new datasets.

## Contact Information
For questions or feedback, feel free to contact:

- **Fasil Teshome**
- Email: fasilteshsoft@gmail.com
- GitHub: [Fasasoft](https://github.com/Fasasoft)

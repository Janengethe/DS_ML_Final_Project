## Gym Class Attendance Prediction
### Overview
This machine learning project aims to predict gym class attendance based on historical data. The project utilizes a regression model to forecast the number of people attending gym classes, allowing for better resource allocation and class scheduling.

### Table of Contents
1. Project Description
2. Data
3. Preprocessing
4. Model Development
5. Hyperparameter Tuning
6. Evaluation
7. Deployment
8. Getting Started
9. Dependencies
10. Contributing
11. License

### Project Description
In this project, we build a predictive model to estimate the number of attendees for gym classes. Accurate predictions help optimize staffing and resource allocation, ensuring that gym-goers have a seamless experience.

### Data
* Dataset: Gym Class Attendance Data
* Columns: number_people, date, timestamp, day_of_week, is_weekend, is_holiday, temperature, is_start_of_semester, is_during_semester, month, hour

### Preprocessing
* Data cleaning to handle missing values.
* Feature engineering to create relevant features.
* Date and time manipulation.

### Model Development
* Utilized a regression model to predict class attendance.
* Implemented feature scaling and encoding for model training.
* Evaluated models using performance metrics like MSE, MAE, and R² score.

### Hyperparameter Tuning
* Employed grid search to fine-tune model hyperparameters.
* Optimal hyperparameters were selected based on cross-validation results.

### Evaluation
* Model performance was assessed on test dataset.
* Metrics:
  * Mean Squared Error (MSE)
  * Mean Absolute Error (MAE)
  * R-squared (R²) score

### Deployment
* Deployed the final model for real-world usage.
* Used Streamlit for deployment.
* Created a prediction pipeline for integration into applications.

### Getting Started
* Clone this repository to your local machine.
* Install the required dependencies using pip install -r requirements.txt.
* Explore the provided Jupyter notebooks for data exploration and model training.
* Deploy the model as needed for real-world usage.

### Dependencies
Python 3.6+
NumPy
Pandas
Scikit-learn
Matplotlib
Plotly (for interactive visualizations)

### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.


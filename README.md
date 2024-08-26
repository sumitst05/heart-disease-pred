# Heart Disease Prediction API

This project is just me trying to get my hands dirty with a little bit of ML magic.

## Project Structure

- `app/`: Has got the FastAPI application code.
- `src/models/`: Has the pre-trained model file `heart_model.pkl`.
- `src/data/`: Dataset used for model training ([heart.csv](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset/data))
- `notebooks/`: Contains Jupyter Notebooks used for developing and testing the model.
- `requirements.txt`: Lists the Python dependencies for the project.

## How to Use

### Starting the FastAPI Application

1. **Install Dependencies**: Make sure you have all required packages installed. You can install them using:
   ```bash
   pip install -r requirements.txt

2. **Run the FastAPI Application: Start the server with**:
    ```bash
    uvicorn app.main:app --reload
    ```
    > The API will be accessible at http://127.0.0.1:8000.


### Making Predictions

To make a prediction, send a POST request to the /predict endpoint with the following JSON body:

_Example:_

```json
{
  "age": 34,
  "sex": 0,
  "cp": 1,
  "trestbps": 118,
  "chol": 210,
  "fbs": 0,
  "restecg": 1,
  "thalach": 192,
  "exang": 0,
  "oldpeak": 0.7,
  "slope": 2,
  "ca": 0,
  "thal": 1
}
```

**Parameters**:

- age: Age of the patient (integer).

- sex: Sex of the patient (0 = female, 1 = male).

- cp: Chest pain type (0 to 3).

- trestbps: Resting blood pressure (integer).

- chol: Serum cholesterol level (integer).

- fbs: Fasting blood sugar > 120 mg/dl (0 = false, 1 = true).

- restecg: Resting electrocardiographic results (0 to 2).

- thalach: Maximum heart rate achieved (integer).

- exang: Exercise induced angina (0 = no, 1 = yes).

- oldpeak: Depression induced by exercise relative to rest (float).

- slope: Slope of the peak exercise ST segment (0 to 2).

- ca: Number of major vessels colored by fluoroscopy (0 to 3).

- thal: Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect).


## Model File

The pre-trained model file heart_model.pkl is included in the src/models/ directory. This file was created by training the model on the dataset provided in data/heart.csv.

## Notbook

You can find the colab notebook that was used in /notebooks

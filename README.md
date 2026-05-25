# Heart Disease Prediction Using Machine Learning
Cardiovascular diseases (CVDs) remain the leading cause of mortality globally, necessitating advanced computational tools for early detection and risk assessment. This project presents a robust, end-to-end clinical decision support system designed to predict the likelihood of heart disease in patients based on physiological parameters.
By bridging the gap between complex machine learning algorithms and practical clinical application, this platform offers a scalable solution for proactive healthcare management.
## 🚀 Key Features
 * **Real-Time Prediction**: Generates near-instantaneous predictions (processing in approximately 1.2 seconds) to assist in time-sensitive medical situations.
 * **High Accuracy**: Achieves an 87% predictive accuracy using an optimized Random Forest Classification model.
 * **Graphical Visualization**: Generates bar graphs comparing a user's health metrics against a healthy baseline for easy visual analysis.
 * **Secure Authentication**: Provides complete user lifecycle management, including sign-up, secure login, and password recovery.
 * **Email Notifications**: Utilizes Flask-Mail to automatically send system-generated passwords directly to user emails.
 * **Responsive Interface**: Ensures accessibility across devices (smartphones, tablets, computers) for both medical professionals and patients.
## 🛠️ Technology Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3.9+, Flask | Engine for logic, model routing, and REST API creation. |
| **Machine Learning** | Scikit-learn, Random Forest | Training the classification model and evaluating predictions. |
| **Data Handling** | Pandas, Pickle | Cleaning user input data and serializing the trained model. |
| **Database** | SQLite3 | Lightweight, file-based storage for user credentials. |
| **Visualization** | Matplotlib | Generating comparative charts for clinical metrics. |

## 📊 Dataset & Algorithm
### The Dataset
The model is trained and validated using the **UCI Heart Disease Dataset**. It incorporates 14 critical clinical attributes, including:
 * Age and Sex
 * Chest Pain Type (Typical, Atypical, Non-anginal, Asymptomatic)
 * Resting Blood Pressure and Serum Cholesterol
 * Maximum Heart Rate Achieved
 * Resting Electrocardiographic Results and ST Depression
 * Number of Major Vessels Colored by Fluoroscopy
### The Algorithm
The core of the system utilizes a **Random Forest Algorithm**, chosen for its high accuracy and resistance to overfitting. The ensemble learning technique builds multiple decision trees and aggregates their outputs to handle complex, non-linear relationships and missing values efficiently.
## 💻 Setup and Installation
Follow these steps to run the application locally:
 1. **Clone the repository** and navigate to the project directory.
 2. **Create a virtual environment** to ensure dependency management.
 3. **Install dependencies** (requires Flask, Flask-Mail, pandas, scikit-learn, matplotlib).
 4. **Set Environment Variables**: Configure MAIL_PASSWORD in your environment to enable the Gmail SMTP email functionality.
 5. **Ensure Model Exists**: Verify that the pre-trained heartdiseaseprediction.model pickle file is present in the root directory.
 6. **Run the application**: Execute python app.py.
 7. **Access the app**: Open a web browser and navigate to the local Flask server (typically http://127.0.0.1:5000/).

    

#!/usr/bin/python3
"""
console module
"""
from os import getenv
import importlib
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.models import User, Program, Course
from models.models import Project, Enrollment, Resource
from models.models import Quiz
from models.models import  UserQuiz
from models import storage



class EduPahtwayommand(cmd.Cmd):
    """Console class"""
    prompt = '(RoofMarket) ' if sys.__stdin__.isatty() else ''
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Program': Program,
               'Course': Course, 'Project': Project, 'Enrollment': Enrollment,
               'Resource': Resource, 'Quiz': Quiz, 'UserQuiz': UserQuiz
              }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_EOF(self, line):
        """Handle End-of-File (EOF) condition to exit the program gracefully"""
        print()
        return True

    def do_create(self, args):
        """ Create an object of any type

            Usage: create class_name
        """
        project_dict = [{
            "title": "Predicting Customer Churn in Telecom",
            "task_name": "Customer Churn Prediction",
            "description": """
            **Objective:**
            Students will analyze customer data to predict which customers are likely to churn (cancel their subscription) from a telecommunications company. 
            They will perform exploratory data analysis, build predictive models using statistics and probability, and evaluate the models' effectiveness in predicting churn.
            
            **Dataset:**
            You can either create a synthetic dataset or use an open-source customer churn dataset. A widely used real dataset is available on platforms like Kaggle or you can use the IBM Telco Customer Churn dataset.
            
            Here's a brief overview of what the dataset might look like:
            
            - **CustomerID**: Unique identifier for each customer.
            - **Gender**: Male or Female.
            - **SeniorCitizen**: Whether the customer is a senior citizen (1 = Yes, 0 = No).
            - **Partner**: Whether the customer has a partner (Yes/No).
            - **Dependents**: Whether the customer has dependents (Yes/No).
            - **Tenure**: Number of months the customer has been with the company.
            - **PhoneService**: Whether the customer has phone service (Yes/No).
            - **MultipleLines**: Whether the customer has multiple phone lines (Yes/No).
            - **InternetService**: Type of internet service (DSL/Fiber optic/No).
            - **OnlineSecurity**: Whether the customer has online security (Yes/No).
            - **OnlineBackup**: Whether the customer has online backup (Yes/No).
            - **DeviceProtection**: Whether the customer has device protection (Yes/No).
            - **TechSupport**: Whether the customer has tech support (Yes/No).
            - **StreamingTV**: Whether the customer has streaming TV (Yes/No).
            - **StreamingMovies**: Whether the customer has streaming movies (Yes/No).
            - **Contract**: Type of contract (Month-to-month, One year, Two year).
            - **PaperlessBilling**: Whether the customer has paperless billing (Yes/No).
            - **PaymentMethod**: Payment method (Electronic check, Mailed check, Bank transfer, Credit card).
            - **MonthlyCharges**: The customer's monthly charges.
            - **TotalCharges**: Total charges over the customer's tenure.
            - **Churn**: Whether the customer has churned (Yes/No).
            
            **Project Steps:**
            
            1. **Exploratory Data Analysis (EDA):**
                - **Data Cleaning**: Handle missing values, check for duplicates, and ensure correct data types.
                - **Descriptive Statistics**: Calculate and interpret mean, median, standard deviation, and correlation among features.
                - **Visualizations**: Create plots such as histograms, box plots, and heatmaps to understand the distribution of data and relationships between variables.
                - **Churn Distribution**: Analyze the distribution of churn (Yes/No) and explore which features (e.g., contract type, payment method, tenure) are correlated with churn.
            
            2. **Statistical Analysis:**
                - **Hypothesis Testing**: Test hypotheses like:
                    - "Customers with longer tenure are less likely to churn."
                    - "Customers on month-to-month contracts are more likely to churn."
                - **Probability Analysis**: Use concepts like conditional probabilities to estimate the likelihood of churn based on customer features.
                - **Chi-square Test**: Conduct tests to determine whether the relationship between categorical features (e.g., contract type, payment method) and churn is statistically significant.
            
            3. **Predictive Modeling:**
                - **Logistic Regression**: Build a logistic regression model to predict the probability of customer churn.
                - **Decision Trees**: Implement a decision tree classifier to create interpretable models for predicting churn.
                - **Random Forest**: Use Random Forest to improve model accuracy by using an ensemble of decision trees.
                - **Support Vector Machine (SVM)**: Implement an SVM model for churn prediction.
                - **Feature Engineering**: Create new features (e.g., tenure categories, total charges per month) to improve model performance.
            
            4. **Model Evaluation:**
                - **Confusion Matrix**: Evaluate model performance using accuracy, precision, recall, F1-score, and ROC-AUC.
                - **Cross-validation**: Use k-fold cross-validation to ensure the model generalizes well on unseen data.
                - **Hyperparameter Tuning**: Use grid search or random search to optimize the hyperparameters of your models.
            
            5. **Insights and Recommendations:**
                - Identify the most significant factors contributing to churn.
                - Based on your analysis, provide actionable recommendations that the telecom company could use to reduce churn (e.g., offering discounts, improving customer service).
                - Discuss how probability and statistics were used to inform decisions.
            
            **Deliverables:**
            - **Report**: A detailed report with the following sections:
                - Data Exploration (summary statistics, visualizations)
                - Statistical Analysis (hypothesis testing, probability analysis)
                - Modeling (description of the models used and their evaluation)
                - Insights and Recommendations (actions to reduce churn based on findings)
            - **Code**: Python code (using libraries such as pandas, numpy, scikit-learn, seaborn, matplotlib) for data cleaning, exploration, modeling, and evaluation.
            - **Presentation**: A 10-15 minute presentation that highlights key findings and recommendations based on the analysis.
            
            **Tools and Libraries:**
            - Python Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Statsmodels
            - Tools for Reporting: Jupyter Notebooks or Google Colab
            - Data Source: Kaggle (IBM Telco Customer Churn dataset)
            
            **Learning Outcomes:**
            - Understand the application of probability and statistics in real-world data science problems.
            - Develop skills in data cleaning, exploratory data analysis, and visualization.
            - Build and evaluate predictive models for classification tasks.
            - Learn to interpret statistical test results and apply them to make data-driven decisions.
            - Gain hands-on experience with machine learning algorithms such as Logistic Regression, Decision Trees, and Random Forests.
            
            By working with a real-world problem like customer churn prediction, students will gain practical experience with statistical concepts, predictive modeling, and data-driven decision-making in the context of data science.
            """,
            "course_id": "2d1b9011-01d6-400c-aaea-b418155cdf1c",
        }]


     

        try:
            for program_data in project_dict:
                new_instance = Project()
                for key, value in program_data.items():
                    setattr(new_instance, key, value)
                new_instance.save()
                print(f"Created Program with ID: {new_instance.id}")
        except Exception as e:
            print(e)


    def do_destroy(self, args):
        """Delete an object or row from the database
        Usage: destroy class_name object_id
        
        """
        
        arguments = shlex.split(args)
        if not args:
            print("** class doesn't exist **")
            return
        elif arguments[0] not in EduPahtwayommand.classes:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 1:
            print("** provide the id of the object **")
            return
        ob_id = "{}.{}".format(arguments[0].lower(), arguments[1])
        for key, value in storage.all(arguments[0]).items():
            if (key == ob_id):
                value.delete()
                storage.save()

    def do_all(self, args):  
        print(storage.get_object(User))

    def do_get(self, args):
        """Get an object"""
        if args:
            arguments = shlex.split(args)
            if len(arguments) == 2:
                user = storage.get_object(User, id="9566ffb2-1df8-496f-8f13-972bdf2f60ab")
                print(user)
                user.delete()
                storage.save()
                


if __name__ == '__main__':
    EduPahtwayommand().cmdloop()

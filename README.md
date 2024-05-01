### Boston House Pricing Prediction

The end-to-end machine learning project for Boston House Pricing Prediction involves using Docker for containerization and creating a CI/CD pipeline. Here is a summary of the project:

1. **Machine Learning Project**:
   - The project involves predicting Boston house prices based on various features using machine learning models.
   - Data ingestion, data transformation, model training, and prediction pipelines are implemented in the project.
   - The Flask web application allows users to input data for predicting student performance, leveraging a machine learning model trained on educational data.

2. **Docker Integration**:
   - Docker is utilized for containerizing the machine learning project, ensuring consistency and portability across different environments.
   - By containerizing the project with Docker, dependencies and configurations are encapsulated, simplifying deployment and scaling.

3. **CI/CD Pipeline**:
   - A CI/CD pipeline is set up to automate the testing, building, and deployment processes of the machine learning project.
   - The pipeline ensures that changes to the project are automatically tested and deployed, improving efficiency and reducing manual errors.
   - Continuous Integration (CI) involves automatically testing code changes, while Continuous Deployment (CD) automates the deployment of successful builds.

4. **Boston House Pricing Prediction**:
   - The project focuses on predicting house prices in Boston using machine learning algorithms trained on historical housing data.
   - Users can interact with the Flask web application to input data related to student performance factors and receive predictions based on the machine learning model.

In summary, the end-to-end machine learning project for Boston House Pricing Prediction incorporates Docker for containerization to streamline deployment and maintenance, along with a CI/CD pipeline for automating testing and deployment processes, ensuring efficient project management and delivery.

### Software And Tools Requirements

1. [Github Account](https://github.com/palakgandhi98)
2. [DagsHub](https://dagshub.com/palakgandhi98/MLProject)
3. [Hugging Face](https://huggingface.co/palakgandhi)
4. [HerokuAccount](https://heroku.com)
5. [VSCodeIDE](https://code.visualstudio.com/)
6. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment

```
conda create -p venv python==3.11.7 -y
```

MLFLOW_TRACKING_URI=https://dagshub.com/apgandhi98/MLProject.mlflow \
MLFLOW_TRACKING_USERNAME=apgandhi98 \
MLFLOW_TRACKING_PASSWORD=d222176e3144a49528619bb099863efc55eacd70 \
python script.py

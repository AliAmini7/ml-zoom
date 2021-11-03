This [dataset](https://www.kaggle.com/tejashvi14/employee-future-prediction) is taken from Kaggle. 

# About The Data

A company's HR department wants to predict whether some customers would leave the company in next 2 years. We are building a predictive model that predicts the prospects of future and present employee.

In this dataset, there are 8 features and 1 label. Most of the features are categorical with some that are numerical. In the following, distribution of features are presented. 

# *features:* 

Education

![Education](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/figures/Education.png)

JoiningYear

![JoiningYear](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/figures/joining_year.png)

City

![City](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/figures/city.png)

PaymentTier

![PaymentTier](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/figures/payment.png)

Age

![Age](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/figures/age.png)

Gender

![Gender](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/figures/gender.png)

EverBenched

![EverBenched](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/figures/ever_benched.png)

ExperienceInCurrentDomain

![ExperienceInCurrentDomain](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/figures/exp.png)


# *labels:* 

LeaveOrNot

NotLeave    0.65

Leave       0.35


With these features, we will build a predictive model that returns the probability that an employee is going to leave the company.


# How to test the deployement?
After deploying the predictive system, you can test it via the predict_test.py file provided. It posts the information of an employee and gets the probability of that employee leaving the company. 

![test](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/screenshots/predict_test.jpg)


# Dependency and environment management:
Contained in this repo there are two files, Pipfile and Pipfile.lock. You can run the app in a virtual environment by using the following two shell commands:

```console
pipenv shell
```

and then

```console
gunicorn --bind 0.0.0.0:9696 predict:app
```

![pipenv-shell](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/screenshots/pipenv-shell.jpg)


# Containerization:
For containerization a docker file is provided. To run it, you need to have docker installed in your system. For Windows users who use WSL, the following link is the best resource on how to install and run docker smoothly:

https://docs.docker.com/desktop/windows/wsl/ 

After the installation, you first need to build and then run the container. Don't forget to map the ports.

```console
docker build -t project1 .
```

```console
docker run -it --rm -p 9696:9696 project1
```

![docker](https://github.com/AliAmini7/ml-zoom/blob/main/project%201/screenshots/docker.jpg)


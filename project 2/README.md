This [dataset](https://www.openml.org/d/1461) is taken from Open ML. 

# About The Data

Bank Marketing
The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (or not) subscribed.

The classification goal is to predict if the client will subscribe a term deposit.

# *features:* 

1 - age (numeric)

2 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur", "student","blue-collar","self-employed","retired","technician","services")

3 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)

4 - education (categorical: "unknown","secondary","primary","tertiary")

5 - default: has credit in default? (binary: "yes","no")

6 - balance: average yearly balance, in euros (numeric)

7 - housing: has housing loan? (binary: "yes","no")

8 - loan: has personal loan? (binary: "yes","no")

- related with the last contact of the current campaign:

9 - contact: contact communication type (categorical: "unknown","telephone","cellular")

10 - day: last contact day of the month (numeric)

11 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")

12 - duration: last contact duration, in seconds (numeric)

- other attributes:

13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)

14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)

15 - previous: number of contacts performed before this campaign and for this client (numeric)

16 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")



# *labels:* 

success

no     0.884686

yes    0.115314


With these features, we will build a predictive model that returns the probability that a client has subscribed to a term deposit.


# Dependency and environment management:
Contained in this repo there are two files, Pipfile and Pipfile.lock. You can run the app in a virtual environment by using the following two shell commands:

```console
pipenv shell
```

and then

```console
gunicorn --bind 0.0.0.0:9696 predict:app
```



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



# How to test the deployement?
After deploying the predictive system, you can test it via the predict_test.py file provided. It posts the information of a client and gets the probability of that client applying for a product. 



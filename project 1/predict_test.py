#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'


employee = {
    "Education": "Masters",
    "JoiningYear": 2012,
    "City": "Bangalore",
    "PaymentTier": 3,
    "Age": 27,
    "Gender": 'Male',
    "EverBenched": 'No',
    "ExperienceInCurrentDomain": 5
}


response = requests.post(url, json=employee).json()
print(response)


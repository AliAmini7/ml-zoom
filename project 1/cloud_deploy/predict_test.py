#!/usr/bin/env python
# coding: utf-8

import requests

host = 'leaveornot-env.eba-cxusvxkz.ap-southeast-2.elasticbeanstalk.com'
url = f'http://{host}/predict'


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


#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'


client = {
    "V1": 58,
    "V2": 'management',
    "V3": 'married',
    "V4": 'tertiary',
    "V5": 'no',
    "V6": 2143,
    "V7": 'yes',
    "V8": 'no',
    "V9": 'unknown',
    "V10": 5,
    "V11": 'may',
    "V12": 261,
    "V13": 1,
    "V14": -1,
    "V15": 0,
    "V16": 'unknown'
}


response = requests.post(url, json=client).json()
print(response)


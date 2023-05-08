#!/usr/bin/env python
# coding: utf-8

cd C:\Users\Avinash\Desktop\


#%pip install faker

import csv
import pandas as pd

# File has india_pop_share_state_wise.csv  all states and there share of population along with 5 random districts 


df = pd.read_csv("india_pop_share_state_wise.csv")
print("sample data")
df.head(1)

# to generate fake name , id , age , dob ,zipcode 
from faker import Faker
import random

# Initialize the Faker object
fake = Faker()

country='India'

# function to return 1 row of data 
def generate_row():
    name=fake.first_name()
    age = random.randint(3, 80)
    dob = fake.date_of_birth(minimum_age=age-3, maximum_age=age)
    state 
    district = random.choice(districts.split())
    pincode = fake.zipcode()
    id_num = fake.random_number(digits=8)
    return [country,name, age, dob, language, state, district, pincode, id_num]


# Total Population  count 
num_rows=1500000000


# hard code valued India 
# For ever state the data is generated acording to the share count  of there population . by selecting respective state , language , districts
#

country='India'
for index, row in df.iterrows():
    id = row["Id"]
    language = row["language"]
    state = row["States"]
    share = row["Share"]
    districts = row["Districts"]
    share = int(num_rows*row["Share"])
# If it is one time use w+ . I am used a ( append ) 
    with open('India_population.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(share):
            pop = generate_row()
            writer.writerow(pop)

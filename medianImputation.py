import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os as os

#load data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

#eliminate category data

# Get the categorical and numeric columns
category_columns = [
    'ProductCD', 'card1', 'card2', 'card3', 'card4', 'card5', 'card6',
                   'addr1', 'addr2', 'P_emaildomain', 'R_emaildomain', 'DeviceType', 'DeviceInfo',
                   'M1','M2','M3','M4','M5','M6','M7','M8','M9',"id_12",
                   "id_13","id_14","id_15","id_16","id_17","id_19","id_20",
                   "id_28","id_29","id_30","id_31","id_32","id_33",
                   "id_34","id_35","id_36","id_37","id_38"]

numeric_columns = list(set(train.columns) - set(category_columns))

#Dealing with those NAN value in numeric columns

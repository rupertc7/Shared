# Purpose:  splits data set csv into training and validation sets - sagemaker canvas
# How:      using split and pandas
# Status:   it works
# Elements: 
# Imports:  import pandas as pd      from sklearn.model_selection import train_test_split
# Author:   AWS
# Date:     2023-11-15
# Note:     part of a lab
#______________________________________________________________________
# split_datasets.py

#!/usr/bin/env python3
import pandas as pd
from sklearn.model_selection import train_test_split

# load the filename into a variable
data_location = 'storedata_total.csv'

# Use Pandas to read the CSV into a dataframe.
df = pd.read_csv(data_location)

# print the current column names and first ten records.
print(df.head(10))

# Transform the values in the retained column from 0 and 1, to N and Y.
df['retained'] = df['retained'].replace([0, 1],['N', 'Y'])

# Print the transformation
print(df.head(10))

#Split transformed dataset into training and validation sets
train_data, val_data = train_test_split(df, test_size=0.2, random_state=30)    

print("Training Data : {} Features, {} Records".format(train_data.shape[1], train_data.shape[0]))
print("Validation Data : {} Features, {} Records".format(val_data.shape[1], val_data.shape[0]))

train_data.to_csv('training_data.csv', header=True, index=False)
val_data.to_csv('validation_data.csv', header=True, index=False)

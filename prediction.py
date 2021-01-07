#Import Modules
#import pandas as pd
#import numpy as np
#import seaborn as sns
#import pandas as pd
#from sklearn.linear_model import LinearRegression
#rom sklearn.model_selection import train_test_split
#import tensorflow.keras as kr

## Import data from csv file
#df = pd.read_csv("./powerproduction.csv")
#
## load the dataset
#data = df.values
#
## choose the input and output variables
#x = data[:, 0] 
#y = data[:, 1]
#
## split data into training and testing sets
#
## split the data set into training and testing set with 33% of the data in test set
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=1)
#
## Train a model.
#model = kr.models.Sequential()
#model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
#model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
#model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')
#
##print(model.summary()) Test function
#
##Fit model
#model.fit(x_train, y_train, epochs=600, batch_size=10)
#
#def predict(speed):
#    prediction = model.predict([speed])
#    return str(prediction[0][0])

def test():
    print("Test of prediction program")

#print(predict(10))

from tensorflow.keras.models import load_model

#model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
#del model  # deletes the existing model

# returns a compiled model
# identical to the previous one
model = load_model('./my_model.h5')

test()
print(model.predict([15.0]))
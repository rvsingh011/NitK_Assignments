import csv
import pandas as pd
from pandas import read_csv, DataFrame
from numpy.random import seed
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split
from keras.layers import Input, Dense
from keras.models import Model
from keras.callbacks import LambdaCallback
from keras.callbacks import ModelCheckpoint
import numpy	



'''
Use of Autoencoder for dimensionality reduction with single layer of input, hidden and output layers, where the no of nodes corresponding to input layer is equal to the no of features present in input layer, no of nodes in hidden layer is equal to the no of feature we want in out output. Here for dimensionality reduction we are only using the encoding of input dimension to reduced dimension. 


### SPARSE AUTOENCODER ###
# InputLayer (None, no of feature in input file)
#      Dense (None, 100)

'''

 
# Reading the input as csv file  
df = read_csv("train_in.csv")
Y = df
X = df.ix[:,:]


# Scale each feature into [0, 1] range 
sX = minmax_scale(X, axis = 0)

# Finding out the no of dimension present in the input file
ncol = sX.shape[1]

# Dividing our given csv file for training and testing, we can change the size of traing dataset by changing the value of "train_size"(value assigned to this must be in between 0 and 1)
X_train, X_test, Y_train, Y_test = train_test_split(sX, Y, train_size = 0.5, random_state = seed(2017))
print X_train
print X_test
print Y_train
print Y_test 
# Defining the input layer 
input_dim = Input(shape = (ncol, ))

# Defining dimension for encoder
encoding_dim = 3

# Defining the hidden or encoding layer 
encoded = Dense(encoding_dim, activation = 'relu')(input_dim)
encoded1 = Dense(ncol, activation = 'sigmoid')(encoded)

# Specifing the parameters to the auto encoder model
autoencoder = Model(input = input_dim, output = encoded1)



#print_weights = keras.callbacks.LambdaCallback(on_epoch_end=lambda batch, logs: print())



# Configure and train the autoencoder model , with given optimized and loss function for calculating the error_weight of the nodes in input layer and here we are using 50 epochs to get efficient dimensions slected in our output data. we can change value of "nb_epoch" to get different output or efficent output
autoencoder.compile(optimizer = 'adadelta', loss = 'binary_crossentropy')

# checkpoint
#filepath="weights.hdf5"
#checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
#checkpointer = [checkpoint]

checkpoint = ModelCheckpoint(filepath='weights.hdf5', monitor='val_loss',mode='min' , verbose=1, save_weights_only=True, save_best_only=True , period=1)
print "heyyyy"


autoencoder.fit(X_train, X_train, epochs = 20, batch_size = 100, shuffle = True, validation_data = (X_test, X_test), callbacks=[checkpoint])
print X_test
# The encoder to extract reduced dimension feature fron the above autoencoder model
encoder = Model(input = input_dim, output = encoded)
encoded_input = Input(shape = (encoding_dim, ))
encoded_out = encoder.predict(sX)
encoded_out[0:2]
#print encoded_out[0:2]
# Store the output as reduced dimension into the another csv file called "foo1.csv"


#autoencoder.load_weights("weights.best.hdf5")
# Compile model (required to make predictions)
#autoencoder.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#print("Created model and loaded weights from file")
# load pima indians dataset





columns = [i for i in range(1,4)]
a=str(columns).strip('[]')
print a



'''with open('foo2.csv', 'w') as csvfile:
        #fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        writer.writeheader()'''

#with open('foo2.csv', 'wb') as csvfile:
#new_column = pd.DataFrame(columns)
#print new_column
    #writer = csv.DictWriter(csvfile, fieldnames = columns, delimiter = ';')
    #writer.writeheader()

numpy.savetxt("train_out.csv", encoded_out , delimiter="," , header=a, comments="")

#user1 = pd.read_csv('foo1.csv', names=columns, header=None)
'''ss
df = pd.read_csv('foo2.csv')
new_column = pd.DataFrame(columns)
df = df.merge(new_column, left_index = True, right_index = True)
df.to_csv('foo2.csv')'''











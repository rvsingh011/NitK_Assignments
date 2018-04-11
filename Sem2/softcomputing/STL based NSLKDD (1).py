
# coding: utf-8

# In[71]:


# Here are some imports that are used along this notebook
import math
import itertools
import pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import seaborn as sns
from time import time
import tensorflow as tf
from collections import OrderedDict
import keras
from sklearn.model_selection import KFold
from keras.utils import np_utils
# get_ipython().run_line_magic('matplotlib', 'inline')
gt0 = time()


# In[72]:


train20_nsl_kdd_dataset_path = "NSL_KDD_Dataset/KDDTrain+_20Percent.txt"
train_nsl_kdd_dataset_path = "NSL_KDD_Dataset/KDDTrain+.txt"
test_nsl_kdd_dataset_path = "NSL_KDD_Dataset/KDDTest+.txt"


# In[73]:


col_names = np.array(["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","labels"])


# In[74]:


nominal_inx = [1, 2, 3]
binary_inx = [6, 11, 13, 14, 20, 21]
numeric_inx = list(set(range(41)).difference(nominal_inx).difference(binary_inx))


# In[75]:


nominal_cols = col_names[nominal_inx].tolist()
binary_cols = col_names[binary_inx].tolist()
numeric_cols = col_names[numeric_inx].tolist()


# In[76]:


# Dictionary that contains mapping of various attacks to the four main categories
attack_dict_five_class = {
    'normal': 'normal',
    
    'back': 'DoS',
    'land': 'DoS',
    'neptune': 'DoS',
    'pod': 'DoS',
    'smurf': 'DoS',
    'teardrop': 'DoS',
    'mailbomb': 'DoS',
    'apache2': 'DoS',
    'processtable': 'DoS',
    'udpstorm': 'DoS',
    
    'ipsweep': 'Probe',
    'nmap': 'Probe',
    'portsweep': 'Probe',
    'satan': 'Probe',
    'mscan': 'Probe',
    'saint': 'Probe',

    'ftp_write': 'R2L',
    'guess_passwd': 'R2L',
    'imap': 'R2L',
    'multihop': 'R2L',
    'phf': 'R2L',
    'spy': 'R2L',
    'warezclient': 'R2L',
    'warezmaster': 'R2L',
    'sendmail': 'R2L',
    'named': 'R2L',
    'snmpgetattack': 'R2L',
    'snmpguess': 'R2L',
    'xlock': 'R2L',
    'xsnoop': 'R2L',
    'worm': 'R2L',
    
    'buffer_overflow': 'U2R',
    'loadmodule': 'U2R',
    'perl': 'U2R',
    'rootkit': 'U2R',
    'httptunnel': 'U2R',
    'ps': 'U2R',    
    'sqlattack': 'U2R',
    'xterm': 'U2R'
}

attack_two_class = []
for key in attack_dict_five_class.keys():
    if key == 'normal':
        pass
    else:
        attack_two_class.append(key)


# In[77]:


#Load test and train data
train_df = pd.read_csv(train_nsl_kdd_dataset_path, names = col_names)
test_df  = pd.read_csv(test_nsl_kdd_dataset_path , names = col_names)
train_labels = train_df.pop('dst_host_srv_rerror_rate')
test_labels = test_df.pop('dst_host_srv_rerror_rate')
total_dataset = pd.concat([train_df, test_df])
print(total_dataset.shape)


# In[78]:


# check for null values
total_dataset[total_dataset.isnull().any(axis=1)]



# In[79]:


test_df.head()


# In[80]:


total_dataset = pd.get_dummies(total_dataset)
print(total_dataset.shape)
train_df = total_dataset.iloc[0:125973, :]
test_df = total_dataset.iloc[125973:, :]
print(test_df.shape, test_df.shape)


# In[81]:


train_labels_for_two_class = pd.DataFrame(train_labels.as_matrix(), columns=["class"])
test_labels_for_two_class = pd.DataFrame(test_labels.as_matrix(), columns=["class"])


# In[82]:


train_labels_for_two_class.loc[train_labels_for_two_class['class'].isin(attack_two_class) , 'class'] = 1
train_labels_for_two_class.loc[train_labels_for_two_class['class'] == "normal" , 'class'] = 0
#for test labels 
test_labels_for_two_class.loc[test_labels_for_two_class['class'].isin(attack_two_class) , 'class'] = 1
test_labels_for_two_class.loc[test_labels_for_two_class['class'] == "normal" , 'class'] = 0


# In[87]:


train_labels_for_two_class = np_utils.to_categorical(train_labels_for_two_class)
test_labels_for_two_class = np_utils.to_categorical(test_labels_for_two_class)


# In[98]:


#min-max mazimazation for the data
from sklearn.preprocessing import MinMaxScaler
train_X = train_df.as_matrix()
train_Y = train_labels_for_two_class

test_X = test_df.as_matrix()
test_Y = test_labels_for_two_class
scaler = MinMaxScaler() 
scaler.fit_transform(train_X)
scaler.fit_transform(train_Y)
scaler.fit_transform(test_X)
scaler.fit_transform(test_Y)
# train_X = train_X[0]
# train_Y = train_Y[0]
# test_X = test_X[0]
# test_Y = test_Y[0]


# In[99]:


#Training our auto encoder

import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy import stats
import tensorflow as tf
import seaborn as sns
from pylab import rcParams
from sklearn.model_selection import train_test_split
from keras.models import Model, load_model
from keras.layers import Input, Dense
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras import regularizers



# In[109]:


input_dim = train_X.shape[1]
input_layer = Input(shape=(input_dim, ))
encoder = Dense(30, activation="sigmoid", 
                activity_regularizer=regularizers.l1(10e-5))(input_layer)
decoder = Dense(input_dim, activation='relu')(encoder)
autoencoder = Model(inputs=input_layer, outputs=decoder)


# In[106]:


nb_epoch = 1
batch_size = 64
autoencoder.compile(optimizer='adam', 
                    loss='mean_squared_error', 
                    metrics=['accuracy'])
checkpointer = ModelCheckpoint(filepath="model.h5",
                               verbose=0,
                               save_best_only=True)

tensorboard = TensorBoard(log_dir='./logs',
                          histogram_freq=0,
                          write_graph=True,
                          write_images=True)

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

history = autoencoder.fit(train_X,train_X ,
                    epochs=nb_epoch,
                    verbose = 1,
                    batch_size=batch_size,
                    shuffle=True,
                    validation_data=(test_X, test_X),
                    callbacks=[checkpointer, tensorboard]).history


# In[110]:


encoder = Model(input_layer, encoder)


# In[111]:


out2 = Dense(2, activation='softmax')(encoder.output)
newmodel = Model(encoder.input,out2)


# In[112]:


test_X.shape


# In[126]:


from keras import optimizers
opt = optimizers.SGD(lr=0.01)
newmodel.compile(loss='categorical_crossentropy',
          optimizer=opt, 
          metrics=['accuracy']) 

newmodel.fit(train_X, train_Y,
      epochs=1,
      batch_size=128,
      shuffle=True,
      validation_data=(test_X, test_Y))


# In[124]:


scores = newmodel.evaluate(test_X, test_Y, verbose=1, steps=50) 
print("Accuracy: ", scores[1])
 


# In[ ]:





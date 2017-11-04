from keras.models import Sequential
from keras.layers import Dense
import numpy as np

X_train = np.array([[0,0,0,1,1], [0,1,1,1,1], [1,0,1,0,1], [1,0,1,1,1], [1,0,1,1,1]])
Y_train = np.array([0, 0, 0, 0, 1])
model = Sequential()
model.add(Dense(units=3,activation='tanh',use_bias=True, input_dim=5))
model.add(Dense(units=5,activation='tanh'))
model.add(Dense(1, activation='tanh'))
model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])
model.summary()
model.fit(X_train, Y_train, batch_size=2, epochs=100, verbose=1)

output = model.predict(np.array([[1,0,0,0,1]]))
print(output)
print(round(output[0,0]))


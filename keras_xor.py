import numpy as np
from keras.models import Sequential #keras uses tensor flow behind the scenes
from keras.layers.core import Activation, Dense

# the four different states of the XOR gate
training_data = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
], "float32")

# the four expected results in the same order
target_data = np.array([
  [0],
  [1],
  [1],
  [0]
], "float32")

# Choose the model type
model = Sequential()

# Specify the layered nodes of the network
model.add(
  Dense(16, 
    input_dim=2, #since the input is two dimensional
    activation='relu' #the activation function to use
  )
)

# Add another layer to map to the single output
model.add(
  Dense(1, 
    activation='sigmoid'
  )
)

# Specify the loss and optimization function
model.compile(loss='mean_squared_error',
  optimizer='adam',
  metrics=['binary_accuracy'] # metrics for the end user to see when in verbose mode
)

model.fit(
  training_data, 
  target_data, 
  nb_epoch=284, #number of iterations to run 
  # It gets smarter every iteration 
  # But too many iterations will actually make it overthink and create patterns that do not exist)
  verbose=2 # output the results
)

# predict and print the output
print model.predict(np.array([
    [1,0],
    [1,1]
], "float32")).round() #rounds off the output result
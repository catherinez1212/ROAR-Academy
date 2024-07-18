# Load dependencies
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# Create data
linearSeparableFlag = False
x_bias = 6

def toy_2D_samples(x_bias, linearSeparableFlag):
    label1 = np.array([[1, 1], [-1, -1]])
    label2 = np.array([[1, -1], [-1, 1]])

    if linearSeparableFlag:
        samples1 = np.random.multivariate_normal([5 + x_bias, 0], [[1, 0], [0, 1]], 100)
        samples2 = np.random.multivariate_normal([-5 + x_bias, 0], [[1, 0], [0, 1]], 100)
        samples = np.concatenate((samples1, samples2), axis=0)
        
        # Plot the data
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'rx')
        plt.show()
    else:
        samples1 = np.random.multivariate_normal([5 + x_bias, 5], [[1, 0], [0, 1]], 50)
        samples2 = np.random.multivariate_normal([-5 + x_bias, -5], [[1, 0], [0, 1]], 50)
        samples3 = np.random.multivariate_normal([-5 + x_bias, 5], [[1, 0], [0, 1]], 50)
        samples4 = np.random.multivariate_normal([5 + x_bias, -5], [[1, 0], [0, 1]], 50)
        samples = np.concatenate((samples1, samples2, samples3, samples4), axis=0)
        
        # Plot the data
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'bo')
        plt.plot(samples3[:, 0], samples3[:, 1], 'rx')
        plt.plot(samples4[:, 0], samples4[:, 1], 'rx')
        plt.show()

    labels1 = np.repeat(label1, 100, axis=0)
    labels2 = np.repeat(label2, 100, axis=0)
    labels = np.concatenate((labels1, labels2), axis=0)
    return samples, labels

samples, labels = toy_2D_samples(x_bias, linearSeparableFlag)

# Split training and testing set
randomOrder = np.random.permutation(200)
trainingX = samples[randomOrder[0:100], :]
trainingY = labels[randomOrder[0:100], :]
testingX = samples[randomOrder[100:200], :]
testingY = labels[randomOrder[100:200], :]

# Build the model
model = Sequential()
model.add(Dense(2, input_shape=(2,), activation='linear', use_bias=True))
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['binary_accuracy'])

# Train the model
model.fit(trainingX, trainingY, epochs=500, batch_size=10, verbose=2, validation_split=0.2)

# Evaluate the model
score = 0
for i in range(100):
    predict_x = model.predict(np.array([testingX[i, :]]), verbose=0)
    estimate = np.argmax(predict_x, axis=1)
    correct_class = np.argmax(testingY[i, :])
    
    if correct_class == estimate:
        score += 1

    if estimate == 0:
        plt.plot(testingX[i, 0], testingX[i, 1], 'bo')
    else: 
        plt.plot(testingX[i, 0], testingX[i, 1], 'rx')

print('Test accuracy:', score / 100)
plt.show()

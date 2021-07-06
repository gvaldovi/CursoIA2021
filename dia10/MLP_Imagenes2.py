

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import cv2


mnist = keras.datasets.mnist

(train_images, train_labels),(test_images, test_labels) = mnist.load_data()

plt.figure()
plt.imshow(test_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

class_name = ['0','1','2','3','4','5','6','7','8','9']

train_images=train_images/255
test_images = test_images/255

plt.figure()
plt.imshow(test_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

plt.figure(figsize=(10,10))
for i in range(50):
    plt.subplot(5,10,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i],cmap='gray')
    plt.xlabel(class_name[train_labels[i]])
plt.show()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(7,activation='relu'),
    keras.layers.Dense(5,activation='relu'),
    keras.layers.Dense(10,activation='softmax')
])

model.summary()

model.compile(loss='sparse_categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])


#model.fit(train_images,train_labels,epochs=10)
history = model.fit(train_images,train_labels,
                    batch_size=28,
                    epochs=10,
                    verbose=1,
                    validation_data=(test_images,test_labels))

_,test_acc = model.evaluate(test_images,test_labels)
print('Precisión:',test_acc)

cantNums = 10

indices = np.random.randint(test_images.shape[0] - cantNums,size=cantNums)
predicciones = model.predict(test_images[indices,:])

print(predicciones)
print(predicciones[0,:])
print(np.argmax(predicciones[0,:]))

plt.figure(figsize=(30,10))
for i in range(indices.shape[0]):
    plt.subplot(2,5,i+1)
    img = test_images[indices[i],:]
    plt.imshow(img,cmap='gray')
    plt.title("Predicción: "+str(np.argmax(predicciones[i,:])) + ", Número real: "
    + str(test_labels[indices[i]]))
plt.show()

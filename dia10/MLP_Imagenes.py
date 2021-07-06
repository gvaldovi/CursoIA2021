import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
import cv2

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels),(test_images, test_labels) = fashion_mnist.load_data()

train_images.shape

plt.figure()
plt.imshow(test_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images[0].shape
test_images.shape

train_labels.shape

train_labels[0]

np.min(train_labels)


class_name = ['Camiseta','Pantalón','Suéter','Vestido','Abrigo','Sandalia','Camisa','Zapatilla deportiva','Bolso','Botin']

test_images[0]

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
    keras.layers.Dense(15,activation='relu'),
    keras.layers.Dense(10,activation='softmax')
])

model.summary()

model.compile(loss='sparse_categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])


model.fit(train_images,train_labels,epochs=10)

test_loss,test_acc = model.evaluate(test_images,test_labels)
print('Presición:',test_acc)

prediccion = model.predict(test_images)

prediccion[0]

np.max(prediccion[0])

np.argmax(prediccion[0])

response = requests.get('https://www.turopalaboral.com/2893-home_default/camiseta-s6600-manga-corta-pack-3-unidades-workteam.jpg')

img=Image.open(BytesIO((response.content)))

img2=np.array(img)

plt.figure()
plt.imshow(img2)
plt.colorbar()
plt.grid(False)
plt.show()

img2.shape

img2 = 255 - img2

plt.figure()
plt.imshow(img2)
plt.colorbar()
plt.grid(False)
plt.show()

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.333,0.333,0.333])

img3=rgb2gray(img2)

plt.figure()
plt.imshow(img3)
plt.colorbar()
plt.grid(False)
plt.show()

img3.shape

img4 = cv2.resize(img3,dsize=(28,28),interpolation=cv2.cv2.INTER_CUBIC)

img4.shape

plt.figure()
plt.imshow(img4)
plt.colorbar()
plt.grid(False)
plt.show()

img4 = img4/255

plt.figure()
plt.imshow(img4)
plt.colorbar()
plt.grid(False)
plt.show()

x=np.zeros((1,28,28))

x[0]=np.array(img4)

prediccion2 = model.predict(x)

np.argmax(prediccion2[0])

index = np.arange(len(class_name))

plt.bar(index,prediccion2[0])
plt.ylabel('Confiabilidad',fontsize=15)
plt.xticks(index,class_name,fontsize=15,rotation=90)
plt.title('Predicción')
plt.show()

checkpoint_path = 'ckeckpoint/check'
cp_callbacks = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,save_weights_only=True)
model.fit(train_images,train_labels,epochs=10,callbacks=[cp_callbacks])

test_loss,test_acc = model.evaluate(test_images,test_labels)
print('Precisión:',test_acc)

model2 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(15,activation='relu'),
    keras.layers.Dense(10,activation='softmax')
])

model2.compile(loss='sparse_categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])

_,test_acc = model2.evaluate(test_images,test_labels)
print('Precisión:',test_acc)

model2.load_weights(checkpoint_path)

_,test_acc = model2.evaluate(test_images,test_labels)
print('Precisión:',test_acc)
test_loss,test_acc = model.evaluate(test_images,test_labels)
print('Precisión:',test_acc)

model2 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(15,activation='relu'),
    keras.layers.Dense(10,activation='softmax')
])

model2.compile(loss='sparse_categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])

_,test_acc = model2.evaluate(test_images,test_labels)
print('Precisión:',test_acc)

model2.load_weights(checkpoint_path)
_,test_acc = model2.evaluate(test_images,test_labels)
print('Precisión:',test_acc)
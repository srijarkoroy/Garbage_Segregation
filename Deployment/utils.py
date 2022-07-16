from tensorflow.keras.models import Sequential
from keras.layers import Conv2D, Flatten, MaxPooling2D, Dense, Dropout, SpatialDropout2D
from tensorflow.keras.losses import sparse_categorical_crossentropy, binary_crossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from PIL import Image

def gen_labels():
    train = '../Data/Train'
    train_generator = ImageDataGenerator(rescale = 1/255)

    train_generator = train_generator.flow_from_directory(train,
                                                        target_size = (300,300),
                                                        batch_size = 32,
                                                        class_mode = 'sparse')
    labels = (train_generator.class_indices)
    labels = dict((v,k) for k,v in labels.items())

    return labels

def preprocess(image):
    image = np.array(image.resize((300, 300), Image.ANTIALIAS))
    image = np.array(image, dtype='uint8')
    image = np.array(image)/255.0

    return image

def model_arc():
    model=Sequential()

    #Convolution blocks
    model.add(Conv2D(32, kernel_size = (3,3), padding='same',input_shape=(300,300,3),activation='relu'))
    model.add(MaxPooling2D(pool_size=2)) 

    model.add(Conv2D(64, kernel_size = (3,3), padding='same',activation='relu'))
    model.add(MaxPooling2D(pool_size=2)) 

    model.add(Conv2D(32, kernel_size = (3,3), padding='same',activation='relu'))
    model.add(MaxPooling2D(pool_size=2)) 

    #Classification layers
    model.add(Flatten())

    model.add(Dense(64,activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32,activation='relu'))

    model.add(Dropout(0.2))
    model.add(Dense(6,activation='softmax'))

    return model

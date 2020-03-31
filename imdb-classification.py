# -*- coding: utf-8 -*-
# Importing the libraries --------------------------------------------------------------------
import tensorflow as tf
import keras
from keras.datasets import imdb

# Assigning training and test data to respective variables -----------------------------------

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# Checking training set if imported properly -------------------------------------------------

train_data[0]
train_labels[0]
# Checking max is equal to or below 10000 words
max([max(sequence) for sequence in train_data])

#



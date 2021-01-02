import numpy as np
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import Adam
import tensorflow as tf
import data_helper as dh
import os
import pandas as pd
from tensorflow.keras.models import load_model

# model = load_model('FCmodel')
# print(model.get_config())
# y_pred = model.predict()

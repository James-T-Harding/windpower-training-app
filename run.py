from learning.dbbignetwork import *
from tensorflow.keras import Sequential, layers, metrics, regularizers
from tensorflow import optimizers

from pandas import DataFrame
import numpy

readings = get_readings()
length = int(len(readings)/2)

d1 = readings[:length]
d2 = readings[length:]

wind1, power1 = zip(*d1)

frame = DataFrame(wind1)
frame = frame.fillna(frame.mean()).dropna(axis=1)

mean = frame.mean()

input_size = len(mean),

w2, p2 = zip(*d2)

frame2 = DataFrame(w2)[dict(mean)].fillna(mean)

model = Sequential([
    layers.BatchNormalization(input_shape=input_size),
    layers.Dense(484, 'relu', kernel_regularizer=regularizers.l2(100)),
    layers.Dense(1)
])

model.compile(optimizers.Adam(), loss=metrics.mean_squared_error, metrics=[metrics.mean_absolute_error])

model.fit(frame.values, numpy.array(power1), epochs=100, verbose=0)
print(model.evaluate(frame2.values, numpy.array(p2)))


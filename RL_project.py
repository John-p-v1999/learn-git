
import tensorflow as tf
print(tf.__version__)
assert tf.config.list_physical_devices('GPU')
print('hello')
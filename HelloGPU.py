# -------------------------------------------------------
# メモリの制限 tensorflow-gpu (2.0.0)
# -------------------------------------------------------
import tensorflow as tf
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    for device in physical_devices:
        tf.config.experimental.set_memory_growth(device, True)
        print('memory growth:', tf.config.experimental.get_memory_growth(device))
else:
    print("Not enough GPU hardware devices available")

# -------------------------------------------------------
"""
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
"""#"""
# -------------------------------------------------------
#"""
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
"""#"""

batch_size = 4096
num_classes = 10
epochs = 20

# モデルの生成関数
def createModel():
    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(784,)))
    model.add(Dropout(0.2))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer=RMSprop(),
                  metrics=['accuracy'])
    return model

# Mnistデータのロード
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784) # 2次元配列を1次元に変換(訓練データ)
x_test = x_test.reshape(10000, 784) # 2次元配列を1次元に変換(テストデータ)
x_train = x_train.astype('float32') # int型をfloat32型に変換
x_test = x_test.astype('float32') # int型をfloat32型に変換
x_train /= 255                     # [0-255]の値を[0.0-1.0]に変換
x_test /= 255

# 正解ラベルのOne hot vector化
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# モデルの定義
model = createModel()

# 学習の実行
history = model.fit(x_train, y_train,  # 画像とラベルデータ
                    batch_size=batch_size,
                    epochs=epochs,     # エポック数の指定
                    validation_data=(x_test, y_test))

# モデル構成の確認
model.summary()

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
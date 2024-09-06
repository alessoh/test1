import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

class PostmortemAnalysisModel:
    def __init__(self, input_dim):
        self.model = Sequential([
            Dense(64, activation='relu', input_dim=input_dim),
            Dropout(0.2),
            Dense(32, activation='relu'),
            Dropout(0.2),
            Dense(16, activation='relu'),
            Dense(4, activation='softmax')  # Output layer for 4 agent roles
        ])
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def train(self, X_train, y_train, epochs=100, batch_size=32):
        return self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def save_model(self, filepath):
        self.model.save(filepath)

    @classmethod
    def load_model(cls, filepath):
        loaded_model = tf.keras.models.load_model(filepath)
        instance = cls(loaded_model.input_shape[1])
        instance.model = loaded_model
        return instance
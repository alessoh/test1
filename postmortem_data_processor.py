import pandas as pd
from sklearn.preprocessing import StandardScaler

class PostmortemDataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def collect_data(self, postmortem_results):
        data = []
        for result in postmortem_results:
            features = self.extract_features(result)
            data.append(features)
        return pd.DataFrame(data)

    def extract_features(self, result):
        # Assuming result is a CrewOutput object or a string representation of it
        # You may need to adjust this based on the actual structure of the result
        if isinstance(result, str):
            # If result is a string, we'll use some basic text analysis
            features = {
                'length': len(result),
                'word_count': len(result.split()),
                'sentence_count': result.count('.') + result.count('!') + result.count('?'),
                'average_word_length': sum(len(word) for word in result.split()) / len(result.split()) if result.split() else 0
            }
        else:
            # If result is an object, we'll try to extract some general attributes
            features = {
                'task_completion_time': getattr(result, 'task_completion_time', None),
                'accuracy_score': getattr(result, 'accuracy_score', None),
                'collaboration_score': getattr(result, 'collaboration_score', None),
                'efficiency_score': getattr(result, 'efficiency_score', None),
            }
        return features

    def preprocess_data(self, df):
        # Fill NaN values with the mean of the column
        df = df.fillna(df.mean())
        
        # Identify numerical features
        numerical_features = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        
        # Normalize numerical features
        if numerical_features:
            df[numerical_features] = self.scaler.fit_transform(df[numerical_features])
        
        return df
"""
*******************************************************************
                        -- Music Model --

Description: A model that uses a combination of k-means and k-
             nearest neighbor to recommend a user a number of
             songs based on their provided preferences.

Name: Gage Mather

*******************************************************************
"""

import os
import random
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

class MusicModel ():

    features = None
    music_df = None
    path_to_data = None
    kmeans = None
    n_neighbors = None
    scaler = None

    def __init__ (self):
        """ Initialization of path to dataset, pandas dataframe, models, and features to be used """

        self.features = [
            'danceability',
            'energy',
            'loudness',
            'acousticness',
            'instrumentalness',
            'liveness',
            'valence',
            'tempo'
        ]

        self.path_to_data = os.path.join("data","dataset.csv")
        self.music_df = pd.read_csv(self.path_to_data).drop('Unnamed: 0', axis=1) 
        self.kmeans = KMeans(n_clusters=500, n_init="auto", random_state=random.randint(1, 5)) 
        self.n_neighbors = NearestNeighbors(n_neighbors=5)
        

    def predict(self, prediction_data): 
        """
        This function scales the prediction and feeds it into the k-means model. 
        Once a cluster prediction is obtained from k-means, we select that cluster
        and fit that data to a k-nearest-neighbor model. We then feed the prediction data
        into the knn model and return the five closest songs.
        """

        assert prediction_data != None and len(prediction_data) == 8

        # Dimensionality reduction via PCA was originally conducted here but the need
        # for it vanished.
        prediction_data = pd.DataFrame([prediction_data], columns=self.features)
        print (prediction_data)
        transformed_data = self.scaler.transform(prediction_data)
        
        cluster_prediction = self.kmeans.predict(transformed_data)

        prediction_result = self.music_df[self.music_df['cluster_id'] == cluster_prediction[0]]
        self.n_neighbors.fit(prediction_result[self.features])

        indicies = self.n_neighbors.kneighbors(prediction_data, return_distance=False)
        return prediction_result.iloc[indicies[0]]['track_id']


    def train_model (self):
        """ 
        This function makes a scaled copy of the data and uses
        it to fit the k-means model. After the model is fit, a 
        new column in the original dataset is created to hold
        cluster assignments.
        """

        self.scaler = StandardScaler()
        features_scaled = self.scaler.fit_transform(self.music_df[self.features]) 

        self.kmeans.fit(features_scaled)

        cluster_labels = self.kmeans.labels_
        self.music_df['cluster_id'] = cluster_labels


if __name__ == "__main__": 

    # data format
    # danceability, energy, loudness, acousticness, instrumentalness, liveness, valence, tempo (in that order)
    
    # I beg you 5kKSQULHCPFE7CKMPrkAtP
    pred_data_values = [0.456, 0.893, -2.825,  0.00321, 0.0, 0.121, 0.478, 127.884]

    # fly me to the moon pt 2 5V0kQxkQeXNTnGNLRGZ6bX
    # pred_data_values = [0.322, 0.00207, -35.061, 0.996, 0.889, 0.0822, 0.149, 75.769]


    features = [
            'track_id',
            'track_name',
            'danceability',
            'energy',
            'loudness',
            'acousticness',
            'instrumentalness',
            'liveness',
            'valence',
            'tempo'
        ]
    
    K_model = MusicModel()

    K_model.train_model()
    pred_df = K_model.predict(pred_data_values)

    #print (pred_df.describe())
    print (pred_df)
    print (pred_data_values)
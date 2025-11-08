import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class MusicModel ():

    features = None
    music_df = None
    path_to_data = None
    kmeans = None
    pca = None
    scaler = None
    labels_assigned = False
    X_pca = None

    def __init__ (self):
        """ Initialization of path to dataset, pandas dataframe, model, and features to be used """

        self.features = [
            'danceability',
            'energy',
            'loudness',
            'speechiness',
            'acousticness',
            'instrumentalness',
            'liveness',
            'valence',
            'tempo'
        ]

        self.path_to_data = os.path.join("data","dataset.csv")
        self.music_df = pd.read_csv(self.path_to_data).drop('Unnamed: 0', axis=1) 
        self.kmeans = KMeans(n_clusters=500, init='k-means++', n_init="auto", random_state=42)


    def predict(self, prediction_data): 
        """
        This function transforms the prediction data using the scaler and pca objects
        defined by the "train_model" function. Currently, it returns 5 random samples
        from the cluster that was chosen by kmeans. 
        """

        prediction_data = pd.DataFrame([prediction_data], columns=self.features)

        # scale and conduct pca on input
        prediction_data = self.scaler.transform(prediction_data)
        prediction_data = self.pca.transform(prediction_data)

        # make cluster prediction
        cluster_prediction = self.kmeans.predict(prediction_data)

        # only assign lables once
        if self.labels_assigned is False:
            cluster_labels = self.kmeans.labels_
            self.music_df['cluster_id'] = cluster_labels
            self.labels_assigned = True

        # select 5 random samples from the cluster and return them
        prediction_result = self.music_df[self.music_df['cluster_id'] == cluster_prediction[0]]
        print(prediction_result.shape)
        return prediction_result.sample(n=5)


    def train_model (self):
        """ 
        This function is responisble for preforming scaling and pca on the original data.
        This function also fits the model to the transformed data.
        """

        # Standardize and conduct PCA
        self.scaler = StandardScaler()
        features_scaled = self.scaler.fit_transform(self.music_df[self.features])

        self.pca = PCA(n_components=0.70) 
        self.pca.fit(features_scaled)
        self.X_pca = self.pca.transform(features_scaled)

        # Train the K-Means Model
        self.kmeans.fit(self.X_pca)
    
    
if __name__ == "__main__":

    # Example predictions
    # danceability,energy,loudness,speechiness,acousticness,instrumentalness,liveness,valence,tempo

    # Drugs 3iiDWuaIzuGKZezHvQY4GA
    # pred_data_values = [0.77, 0.649, -6.824, 0.194, 0.108, 0.000683, 0.134, 0.522, 84.012]

    # I beg you 5kKSQULHCPFE7CKMPrkAtP
    # pred_data_values = [0.456, 0.893, -2.825, 0.0813, 0.00321, 0.0, 0.121, 0.478, 127.884]

    # fly me to the moon pt 2 5V0kQxkQeXNTnGNLRGZ6bX
    pred_data_values = [0.322, 0.00207, -35.061, 0.0523, 0.996, 0.889, 0.0822, 0.149, 75.769]
    
    
    K_model = MusicModel()

    K_model.train_model()
    print(K_model.predict(pred_data_values))
  

import pandas as pd
import os

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class MusicModel ():

    global features
    global music_df
    global path_to_data

    def __init__ (self):
        """ Initialization of path to dataset, pandas dataframe, and features to be used """
        
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


    def prediction(self, prediction_data, model, pca, scaler): 
        """
        This function transforms the prediction data using the passed scaler and pca objects.
        It also makes and returns the prediction.
        """
        
        features_scaled = scaler.transform(prediction_data)
        prediction_pca = pca.transform(features_scaled)

        return model.predict(prediction_pca)
        

    def model (self, prediction_data):
        """
        This function is responisble for preforming scaling and pca on the original data.
        It also passes the prediction data to the predict function. Once it gets the data
        back, it chooses 5 random entries in the original data frame corrisponding to the
        cluster the prediction made.
        """

        print (self.music_df[self.features].head())
        print (self.music_df.shape)

        # Standardize and conduct PCA
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(self.music_df[self.features])

        pca = PCA(n_components=0.85) 
        pca.fit(features_scaled)
        X_pca = pca.transform(features_scaled)
        print(f"Number of components selected: {pca.n_components_}")

        # Train the K-Means Model
        kmeans = KMeans(n_clusters=15, n_init="auto", random_state=42).fit(X_pca)

        # Make The Prediction
        pred_df = pd.DataFrame([prediction_data], columns=self.features)
        
        cluster_prediction = self.prediction(pred_df, kmeans, pca, scaler)
        print (f"Predicted Cluster: {cluster_prediction}")

        cluster_labels = kmeans.labels_
        self.music_df['cluster_id'] = cluster_labels

        prediction_result = self.music_df[self.music_df['cluster_id'] == cluster_prediction[0]].sample(n=5)
        return prediction_result


if __name__ == "__main__":

    # Example prediction
    
    pred_data_values = [0.268, 0.461, 0.568, -9.235, 0.569, 0.00133, 0.132, 0.143, 87.017]
    K_model = MusicModel()

    print(K_model.model(pred_data_values))



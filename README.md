# Machine Learning Music Recommender

This is a small web application that recommends people a few songs based off of a quiz in which the user provides their preferences. The model is trained on a very large kaggle dataset of various songs obtained from the spotify API (more than 100k entries).

The data has been cleaned to remove entries containing the same song id which brings it down to about 80k entries.

As for the model itself, It primarily uses Scikit learn's K-means model. The idea of recommending songs via this model is to first train it on the dataset. Once trained, the labels from the k-means model are obtained and applied to the dataset. This creates "pools" of tracks with all tracks being close in terms of feature parameters. When a prediction is made, the model will predict which cluster or pool the song belongs to. Once a cluster prediction is made, a different k-nearest-neighbor model trained on the data from the predicted cluster. Finally, the user's preferences are fed into the KNN model which yields the final prediction (a list of 5 songs).

## Running The Application Via Docker

To run the application cd to the root directory of the application and use the following commands...

    # this command builds the container for the web app
    docker build -t (your-name-for-image) .

and...
    
    # runs the container on 127.0.0.1:5000 or localhost:5000
    docker run -d --name (your-container-name) -p 5000:5000 (your-name-for-image)

It should be noted that the parenthesis around the names should be excluded. It should also be noted that "(your-name-for-image)" must match in both commands.

The created container can be stopped by using...
    
    docker stop (your-container-name)

and started again by using...

    docker start (your-container-name)


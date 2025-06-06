# CONFIGURATION FILE

# Path to the directory where the dataset is stored
PATH = './dataset'

# Path to the directory where the balanced dataset is stored
PREDICTION_PATH = './new_datasets/streaming'
BALANCED_TRAIN_PATH = './new_datasets/train.csv'

# Path to the directory where the figures are stored
FIGURES_PATH = './figures'

# Path to the directory where the model is stored
MODEL_PATH = './model'

# Define the Kafka topic name and the bootstrap server
BOOTSTRAP_SERVER = 'localhost:9092'
TOPIC_NAME = 'traffic-data'

pca_bool = True  # Set to True to use PCA for dimensionality reduction
cross_validation_bool = True  # Set to True to use cross-validation

pca_k = 12 # Number of principal components to keep
cross_validation_folds = 5 # Number of folds for cross-validation   



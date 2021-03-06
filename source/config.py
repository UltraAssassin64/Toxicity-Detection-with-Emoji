__author__ = "Baishali Dutta"
__copyright__ = "Copyright (C) 2021 Baishali Dutta"
__license__ = "Apache License 2.0"
__version__ = "0.1"

# -------------------------------------------------------------------------
#                               Configurations
# -------------------------------------------------------------------------
EMBEDDING_DIMENSION = 100
EMBEDDING_FILE_LOC = '../model/glove/glove.6B.' + str(EMBEDDING_DIMENSION) + 'd.txt'
TRAINING_DATA_LOC = '../data/train.csv'
TEST_DATA_LABEL = '../data/test_labels.csv'
TEST_DATA_COMMENTS = '../data/test.csv'
MAX_VOCAB_SIZE = 21661
MAX_SEQUENCE_LENGTH = 100
BATCH_SIZE = 128
EPOCHS = 30
VALIDATION_SPLIT = 0.2
DETECTION_CLASSES = [
    'neutral',
    'toxic'
]
MODEL_LOC = '../model/comments_toxicity.h5'
TOKENIZER_LOC = '../model/tokenizer.pickle'

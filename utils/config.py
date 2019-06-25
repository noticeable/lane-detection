"""
    This file contains constants used throughout the project
    as well as a configuration class, which is used as a
    training utility.
"""
# data constants PC-specific (!absolute paths)
# data
tr_root = '/Users/nick/Desktop/train_set/clips/'
tr_subdirs = ['0601', '0531', '0313-1', '0313-2']
tr_flabels = ['/Users/nick/Desktop/train_set/label_data_0601.json',
           '/Users/nick/Desktop/train_set/label_data_0531.json',
           '/Users/nick/Desktop/train_set/label_data_0313.json']

ts_root = '/Users/nick/Desktop/test_set/clips/'
ts_subdirs = ['0601', '0531', '0530']
ts_flabels = ['/Users/nick/Desktop/test_set/test_labels.json']


class Configs:

    def __init__(self):
        # hyperparameters
        self.epochs = 30
        self.init_lr = 0.01
        self.batch_size = 5
        self.workers = 4
        self.momentum = 0.9
        self.weight_decay = 0.0001
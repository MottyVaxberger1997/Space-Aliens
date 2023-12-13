import re
from typing import Set

import numpy as np
from sklearn.datasets import fetch_20newsgroups

# Load the 20newsgroups dataset
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
train_data = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
test_data = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
print(len(train_data.data), len(test_data.data))
print(len(train_data.data))
print(len(test_data.data))
data = np.array(train_data.data)


def tokenize(data_train: str) -> Set[str]:
    text = data_train.lower()
    all_words = re.findall("[a-z0-9']+", text)
    return set(all_words)


def design_data(data_train):
    pass


def split(new_data, target):
    return (new_data(new_data[np.where(target == 0)], new_data[np.where(target == 1)],
                     new_data[np.where(target == 2)], new_data[np.where(target == 3)]))


print(split(train_data, train_data.target))

# alt_atheism_messages = [(text, 'alt.atheism') for text in train_data.data if 'alt.atheism' in train_data.target_names]
# soc_religion_christian_messages = [(text, 'soc.religion.christian') for text in train_data.data
#                                    if 'soc.religion.christian' in train_data.target_names]
# comp_graphics_messages = [(text, 'comp.graphics') for text in train_data.data
#                           if 'comp.graphics' in train_data.target_names]
# sci_med_messages = [(text, 'sci.med') for text in train_data.data if 'sci.med' in train_data.target_names]

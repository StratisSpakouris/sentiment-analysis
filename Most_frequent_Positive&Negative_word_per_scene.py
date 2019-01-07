from Sentiment_analysis_project import *

# Store all positive and negative dictionaries in lists
pos_dicts_list = pos_per_scene(scenes_cleaning(split_scenes(ms_data)))[1]
neg_dicts_list = neg_per_scene(scenes_cleaning(split_scenes(ms_data)))[1]

# Find the most frequent positive word for each scene
most_freq_pos_words = []
for pos_diction in pos_dicts_list:
    most_freq_positive = max(pos_diction, key=pos_diction.get)
    most_freq_pos_words.append(most_freq_positive)

# Find the most frequent negative word for each scene
most_freq_neg_words = []
for neg_diction in neg_dicts_list:
    most_freq_negative = max(neg_diction, key=neg_diction.get)
    most_freq_neg_words.append(most_freq_negative)

# Create dataframe of the two lists
table = pd.DataFrame({'Most frequent positive words': most_freq_pos_words,
            'Most frequent negative words': most_freq_neg_words})

# Adjust the index names
for i in range(10):
    new_table = table.rename(index={i-1: 'Scene ' + str(i) for i in range(1,11)})

# Align each column
freq_table = new_table.style.set_properties(**{'text-align': 'center'})
display(freq_table)

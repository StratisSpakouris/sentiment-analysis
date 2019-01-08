import re
import pandas as pd
#import numpy as np
from IPython.display import display

# Open and read file
ms = open('midsummer.txt')
ms_data = ms.read()


def split_scenes(text):
    '''
    Split the text into 10 scenes.
    '''
    # Text preprocessing to get the scenes of the play individually
    first_4_acts = ms_data.split('ACT V')[0]

    # get the first 4 acts splitted
    splitted_acts = first_4_acts.split(
        'ACT I' or 'ACT II' or 'ACT III' or 'ACT IV' or 'ACT V')

    # remove the first element which is the introduction
    splitted_acts.pop(0)

    # get the 5th act
    act5 = ms_data.split('ACT V')[1]

    # combine all the acts in a list
    splitted_acts.append(act5)

    # Split the 5 acts into scenes
    scenes = []
    for act in splitted_acts:
        for scene in act.split('SCENE II'):
            scenes.append(scene)

    return scenes
# ---------------------------------------------------------


# Open and read files
pos_txt = open('positive-words.txt', encoding='latin-1')
pos_read = pos_txt.readlines()
neg_txt = open('negative-words.txt', encoding='latin-1')
neg_read = neg_txt.readlines()

# ---- Preprocessing of the lexicons ----

# Delete the the introductions and keep only the words
del pos_read[0:35]
del neg_read[0:37]

# Clean the words from character \n
pos_list = list(map(lambda s: s.strip(), pos_read))
neg_list = list(map(lambda s: s.strip(), neg_read))

# Extend POSITIVE lexicon with words that end with "'d". This is because there
# are some words of this type in the text and otherwise cannot be recognised.
modified_pos = []
for word in pos_list:
    if word[-1] == 'd' and word[-2] == 'e':
        new_string = word[:-2] + word[-2:].replace("e", "'")
        modified_pos.append(new_string)

pos_list.extend(modified_pos)

# Extend NEGATIVE lexicon with words that end with "'d". This is because there
# are some words of this type in the text and otherwised cannot be recognised.
modified_neg = []
for word in pos_list:
    if word[-1] == 'd' and word[-2] == 'e':
        new_string = word[:-2] + word[-2:].replace("e", "'")
        modified_neg.append(new_string)

neg_list.extend(modified_neg)


# ---- Preprocessing of the text ----

def scenes_cleaning(scenes):
    '''
    Clears each word from special characters
    '''
    # Split each scene into single strings
    splitted_scenes = []
    for i in range(len(scenes)):
        split_scene = scenes[i].split()
        splitted_scenes.append(split_scene)

    # Clean the words of each scene from character \n
    stripped_scenes = []
    for scene in splitted_scenes:
        stripped = list(map(lambda s: s.strip(), scene))
        stripped_scenes.append(stripped)

    # Clean each word in each scene from special characters
    cleaned_scenes = []
    for scene in stripped_scenes:
        scene_cl = []
        for ele in scene:
            cleaned = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "",
                             ele.replace("[", "").replace("]", "").lower())
            scene_cl.append(cleaned)
        cleaned_scenes.append(scene_cl)

    return cleaned_scenes


# ---- Measuring the positivity/negativity of the text ----
# Measure used: ratio (# of positive words/# of negative words) for each scene.
# By this measure we can see the strength of polarity for each scene.

def pos_per_scene(scenes):
    '''
    Finds the total number of positive words for each scene.
    '''
    pos_sums = []
    all_pos_dicts = []
    for scene in scenes:
        pos_dict = {}
        pos_sum = []
        for word in scene:
            if word in pos_list:
                if word not in pos_dict.keys():
                    pos_dict[word] = 1
                else:
                    pos_dict[word] += 1

        sum_scene = sum(pos_dict.values())
        pos_sums.append(sum_scene)
        all_pos_dicts.append(pos_dict)

    return pos_sums, all_pos_dicts


def neg_per_scene(scenes):
    '''
    Finds the total number of negative words for each scene.
    '''
    neg_sums = []
    all_neg_dicts = []
    for scene in scenes:
        neg_dict = {}
        neg_sum = []
        for word in scene:
            if word in neg_list:
                if word not in neg_dict.keys():
                    neg_dict[word] = 1
                else:
                    neg_dict[word] += 1

        sum_scene = sum(neg_dict.values())
        neg_sums.append(sum_scene)
        all_neg_dicts.append(neg_dict)

    return neg_sums, all_neg_dicts


def compare_scenes(positives, negatives):
    '''
    Compares the number of positive and negative words in each scene
    and returns the respective message.
    '''
    scene_ratio = []
    outputs = []
    for i in range(len(positives)):
        ratio = positives[i] / negatives[i]
        if ratio > 1:
            outputs.append(
                'Scene {} is positive with ratio {:.3f}'.format(i + 1, ratio))
            scene_ratio.append(ratio)
        elif ratio < 1:
            outputs.append(
                'Scene {} is negative with ratio {:.3f}'.format(i + 1, ratio))
            scene_ratio.append(ratio)
        else:
            outputs.append(
                'Scene {} is neutral with ratio {:.3f}'.format(i + 1, ratio))
            scene_ratio.append(ratio)
    return scene_ratio, outputs


print('Positive words per scece: ', pos_per_scene(
    scenes_cleaning(split_scenes(ms_data)))[0])
print('Negative words per scene: ', neg_per_scene(
    scenes_cleaning(split_scenes(ms_data)))[0])
display(compare_scenes(pos_per_scene(scenes_cleaning(split_scenes(ms_data)))[
    0], neg_per_scene(scenes_cleaning(split_scenes(ms_data)))[0])[1])

from Midsummer_SentimentAnalysis import split_scenes, ms_data

# Split each scene by lines
scenes_list = []
for s in split_scenes(ms_data):
    scenes_list.append(s.splitlines())

# Find one-word lines in the whole text
one_word_lines = []
for s in scenes_list:
    for line in s:
        if len(line.split()) == 1:
            one_word_lines.append(line)

# List with the name of each character
char_names = ['THESEUS', 'EGEUS', 'LYSANDER', 'DEMETRIUS', 'PHILOSTRATE', 'QUINCE', 'SNUG',
              'BOTTOM', 'FLUTE', 'SNOUT', 'STARVELING', 'HIPPOLYTA', 'HERMIA', 'HELENA', 'OBERON',
              'TITANIA', 'PUCK', 'PEASBLOSSOM', 'COBWEB', 'MOTH', 'MUSTARDSEED', 'PYRAMUS', 'THISBE',
              'WALL', 'MOONSHINE', 'LION']

# Create dictionary with names as keys
names_dict = dict([(name, 0) for name in char_names])

# Compare each word in the 'one word lines' list with each name in the 'character names' list
for word in one_word_lines:
    for name in char_names:
        if word == name:
            names_dict[name] += 1

print('The character who speaks the most is: {}'.format(max(names_dict, key=names_dict.get)))

from Midsummer_SentimentAnalysis import *

# Two lists of positive & negative words respectively
pos_words = pos_per_scene(scenes_cleaning(split_scenes(ms_data)))[0]
neg_words = neg_per_scene(scenes_cleaning(split_scenes(ms_data)))[0]
ratios = compare_scenes(pos_per_scene(scenes_cleaning(split_scenes(ms_data)))[
                        0], neg_per_scene(scenes_cleaning(split_scenes(ms_data)))[0])[0]

# the x locations for the scenes
ind = np.arange(10)

# the width of the bars
width = 0.35

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
plt.subplots_adjust(wspace=0.3)

rects1 = ax1.bar(ind, pos_words, width, color='g')
rects2 = ax1.bar(ind + width, neg_words, width, color='r')

ax1.set_ylabel('# of words', rotation=0, labelpad=40)
ax1.set_xlabel('Scenes', labelpad=20)
ax1.set_title('Positive & Negative words per scene')
ax1.set_xticks(ind + width / 2)
ax1.set_xticklabels(np.arange(1, 11))
ax1.legend(labels=['+ words', '- words'])

# Green bars if ratio > 1 and red bars if ratio < 1
colormat = np.where([i > 1 for i in ratios], 'g', 'r')
ratios_plot = ax2.bar(ind, ratios, color=colormat)

# Threshold line
h_line = ax2.hlines(y=1, xmin=0, xmax=10, linestyle='--',
                    linewidth=2, color='black', label='Threshold')

ax2.set_ylabel('Ratio', rotation=0, labelpad=20)
ax2.set_xlabel('Scenes', labelpad=20)
ax2.set_title('Polarity ratio per scene')
ax2.set_xticks(ind)
ax2.set_xticklabels(np.arange(1, 11))
ax2.legend(labels=['Threshold', 'positive scenes'], loc='best', )
plt.show()

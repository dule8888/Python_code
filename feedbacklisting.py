# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 12:18:37 2018

@author: ldu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import matplotlib.image as image
import matplotlib.colors
from collections import defaultdict
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
from IPython.display import Image as im
import squarify as sq


data = pd.read_csv(r'Y:\le\FEEDBACK\feed1.csv', encoding = "ISO-8859-1")
data.rename(columns={'listing Id':'listing_Id'}, inplace=True)
data[['listing_Id']] = data[['listing_Id']].astype(str)

cat_number = data.Cat.value_counts()

# Limit top listings to those with more than 2 times
temp_dict = cat_number.to_dict()
temp_dict['Other'] = listing_Id[listing_Id<2].sum()
less_listing = pd.Series(temp_dict)
less_listing.sort_values(ascending=False, inplace=True)

# Turn Series into DataFrame for display purposes
df = less_listing.to_frame()
df.columns=['Number of bad feedbacks']
df.index.name = 'listing_Id'


# New colors for tree map since base ones are bland
cmap = plt.cm.gist_rainbow_r
norm = matplotlib.colors.Normalize(vmin=0, vmax=15)
colors = [cmap(norm(value)) for value in range(15)]
np.random.shuffle(colors)

# Use squarify to plot the tree map with the custom colors
fig,ax = plt.subplots(1,1,figsize=(11,11))
sq.plot(sizes=less_listing.values, label=less_listing.index.values, alpha=0.5, ax=ax, color=colors)
plt.axis('off')
plt.title('Countries by Number of Wine Reviews')
plt.show()

# for
descriptions = defaultdict(list)
data.apply(lambda x: descriptions[x.Cat].append(x.Feedback), axis=1)
descriptions['Bumpers'][0:5]
desc_string=''
# tokenization
unwanted_characters = re.compile('[^A-Za-z ]+')
try:   
    for cat in temp_dict:
        number = temp_dict[cat]
        desc_string = ' '.join(descriptions[cat])
        descriptions[cat] = ' '.join([w.lower() for w in re.sub(unwanted_characters, ' ', desc_string).split() if len(w) > 3])
        wc=WordCloud(width=1000, height=800,background_color="white",colormap='jet')
        wc.generate(descriptions[cat])
        wc.to_file(r'Y:\le\FEEDBACK\image1\%s_%d.jpg' %(cat,number))
except:
    pass

# add stopwords
nf_stopwords = ['order','refund','ship','part','ebay','item','seller','week','ordered','weeks','will','still','canceled','days','never']
for w in nf_stopwords:
    STOPWORDS.add(w)



wordlist  = wc.words_

sorted_by_value = sorted(wordlist.items(), key=lambda kv: kv[1])
sorted_by_value.reverse()
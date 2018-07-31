# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 10:57:24 2018

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


data = pd.read_csv('../input/wine-reviews/winemag-data-130k-v2.csv', index_col=0)
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Base from : https://www.analyticsvidhya.com/blog/2021/05/how-to-build-word-cloud-in-python/

#Remember to extract the data file so it is accessible
df = pd.read_csv("technical_debt_dataset.csv")




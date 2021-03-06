import pandas as pd
import numpy as np
from reuters import *
from sklearn.preprocessing import MultiLabelBinarizer
from pandas import DataFrame
import unicodedata

# Get data from reuters folder.
data_streamer = ReutersStreamReader('./reuters').iterdocs(3)
data = get_minibatch(data_streamer, 50000)

data_all = DataFrame({'text':[], 'tags':[]})
rows_all = []

for i in range(0, len(data.tags)):
	temp = data["text"][i]
	temp = unicodedata.normalize('NFKD', temp) #.encode('ascii','ignore')
	# Replace characters.
	for character in ["\n", "|", ">", "<", "-", "+", "^", "[", "]", "#", "\t", "\r", "`"]:
		temp = temp.replace(character, " ")
	if not temp.isspace():
		rows_all.append({'text':temp, 'tags':data["tags"][i]})

data_all = data_all.append(DataFrame(rows_all))
data_all.to_pickle('./interim_data/all.pkl')

print('finished saving data to all.pkl... see data below to check.')
print(data_all.head(2))
print(len(data_all))

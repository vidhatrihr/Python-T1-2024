import pandas as pd
scores = pd.read_csv('scores.csv')
print(scores['Total'].max())
print(scores['Total'].min())
print(scores['Total'].sum())
print(scores['Total'].sum())
print(scores['Total'].sort_values(ascending = False))


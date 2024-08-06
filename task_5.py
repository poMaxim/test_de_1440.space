import pandas as pd

# Предположим в df уже находится исходный датасет

df['time_in_seconds'] = df['time'].apply(lambda x: sum(int(t) * 60 ** i for i, t in enumerate(reversed(x.split(':')))))

df['total_traffic'] = df.groupby(['month', 'category'])['traffic_gb'].transform('sum')
df['total_time'] = df.groupby(['month', 'category'])['time_in_seconds'].transform('sum')

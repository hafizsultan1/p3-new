import pandas as pd

link ='https://www.football-data.co.uk/mmz4281/2223/E0.csv'

df_premier21 = pd.read_csv(link)

r = df_premier21.rename (columns={'FTHG':'home_goals','FTAG':'away_goals'})

print(r)


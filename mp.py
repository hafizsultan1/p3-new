import pandas as pd
link = 'https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)'
simpsons = pd.read_html(link)

print(len(simpsons))

print (simpsons[1])
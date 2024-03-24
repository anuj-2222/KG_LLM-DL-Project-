import webbrowser
import time
import pandas as pd
# Open the URL in the default web browser

df=pd.read_csv("LINK.csv")
lnk=df['LINK']
lk=lnk.values
link=lk.tolist()
for i in link:
    url = i
    webbrowser.open(url)
    time.sleep(1)

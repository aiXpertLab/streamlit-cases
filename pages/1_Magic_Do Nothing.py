x = """
## Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data, charts) without having to type an explicit command at all.

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using st.write
"""
'x', x 


import pandas as pd
df = pd.DataFrame({'Names': ['Aneesha','anee','aneeshabsoman']})
df


import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig 
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
data = {
    'age': [24, 29, 35, 36, 70, 18, 65, 45, 50],
    'salary': [35, 42, 80, 72, 42, 25, 50, 110, 112],
    'qual': [3, 3, 5, 3, 2, 2, 3, 4, 4],
    'class': ['A', 'A', 'B', 'A', 'C', 'C', 'A', 'B', 'B']  # Adding a class column for the plot
}
df = pd.DataFrame(data)
print(df)
plt.figure()
parallel_coordinates(df, 'class', cols=['age', 'salary', 'qual'], color=('#556270', '#4ECDC4', '#C7F464'))
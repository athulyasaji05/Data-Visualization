import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "2020": np.random.randint(100, 200, size=12),
    "2021": np.random.randint(100, 200, size=12),
    "2022": np.random.randint(100, 200, size=12)
}
df = pd.DataFrame(data)
df.set_index("month", inplace=True)
plt.figure(figsize=(10, 8))
sns.heatmap(df, annot=True, cmap="YlGnBu", cbar=True)

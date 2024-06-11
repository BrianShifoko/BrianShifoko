# generate_radar_chart.py

import matplotlib.pyplot as plt
import numpy as np

# Sample data for the radar chart (replace with your actual data)
labels = ['Python', 'JavaScript', 'HTML', 'CSS', 'Java']
stats = [90, 85, 95, 75, 80]

# Number of variables (labels)
num_vars = len(labels)

# Compute angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Make the plot close to a circle
stats += stats[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='red', alpha=0.25)
ax.plot(angles, stats, color='red', linewidth=2)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Save radar chart as radar_chart.png
plt.savefig('radar_chart.png', bbox_inches='tight')
plt.close()

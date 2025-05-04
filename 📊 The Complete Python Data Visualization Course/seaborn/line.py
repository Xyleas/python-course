import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load data
with open('prog-langs-popularity.pickle', 'rb') as f:
    data = pickle.load(f)

# Splt into two lists
languages, rankings = zip(*data)

# Get the Java years and ranks (split Java data into two lists)
java_years, java_ranks = zip(*rankings[0])

# matplotlib: plt.plot(java_years, java_ranks)
sns.lineplot(java_years, java_ranks)
plt.xticks(java_years)
plt.xlabel('year')
plt.ylabel('ranking')
plt.title('Java Ranking')
plt.show()
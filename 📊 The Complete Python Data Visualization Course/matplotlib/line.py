import matplotlib.pyplot as plt
import pickle

# Load data
with open('prog-langs-popularity.pickle', 'rb') as f:
    data = pickle.load(f)

#Test print(data)

# Splt into two lists
languages, rankings = zip(*data)
#Test print(langauges)
#Test print(rankings)

# Get the Java years and ranks (split Java data into two lists)
java_years, java_ranks = zip(*rankings[0])
#Test print(java_years)
#Test print(java_ranks)

plt.plot(java_years, java_ranks)
plt.xticks(java_years)
# x-axis: year, y-axis: ranking, title: Java Ranking
plt.xlabel('year')
plt.ylabel('ranking')
plt.title('Java Ranking')
plt.show()
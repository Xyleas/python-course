import matplotlib.pyplot as plt
import pickle

# Load data
with open('prog-langs-popularity.pickle', 'rb') as f:
    data = pickle.load(f)

# Split into two lists
languages, rankings = zip(*data)

# Iterate over all of the languages and call "plot" on their data
for i in range(len(languages)):
    # For each language, split their data into years and ranking lists
    years, ranks = zip(*rankings[i])
    plt.plot(years, ranks)

# x-axis=year, y-axis=ranking, title=Rankings of Programming Languages
plt.xlabel('year')
plt.ylabel('ranking')
plt.title('Rankings of Programming Languages')
plt.legend(langauges)
plt.show()
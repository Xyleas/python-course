import matplotlib.pyplot as plt
import pickle

# Load data
with open('devs-outside-time.pickle', 'rb') as f:
    data = pickle.load(f)

#Test print(data)

# Split into to lists
time, responses = zip(*data)
#Test print(time)
#Test print(responses)

plt.pie(responses, labels=time, autopct='%d%%')
# Force the x/y axes to have the same scale
# Circle instead of an ellipse
plt.axis('equal')
plt.title('Daily TIme Developers Spend Outside')
plt.show()

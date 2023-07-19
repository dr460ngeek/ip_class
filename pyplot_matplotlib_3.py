from matplotlib import pyplot as plt
players = ['Dhoni', 'Virat', 'Shikhar', 'Rishabh']
runs = [76,102,48,27]
plt.bar(players,runs)
plt.title('Players Runs')
plt.xlabel('Players')
plt.ylabel('Runs')
plt.show()

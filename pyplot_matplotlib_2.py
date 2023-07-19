from matplotlib import pyplot as plt

year = ['2020 - 21','2019 - 21','2021 - 22','2022 - 23']
ns = [83.4,89.7,88.7,91.2]
nk = [87.3,88.3,82.5,90.2]
nfb = [90.2,89.0,83.7,93.5]

plt.plot(year, ns, marker = 'o', label = 'Narayana - Siliguri')
plt.plot(year, nk, marker = '*', label = 'Narayana - Kalimpong')
plt.plot(year, nfb, marker = '^', label = 'Narayana - Fulbari')

plt.title("Result Analysis of Class - XII")
plt.xlabel("Year")
plt.ylabel("Percentage")
plt.legend()

# plt.savefig('Result.png')
plt.show()

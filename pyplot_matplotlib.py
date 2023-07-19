from matplotlib import pyplot as plt
dist = [0,1,2,3,4,5]
time = [0,2,4,6,8,10]
plt.plot(dist,time, linestyle = '-.', marker = 'x')
plt.xlabel('Distance in kilometer')
plt.ylabel('Time in minute')
plt.title('Graph of Distance Vs Time')
# plt.savefig('Line1.png') #png, jpeg, pdf, svg
plt.show()
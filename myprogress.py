from matplotlib import pyplot as plt

year = ['PT-1', 'PT-2', 'Term-1', 'PT-3', 'PT-4', 'Term-2']

# class10 = [16, 17, 56, 18, 19, 60]
# class11 = [18, 13, 52, 11, 17, 52]
# class12 = [14, 11, 55, 14, 13, 56]

pt1 = int(input(" Enter your marks of PT-1: "))
pt2 = int(input(" Enter your marks of PT-2: "))
pt3 = int(input(" Enter your marks of PT-3: "))
pt4 = (pt1+pt2+pt3)/3
class12 = [pt1, pt2, 56, pt3, pt4, 60]
# #plt.plot(year, class10, marker = 'o', label = 'Class 10 2020-21')
# #plt.plot(year, class11, marker = '*', label = 'Class 11 2021-22')
plt.plot(year, class12, marker = '^', label = 'Class 12 2022-23')

plt.title("Reslut Analysis of Pratham Agarwal")
plt.xlabel("Marks")
plt.ylabel("Total exams in the session.")
plt.legend()

plt.show()
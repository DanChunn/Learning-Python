from matplotlib import pyplot as plt

title = "pop vs year"
xlab = "year"
ylab = "population"

year = [1980,1990,2000,2010,2020]
pop = [500,1000,2000,2500,2900]

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

tick_val = [1000,2000,3000,4000]
tick_lab = ['1B','2B','3B','4B']

plt.yticks(tick_val,tick_lab)
plt.plot(year,pop)
plt.show()

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.scatter(year,pop)
plt.show()

plt.hist(pop, bins = 5)
plt.show()
plt.clf()
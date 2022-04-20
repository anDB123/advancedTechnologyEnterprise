import numpy as np
from matplotlib import pyplot as plt

interest_over_time = np.genfromtxt("C:/Users/AndyPC/Desktop/ratioData/multiTimeline.csv", delimiter=',')
fig, ax = plt.subplots()

ax.plot(interest_over_time[:-5])
ax.set_xlabel("Year")
ax.set_ylabel("Interest (out of 100)")
plt.xticks(np.linspace(0, 245, 6), labels=['2017', '2018', '2019', '2020', '2021', '2022'])
fig1 = plt.gcf()
plt.show()
plt.draw()
save_location = "C:/Users/AndyPC/Desktop/ratioData/"
fig1.savefig("{}tesla_interest_over_time.pdf".format(save_location), dpi=100)
fig1.savefig("{}tesla_interest_over_time.png".format(save_location), dpi=100)

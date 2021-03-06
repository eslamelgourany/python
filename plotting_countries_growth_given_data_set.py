import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

data = pd.read_csv('countries.csv')
usa = data[data.country == "United States"]
# print(usa)

china = data[data.country == "China"]
# print(china)

egypt = data[data.country == "Egypt"]
# print(egypt)

czech_republic = data[data.country == "Czech Republic"]
# print(czech_republic)


fig = plt.figure(dpi=100, figsize=(18, 8))

ax1 = plt.subplot(2, 2, 1)
ax2 = plt.subplot(2, 2, 2)
ax3 = plt.subplot(2, 2, 3)
ax4 = plt.subplot(2, 2, 4)



ax1.plot(czech_republic.year , czech_republic.population / 10 **6 , 'r')
ax2.plot(czech_republic.year , egypt.population / 10 **6 , 'y')
ax3.plot(czech_republic.year, usa.population / 10 **6 , 'c')
ax4.plot(czech_republic.year, china.population / 10**6 , 'g')


ax1.legend(["Czech Repubic"])
ax2.legend(["Egypt"])
ax3.legend(["USA"])
ax4.legend(["China"])

for ax in (ax1,ax2,ax3,ax4):
    ax.set_xlabel("Years from (1950 to 2007)")


ax1.set_ylabel("Czech republic population in Million")
ax2.set_ylabel("Egypt population in Million")
ax3.set_ylabel("USA population in Million")
ax4.set_ylabel("China population in Million")


fig.suptitle("Comaprisons in Populations", fontsize=18)
fig.subplots_adjust(hspace=0.4)
plt.show()



#
# plt.plot(usa.year , usa.population /10 ** 6)
# plt.plot(china.year , china.population/10 **6)
# plt.plot(egypt.year, egypt.population /10**6)
# plt.plot(czech_republic.year , czech_republic.population / 10 ** 6)
# plt.legend(["USA", "CHINA ", "EGYPT", "CZ"])
# plt.show()




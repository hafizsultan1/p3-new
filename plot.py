import matplotlib.pyplot as plt

gdp_cap = [26, 39, 90, 120, 200]
life_exp = [40, 34, 55, 20, 90]

plt.scatter(gdp_cap,life_exp)
plt.xscale('log')
plt.show()
import matplotlib.pyplot as plt

models = ["Model S", "Model S Plaid", "Model 3 Rear Wheel Drive", "Model 3 Long Range", "Model 3 Performance",
          "Model X",
          "Model X Plaid",
          "Model Y Long Range", "Model Y Performance"]
prices = [99900, 135990, 46990, 55990, 62990, 114990, 138990, 62990, 67990]
prices, models = zip(*sorted(zip(prices, models)))
fig, ax = plt.subplots()
ax.bar(models, prices)
ax.set_xlabel("Model Name")
ax.set_ylabel("Model Price (USD)")
plt.xticks(rotation=30, ha='right', rotation_mode='anchor')
# plt.show()
save_location = "C:/Users/AndyPC/Desktop/"
plt.tight_layout()
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig("{}priceComparison.pdf".format(save_location), dpi=100)
fig1.savefig("{}priceComparison.png".format(save_location), dpi=100)

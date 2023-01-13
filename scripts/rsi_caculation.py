
g = [
    566.710022,
    564.229980,
    549.919983,
    549.799988,
    536.179993,
    518.799988,
    522.030029,
    525.799988,
    516.880005,
    502.989990,
    488.070007,
    490.160004,
    482.820007,
    481.609985,
    488.899994,
    477.320007,
    483.470001,
    482.519989,
    492.429993,
    505.130005,
]
perChanges = []
for index in range(len(g)):
    if index > 0 and index <= 22:
        perChanges.append((g[index]-g[index-1]) / g[index-1])
posChanges = []
negChanges = []
for percent in perChanges:
    if percent < 0.0:
        negChanges.append(percent)
    else:
        posChanges.append(percent)
print(len(posChanges) + len(negChanges))

from matplotlib.figure import Figure

# Create a Figure and add a plot
fig1 = Figure(figsize=(6, 4), dpi=90) # <= main fig object
ax = fig1.add_subplot(111)
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
ax.plot(x, y, marker='o', color='b')
ax.set_title("Line Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")


import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(1)
plt.ion() # in order to enable interactive plotting
ax = fig.add_subplot(111)
hl, = plt.plot([], [], color='#EE6666', linewidth = 4) # after subplot to add it to subplots

x_coord =[]
y_coord =[]
x_coord = np.asarray(x_coord)
y_coord = np.asarray(y_coord)

def update_line(hl, new_data):
    hl.set_xdata(new_data[0])
    hl.set_ydata(new_data[1])
    plt.draw()
    plt.axis([0,new_data[0][-1]+2,0,1])

ax.set(facecolor='#E6E6E6')
plt.title( ' for patient ' , fontsize=12, fontstyle='italic', fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('k', fontsize=12)
ax.grid(color='w', linestyle='solid')
# lighten ticks and labels
ax.tick_params(colors='gray', direction='in')
for tick in ax.get_xticklabels():
    tick.set_color('0.3')
for tick in ax.get_yticklabels():
    tick.set_color('0.3')

plt.xticks(fontsize = 8)


for i in range(100):
    y = np.random.random()
    x_coord = np.append(x_coord, i)
    y_coord = np.append(y_coord, y)
    update_line(hl, [x_coord, y_coord])
    plt.pause(0.05)


# while True:
#     plt.pause(0.05)


# plt.axis([0, 10, 0, 1])
# plt.ion() # in order to enable interactive plotting
#
#
# for i in range(100):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.05)
#
# # while True:
# #     plt.pause(0.05)


    # # plt.ion() # in order to enable interactive plotting
    # plt.axis([0, 10, 0, 1])
    #
    # hl, = plt.plot([], [])
# def update_line(hl, new_data):
#     hl.set_xdata(np.append(hl.get_xdata(), new_data[0]))
#     hl.set_ydata(np.append(hl.get_ydata(), new_data[1]))
#     plt.draw()
#
# for i in range(100):
#     y = np.random.random()
#     update_line(hl, [i/10, y])
#     print(y)
#     plt.pause(0.05)
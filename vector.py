'''
Vector class/structure used to plot vectors
'''

class Vector:
    def __init__(self, xstart, ystart, dx, dy, color, name):
        '''
        xstart, ystart store the starting point of a vector.
        dx, dy are length of a vector in x and y directions.
        color is the color of a vector.
        name is the name of the vector and the name will be presented 
            on the legend of the graph.
        '''
        self.xstart = xstart
        self.dx = dx
        self.ystart = ystart
        self.dy = dy
        self.color = color
        self.name = r"$\vec{%s}$" % name

    def get_xstart(self):
        return self.xstart
    def get_ystart(self):
        return self.ystart
    def get_dx(self):
        return self.dx
    def get_dy(self):
        return self.dy
    def get_color(self):
        return self.color
    def get_name(self):
        return self.name

# plt.figure()
# x = np.array([[0, 1]])
# y = np.array([[0, 0]])
# u = np.array([[1, 0]])
# v = np.array([[0, 1]])

# x and y are all the x and y coordinates of all vectors
# u and v are the dx and dy (length in x and y direction) of all vectors
# set the u, v to have the same unit as x and y by
# angles='xy', scale_units='xy', scale=1.
# plt.quiver(x, y, u, v, angles='xy', scale=1, scale_units='xy')
# xmax = max(np.max(x), np.max(x + u)) + 1
# xmin = min(np.min(x), np.min(x + u)) - 1
# ymax = max(np.max(y), np.max(y + v)) + 1
# ymin = min(np.min(y), np.max(y + v)) - 1
# print(xmin, xmax)
# print(ymin, ymax)
# plt.xlim(xmin, xmax)
# plt.ylim(ymin, ymax)
# plt.show()

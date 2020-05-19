from matplotlib import animation
import matplotlib.pyplot as plt


class OutputData(object):
    def __init__(self):
        self.fig = plt.figure()
        self.images = []

    def draw_figure(self, data):
        """ draw flow shape on figure and store """
        keys = [i for i in range(len(data))]
        image = plt.plot(keys, data, 'blue')
        plt.title('1d flow calculation')
        self.images.append(image)

    def show_animation(self):
        """ display animation """
        _ = animation.ArtistAnimation(self.fig, self.images, interval=30)
        plt.show()

    def save_animation(self):
        """ save animation to file """
        ani = animation.ArtistAnimation(self.fig, self.images, interval=1)
        ani.save('1d_flow.gif', writer='imagemagick')

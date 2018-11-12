'''
Plot graphs 
- bar chart

Panitan W
'''

# fix the "cannot display error" error of the matplotlib in ubuntu
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import collections as col

import np

def plot_bar(xdata, ydata, title):
    ''' 
    Plot a bar chart.
    '''
    graph_title = title + " bar char"
    fig_title = title + "_" + "bar.jpg"

    plt.figure(111, figsize=(8, 6), dpi=80)

    plt.bar(xlocation, ydata, width=0.5)

    ymin = min(ydata)
    ymax = max(ydata)
    plt.ylim(ymin, ymax)
    # plt.yscale('log')

    xmin = min(xdata)
    xmax = max(xdata)
    plt.xlim(xmin, xmax)
    xlocation = np.arange(len(xdata))
    # plt.xticks(xlocation, xdata)


    plt.title(graph_title)
    plt.xlabel("Frequency")
    plt.ylabel("% Reference")

    plt.grid(b=True, which='major', color='b', linestyle='-')
    plt.grid(b=True, which='minor', color='g', linestyle='--')

    plt.tight_layout()

    # plt.show()
    plt.savefig(fig_title)

def plot_hist(data, title):
    '''
    Plot a histogram graph 
    - set the bin to 1 for each unique data
    - set the weights for each elements in the list equally
    '''
    graph_title = title + " bar char"
    fig_title = title + "_" + "bar.jpg"

    plt.figure(111, figsize=(8, 6), dpi=80)
    data_array = np.array(data)
    dweigths = np.ones_like(data_array)/float(len(data))

    count_data = col.Counter(data)
    plt.hist(data_array, weights=dweigths, bins=len(count_data.keys()))

    plt.title(grpah_title)
    plt.xlabel("Frequency")

    plt.ylabel("% Reference")
    # plt.yscale('log')

    plt.grid(b=True, which='major', color='b', linestyle='-')
    plt.grid(b=True, which='minor', color='g', linestyle='--')

    plt.tight_layout()

    # plt.show()
    plt.savefig(fig_title)

def plot_cdf(data, title):
    '''
    Plot a CDF graph based on the histogram.
    '''
    graph_title = title + " cdf char"
    fig_title = title + "_" + "cdf.jpg"

    plt.figure(111, figsize=(8, 6), dpi=80)

    data_np = np.array(data)
    dweigths = np.ones_like(data_np)/float(len(data))
    
    plt.hist(data, weights=dweigths, bins=len(set(data)), cumulative=True)
    
    dmax = max(data)
    dmin = min(data)

    plt.title(graph_title)
    plt.xlabel("Frequency")
    
    # plt.yscale('log')
    plt.ylabel("% log(Reference)")
    
    plt.grid(b=True, which='major', color='b', linestyle='-')
    plt.grid(b=True, which='minor', color='g', linestyle='--')
    
    plt.tight_layout()
    plt.show()
    # plt.savefig(fig_title)

def plot_vector(vector_lst):
    ''' 
    Plot vectors on the 2D coordinates.
    
    Ex.
    plot_vector([Vector(0, 0, 3, 0, 'r', "r"),
                 Vector(3, 0, 0, 4, 'g', "g"),
                 Vector(0, 0, 3, 4, 'b', "b")])
    '''

    plt.figure(111, figsize=(8, 6), dpi=80)

    xpoints = []
    ypoints = []
    for v in vector_lst:
        xpoints.append(v.get_xstart())
        xpoints.append(v.get_dx() + v.get_xstart())

    xmin = min(xpoints)
    xmax = max(xpoints)

    for v in vector_lst:
        ypoints.append(v.get_ystart())
        ypoints.append(v.get_dy() + v.get_ystart())

    ymin = min(ypoints)
    ymax = max(ypoints)

    plt.xlim(xmin -1, xmax + 1)
    plt.ylim(ymin -1, ymax + 1)

    legends = []
    labels = []
    for v in vector_lst:
        artist = plt.arrow(v.get_xstart(), v.get_ystart(), v.get_dx(), v.get_dy(),
                           color=v.get_color(), width=0.01,
                           length_includes_head=True,
                           head_width=0.1, head_length=0.1)
        legends.append(artist)
        labels.append(v.get_name())

    plt.legend(legends, labels, loc='best', mode='expand', ncol=len(vector_lst))

    plt.box(False)

    frame = plt.gca()
    # frame.axes.get_xaxis().set_visible(False)
    # frame.axes.get_yaxis().set_visible(False)

    # frame.axes.get_xaxis().set_ticks([])
    # frame.axes.get_yaxis().set_ticks([])
    plt.grid(True)
    plt.show()

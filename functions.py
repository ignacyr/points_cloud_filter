import matplotlib.pyplot as plt


def filter_cloud(p_x, p_y, p_z, cuts):
    # axis limits
    min_of_x, max_of_x = min(p_x), max(p_x)
    min_of_y, max_of_y = min(p_y), max(p_y)
    min_of_z, max_of_z = min(p_z), max(p_z)

    print(cuts['x_down'])
    x_down_cut = int(cuts['x_down'].get())
    x_up_cut = int(cuts['x_up'].get())
    y_down_cut = int(cuts['y_down'].get())
    y_up_cut = int(cuts['y_up'].get())
    z_down_cut = int(cuts['z_down'].get())
    z_up_cut = int(cuts['z_up'].get())

    p_x[p_x > max_of_x - x_up_cut / 100 * (max_of_x - min_of_x)] = None
    p_x[p_x < min_of_x + x_down_cut / 100 * (max_of_x - min_of_x)] = None

    p_y[p_y > max_of_y - y_up_cut / 100 * (max_of_y - min_of_y)] = None
    p_y[p_y < min_of_y + y_down_cut / 100 * (max_of_y - min_of_y)] = None

    p_z[p_z > max_of_z - z_up_cut / 100 * (max_of_z - min_of_z)] = None
    p_z[p_z < min_of_z + z_down_cut / 100 * (max_of_z - min_of_z)] = None
    return p_x, p_y, p_z


# update plot
def update(root, ax, canvas, p_x, p_y, p_z, cuts):
    ax.clear()
    # plotting filtered points
    min_of_x, max_of_x = min(p_x), max(p_x)
    min_of_y, max_of_y = min(p_y), max(p_y)
    min_of_z, max_of_z = min(p_z), max(p_z)
    ax.set_xlim3d(min_of_x, max_of_x)
    ax.set_ylim3d(min_of_y, max_of_y)
    ax.set_zlim3d(min_of_z, max_of_z)
    p_x_upd, p_y_upd, p_z_upd = filter_cloud(p_x, p_y, p_z, cuts)
    ax.scatter(p_x_upd, p_y_upd, p_z_upd, c='r', marker='o', s=1)
    canvas.draw()
    root.update()


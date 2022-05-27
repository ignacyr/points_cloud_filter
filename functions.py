import matplotlib.pyplot as plt


def filter_cloud(p_x, p_y, p_z, x_down, x_up, y_down, y_up, z_down, z_up,
                 min_of_x, max_of_x, min_of_y, max_of_y, min_of_z, max_of_z):

    x_down_cut = x_down
    x_up_cut = x_up
    y_down_cut = y_down
    y_up_cut = y_up
    z_down_cut = z_down
    z_up_cut = z_up

    p_x[p_x > max_of_x - x_up_cut / 100 * (max_of_x - min_of_x)] = None
    p_x[p_x < min_of_x + x_down_cut / 100 * (max_of_x - min_of_x)] = None

    p_y[p_y > max_of_y - y_up_cut / 100 * (max_of_y - min_of_y)] = None
    p_y[p_y < min_of_y + y_down_cut / 100 * (max_of_y - min_of_y)] = None

    p_z[p_z > max_of_z - z_up_cut / 100 * (max_of_z - min_of_z)] = None
    p_z[p_z < min_of_z + z_down_cut / 100 * (max_of_z - min_of_z)] = None
    return p_x, p_y, p_z


# update plot
def update(root, ax, canvas, p_x, p_y, p_z, x_down, x_up, y_down, y_up, z_down, z_up,
           min_of_x, max_of_x, min_of_y, max_of_y, min_of_z, max_of_z):
    ax.clear()
    # plotting filtered points
    ax.set_xlim3d(min_of_x, max_of_x)
    ax.set_ylim3d(min_of_y, max_of_y)
    ax.set_zlim3d(min_of_z, max_of_z)
    p_x_upd, p_y_upd, p_z_upd = filter_cloud(p_x, p_y, p_z, x_down, x_up, y_down, y_up, z_down, z_up,
                                             min_of_x, max_of_x, min_of_y, max_of_y, min_of_z, max_of_z)
    ax.scatter(p_x_upd, p_y_upd, p_z_upd, c='r', marker='o', s=1)
    canvas.draw()
    root.update()


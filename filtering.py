import os


def filter_cloud(p_x, p_y, p_z, x_down, x_up, y_down, y_up, z_down, z_up,
                 min_of_x, max_of_x, min_of_y, max_of_y, min_of_z, max_of_z, scale):

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

    # print(sum(p_z) / len(p_z))  # average value of height (z)

    for i, _ in enumerate(p_x):
        if i % scale != 0:
            p_x[i], p_y[i], p_z[i] = None, None, None

    return p_x, p_y, p_z


# update plot
def update_plot(root, ax, canvas, p_x, p_y, p_z, x_down, x_up, y_down, y_up, z_down, z_up,
                min_of_x, max_of_x, min_of_y, max_of_y, min_of_z, max_of_z, scale):
    ax.clear()
    # plotting filtered points
    ax.set_xlim3d(min_of_x, max_of_x)
    ax.set_ylim3d(min_of_y, max_of_y)
    ax.set_zlim3d(min_of_z, max_of_z)
    p_x_upd, p_y_upd, p_z_upd = filter_cloud(p_x, p_y, p_z, x_down, x_up, y_down, y_up, z_down, z_up,
                                             min_of_x, max_of_x, min_of_y, max_of_y, min_of_z, max_of_z, scale)
    ax.scatter(p_x_upd, p_y_upd, p_z_upd, c='r', marker='o', s=1)
    canvas.draw()
    root.update()


def save_as_csv(p_x, p_y, p_z, x_down, x_up, y_down, y_up, z_down, z_up,
                min_of_x, max_of_x, min_of_y, max_of_y, min_of_z, max_of_z, scale):
    p_x, p_y, p_z = filter_cloud(p_x, p_y, p_z, x_down, x_up, y_down, y_up, z_down, z_up,
                                 min_of_x, max_of_x, min_of_y, max_of_y, min_of_z, max_of_z, scale)

    num = 1
    new_csv_filename = f"csv_cloud{num}.csv"
    while new_csv_filename in os.listdir("data_csv"):
        num += 1
        new_csv_filename = f"csv_cloud{num}.csv"

    with open(f"data_csv/{new_csv_filename}", 'w') as file:
        file.write("x, y, z\n")
        for i, _ in enumerate(p_x):
            if p_x[i] > 0 and p_y[i] > 0 and p_z[i] > 0:
                file.write(f"{p_x[i]}, {p_y[i]}, {p_z[i]}\n")



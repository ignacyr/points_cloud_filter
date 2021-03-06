import sys

import tkinter as tk
import numpy as np
import laspy
from tkinter import Tk
from tkinter import ttk

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from filtering import *


def main():
    try:
        input_filename = f"input_data_las/{sys.argv[1]}"
    except IndexError:
        input_filename = "input_data_las/duza_chmura_zmniejszona.las"  # default

    # reading las file and copy points
    input_las = laspy.file.File(input_filename, mode="r")
    point_records = input_las.points.copy()

    # getting scaling and offset parameters
    las_scale_x = input_las.header.scale[0]
    las_offset_x = input_las.header.offset[0]
    las_scale_y = input_las.header.scale[1]
    las_offset_y = input_las.header.offset[1]
    las_scale_z = input_las.header.scale[2]
    las_offset_z = input_las.header.offset[2]

    # close file
    input_las.close()

    # calculating coordinates
    p_x = np.array((point_records['point']['X'] * las_scale_x) + las_offset_x)
    p_y = np.array((point_records['point']['Y'] * las_scale_y) + las_offset_y)
    p_z = np.array((point_records['point']['Z'] * las_scale_z) + las_offset_z)

    # axis limits
    min_of_x, max_of_x = min(p_x), max(p_x)
    min_of_y, max_of_y = min(p_y), max(p_y)
    min_of_z, max_of_z = min(p_z), max(p_z)

    # plotting points before filtering
    fig = plt.figure(figsize=(11, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(p_x, p_y, p_z, c='r', marker='o', s=1)
    ax.set_xlim3d(min_of_x, max_of_x)
    ax.set_ylim3d(min_of_y, max_of_y)
    ax.set_zlim3d(min_of_z, max_of_z)

    # initialize tkinter gui
    root = Tk()
    root.title('Points cloud filter')
    root.resizable(height=False, width=False)
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().grid(row=0)
    canvas.draw()

    # add widgets
    frame = ttk.Frame(root, padding=10)
    frame.grid(row=1)

    ttk.Label(frame, text='Cut from west [%]:').grid(row=2, column=0)
    x_down = tk.Entry(frame)
    x_down.insert(-1, '0')
    x_down.grid(row=3, column=0)

    ttk.Label(frame, text='Cut from east [%]:').grid(row=0, column=0)
    x_up = tk.Entry(frame)
    x_up.insert(-1, '0')
    x_up.grid(row=1, column=0)

    ttk.Label(frame, text='Cut from south [%]:').grid(row=2, column=1)
    y_down = tk.Entry(frame)
    y_down.insert(-1, '0')
    y_down.grid(row=3, column=1)

    ttk.Label(frame, text='Cut from north [%]:').grid(row=0, column=1)
    y_up = tk.Entry(frame)
    y_up.insert(-1, '0')
    y_up.grid(row=1, column=1)

    ttk.Label(frame, text='Cut from down [%]:').grid(row=2, column=2)
    z_down = tk.Entry(frame)
    z_down.insert(-1, '0')
    z_down.grid(row=3, column=2)

    ttk.Label(frame, text='Cut from up [%]:').grid(row=0, column=2)
    z_up = tk.Entry(frame)
    z_up.insert(-1, '0')
    z_up.grid(row=1, column=2)

    ttk.Label(frame, text='Scale:').grid(row=0, column=3)
    scale = tk.Entry(frame)
    scale.insert(-1, '1')
    scale.grid(row=1, column=3)

    ttk.Button(frame, text="Filter", command=lambda: update_plot(root, ax, canvas, p_x.copy(), p_y.copy(), p_z.copy(),
                                                                 int(x_down.get()), int(x_up.get()),
                                                                 int(y_down.get()), int(y_up.get()),
                                                                 int(z_down.get()), int(z_up.get()),
                                                                 min_of_x, max_of_x, min_of_y,
                                                                 max_of_y, min_of_z, max_of_z,
                                                                 int(scale.get())),
               padding=10).grid(row=4, column=1)

    ttk.Button(frame, text="Save as csv", command=lambda: save_as_csv(p_x.copy(), p_y.copy(), p_z.copy(),
                                                                      int(x_down.get()), int(x_up.get()),
                                                                      int(y_down.get()), int(y_up.get()),
                                                                      int(z_down.get()), int(z_up.get()),
                                                                      min_of_x, max_of_x, min_of_y,
                                                                      max_of_y, min_of_z, max_of_z,
                                                                      int(scale.get())),
               padding=10).grid(row=4, column=2)

    root.protocol("WM_DELETE_WINDOW", lambda: root.quit())  # handling 'X' button on the main window
    root.mainloop()


if __name__ == '__main__':
    main()


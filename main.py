import numpy as np
import laspy
import matplotlib.pyplot as plt

# reading las file and copy points
input_las = laspy.file.File("chmura.las", mode="r")
point_records = input_las.points.copy()

# getting scaling and offset parameters
las_scaleX = input_las.header.scale[0]
las_offsetX = input_las.header.offset[0]
las_scaleY = input_las.header.scale[1]
las_offsetY = input_las.header.offset[1]
las_scaleZ = input_las.header.scale[2]
las_offsetZ = input_las.header.offset[2]

# calculating coordinates
p_X = np.array((point_records['point']['X'] * las_scaleX) + las_offsetX)
p_Y = np.array((point_records['point']['Y'] * las_scaleY) + las_offsetY)
p_Z = np.array((point_records['point']['Z'] * las_scaleZ) + las_offsetZ)

# axis limits
min_of_X, max_of_X = min(p_X), max(p_X)
min_of_Y, max_of_Y = min(p_Y), max(p_Y)
min_of_Z, max_of_Z = min(p_Z), max(p_Z)

# plotting points before filtering
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(p_X, p_Y, p_Z, c='r', marker='o', s=1)
ax.set_xlim3d(min_of_X, max_of_X)
ax.set_ylim3d(min_of_Y, max_of_Y)
ax.set_zlim3d(min_of_Z, max_of_Z)
plt.show()

# get square size [%]
x_down_cut = int(input('Ile % punktów wyciąć od wschodu?: '))
x_up_cut = int(input('Ile % punktów wyciąć od zachodu?: '))
y_down_cut = int(input('Ile % punktów wyciąć od północy?: '))
y_up_cut = int(input('Ile % punktów wyciąć od południa?: '))
z_down_cut = int(input('Ile % punktów wyciąć od dołu?: '))
z_up_cut = int(input('Ile % punktów wyciąć od góry?: '))

# filter points
p_X_upd = p_X.copy()
p_Y_upd = p_Y.copy()
p_Z_upd = p_Z.copy()

p_X_upd[p_X_upd > max_of_X - x_up_cut/100*(max_of_X - min_of_X)] = None
p_X_upd[p_X_upd < min_of_X + x_down_cut/100*(max_of_X - min_of_X)] = None

p_Y_upd[p_Y_upd > max_of_Y - y_up_cut/100*(max_of_Y - min_of_Y)] = None
p_Y_upd[p_Y_upd < min_of_Y + y_down_cut/100*(max_of_Y - min_of_Y)] = None

p_Z_upd[p_Z_upd > max_of_Z - z_up_cut/100*(max_of_Z - min_of_Z)] = None
p_Z_upd[p_Z_upd < min_of_Z + z_down_cut/100*(max_of_Z - min_of_Z)] = None

# plotting filtered points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(p_X_upd, p_Y_upd, p_Z_upd, c='r', marker='o', s=1)
ax.set_xlim3d(min_of_X, max_of_X)
ax.set_ylim3d(min_of_Y, max_of_Y)
ax.set_zlim3d(min_of_Z, max_of_Z)
plt.show()

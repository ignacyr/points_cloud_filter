import laspy
import sys

filename = sys.argv[1]
new_filename = sys.argv[2]
scale = int(sys.argv[3])

input_las = laspy.file.File(filename, mode="r")
point_records = input_las.points.copy()

output_las = laspy.file.File(new_filename, mode="w", header=input_las.header)
output_las.points = [point for i, point in enumerate(point_records) if i % scale == 0]

output_las.close()

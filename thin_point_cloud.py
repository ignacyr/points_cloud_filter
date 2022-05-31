import sys
import os

import laspy


def thin():
    filename = sys.argv[1]
    scale = int(sys.argv[2])

    num = 1
    new_filename = f"out_cloud{num}.las"
    while new_filename in os.listdir("output_data_las"):
        num += 1
        new_filename = f"out_cloud{num}.las"

    input_las = laspy.file.File(f"input_data_las/{filename}", mode="r")
    point_records = input_las.points.copy()

    output_las = laspy.file.File(f"output_data_las/{new_filename}", mode="w", header=input_las.header)

    output_las.points = [point for i, point in enumerate(point_records) if i % scale == 0]

    output_las.close()


if __name__ == "__main__":
    thin()


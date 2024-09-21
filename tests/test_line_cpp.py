import numpy as np
import pyransac3d as pyrsc

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


def generate_data() -> np.ndarray:
    np.random.seed(0)
    versor = np.array([0.0, 0.0, 1.0], dtype=float)
    versor = versor / np.linalg.norm(versor)
    point = np.array([0.0, 0.0, 0.0], dtype=float)
    number_of_points = 2000
    sx = 0.2
    sy = 0.2
    sz = 0.5
    vector = np.random.randn(number_of_points, 3)
    for column_index, sn in zip(range(3), (sx, sy, sz)):
        vector[:, column_index] *= sn
    aux = np.tile(versor, (number_of_points, 1))
    hyperparameter = np.arange(1, number_of_points + 1).reshape(number_of_points, 1)
    pointcloud = point + aux * hyperparameter + vector
    return pointcloud


def plot_pointcloud(
    pc: np.ndarray, ransac_versor: np.ndarray, ransac_point: np.ndarray
):
    fig = plt.figure(dpi=200)
    ax: Axes3D = fig.add_subplot(projection="3d")
    ax.scatter(
        xs=pc[:, 0], ys=pc[:, 1], zs=pc[:, 2], s=15, alpha=0.25, lw=0, marker="."
    )
    ax.view_init(vertical_axis="y")
    ax.set_xlim(left=-2.0, right=2.0)
    ax.set_ylim(bottom=-2.0, top=2.0)
    ax.set_zlim(bottom=0.0, top=2000.0)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    hyper_parameter = (2000.0 - ransac_point[2]) / ransac_versor[2]
    start_vector = ransac_versor * (-ransac_point[2] / ransac_versor[2]) + ransac_point
    end_vector = ransac_versor * hyper_parameter + ransac_point
    plot_vector = np.vstack((start_vector, end_vector))
    ax.plot3D(
        xs=plot_vector[:, 0],
        ys=plot_vector[:, 1],
        zs=plot_vector[:, 2],
        c="red",
        label="3D Line",
    )
    ax.legend()
    plt.show()
    print()


def main():
    pointcloud = generate_data()
    line = pyrsc.Line_cpp()
    versor, point, inliers = line.fit(pointcloud, thresh=0.3)
    plot_pointcloud(pc=pointcloud, ransac_versor=versor, ransac_point=point)


if __name__ == "__main__":
    main()

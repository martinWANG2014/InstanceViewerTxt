#!/bin/python
# author: Chenghao WANG
# Contact: chenghao.wang@hds.utc.fr
# institute: Heudiasyc
# 13/03/2019

import sys
import matplotlib.pyplot as plt


# read data from json file.
def draw_model_from_txt(node_file, user_file, output_file):
    with open(user_file, "r") as ins:
        users_x = []
        users_y = []
        for line in ins:
            xy = line.split()
            users_x.append(float(xy[0]))
            users_y.append(float(xy[1]))

    with open(node_file, "r") as ins:
        nodes_x = []
        nodes_y = []
        for line in ins:
            xy = line.split()
            nodes_x.append(int(xy[0]))
            nodes_y.append(int(xy[1]))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(nodes_x, nodes_y, 'rs', label="Candidate Node")
    plt.scatter(users_x, users_y, s=4, label="User")
    # plt.plot(users_x, users_y, 'bs', label="User")
    ax.set_xlabel('x-[m]')
    ax.set_ylabel('y-[m]')
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])

    # Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
              fancybox=True, shadow=True, ncol=5)
    ax.set_title('Candidate nodes and users positions')
    fig.savefig(output_file)


if __name__ == '__main__':
    draw_model_from_txt(sys.argv[1], sys.argv[2], sys.argv[3])

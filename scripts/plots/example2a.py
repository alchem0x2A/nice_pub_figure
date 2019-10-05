# Double plots with legend outside
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from helper import gridplots, grid_labels, img_path, script_path
import tikzplotlib


def main():
    fig, ax = gridplots(1, 2,
                        r=1,
                        ratio=2.5)

    labels = ["aaa", "bbb", "ccc",
              "ddd", "eee", "fff"]
    xx = np.linspace(0, 1)
    for i, ax_ in enumerate(ax):
        for j, l in enumerate(labels):
            ax_.plot(xx, np.ones_like(xx) * j, "--",
                     label="$Sample: {0}$".format(l))
        ax_.set_xlabel("$x$")
        ax_.set_ylabel("$y$")

    ax[1].legend(loc="center left",
                 bbox_to_anchor=(1.05, 0.5),fontsize="small")
    grid_labels(fig, ax,
                offsets=[(0, 0), (-0.1, 0)]
    )
    # fig.set_constrained_layout(False)
    # ax[-1].set_axis_off()
    # mpl.use("pgf")
    fig.savefig(img_path / "example2a.pdf")
    fig.savefig(img_path / "example2a.pgf")


if __name__ == '__main__':
    main()


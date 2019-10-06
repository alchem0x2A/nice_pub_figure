import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from helper import gridplots, grid_labels, img_path, script_path
import tikzplotlib


def plot_main():
    fig, ax = gridplots(3, 3,
                        r=1,
                        span=[(0, 0, 1, 1), (0, 1, 1, 1), (0, 2, 1, 1),
                              (1, 0, 2, 3)],
                        ratio=1.5)
    functions = [np.sin, np.cos,
                 np.tan]
    func_names = ["sin", "cos", "tan"]

    x = np.linspace(-2.0, 2.0, 255) * np.pi
    
    for i, ax_ in enumerate(ax[: -1]):
        y = functions[i](x)
        y[np.abs(y) > 10] = np.nan
        ax_.plot(x, y, "o",
                 markersize=2,
                 label="$y=\\{0}(x)$".format(func_names[i]))
        ax_.set_xlabel("$x$")
        ax_.set_ylabel("$y$")
        ax_.set_xticks(np.array([-2, -1, 0, 1, 2]) * np.pi)
        ax_.set_xticklabels(["-2π", "-π", "0",
                              "π", "2π"])
        ax_.set_ylim(-2, 2)
        ax_.legend(loc=1, frameon=True)

    xx = np.linspace(0, 10, 256) * np.pi
    y1 = np.sin(xx)
    y2 = np.cos(xx)
    ax[-1].plot(xx, y1, "-", label="$\\sin(x)$")
    ax[-1].plot(xx, y2, "-", label="$\\cos(x)$")
    ax[-1].set_xticks(np.arange(0, 11) * np.pi)
    ax[-1].set_xticklabels(["0"] \
                           + ["${0}\\pi$".format(i) for i in range(1, 11)])
    ax[-1].set_xlabel("$x$")
    ax[-1].set_ylabel("$y$")
    ax[-1].set_yticks([-1, -0.5, 0, 0.5, 1])
    grid_labels(fig, ax,
                offsets=[(0, 0), (0, 0), (0, 0),
                         (0, -0.05)]
    )
    # fig.set_constrained_layout(False)
    # ax[-1].set_axis_off()
    fig.savefig(img_path / "example2.pgf")


if __name__ == '__main__':
    plot_main()


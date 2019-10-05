import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from helper import gridplots, grid_labels, img_path, script_path


def main():
    fig, ax = gridplots(1, 2,
                        r=0.8,
                        ratio=2)
    # Left panel, use line plot
    ax_ = ax[0]
    ax_.plot(np.array([-2, -1, 0, 1, 2]),
             np.exp([1, 5, 10, 15, 20]))
    ax_.set_yscale("log")
    ax_.set_xlabel("$x$")
    ax_.set_xlabel("$y$")

    # Right panel, image plot
    ax_ = ax[1]
    xx, yy = np.meshgrid(np.linspace(-2, 2, 256) * np.pi,
                         np.linspace(-2, 2, 256) * np.pi)
    zz = np.sin(np.sqrt(xx ** 2 + yy ** 2) \
                * np.sign( xx / (yy +
                                 np.eps)))
    ax_.imshow(zz, extent=(xx.min(), xx.max(), yy.min(), yy.max()))
    ax_.set_xticks([])
    ax_.set_yticks([])

    grid_labels(fig, ax, offsets=[(0, 0), (0.02, 0)]
    )
    # fig.set_constrained_layout(False)
    # ax[-1].set_axis_off()
    fig.savefig(img_path / "example3.pdf")
    # tikzplotlib.save(img_path / "example2.tex")


if __name__ == '__main__':
    main()


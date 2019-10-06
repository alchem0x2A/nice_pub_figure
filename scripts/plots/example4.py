import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from helper import gridplots, grid_labels, img_path, script_path
from helper import savepgf
from helper.mpl_helper import add_img_ax


def plot_main():
    fig, ax = gridplots(1, 2,
                        r=1,
                        # gridspec_kw=dict(width_ratios=(1.3, 0.7)),
                        ratio=2.5)
    # fig.set_constrained_layout(False)
    # Left panel, use line plot
    
    ax_ = ax[0]
    add_img_ax(ax_, script_path.parent / "test/earth.jpg")

    ax_ = ax[1]
    xx, yy = np.meshgrid(np.linspace(-2, 2, 256) * np.pi,
                         np.linspace(-2, 2, 256) * np.pi)
    zz = np.cos(np.sqrt(xx ** 2 + yy ** 2) \
                * np.sign( xx / (yy +
                                 np.finfo(np.float).eps)))  # very small num
    ax_.imshow(zz, extent=(xx.min(), xx.max(), yy.min(), yy.max()))
    # ax_.imshow(zz)
    ax_.set_xticks([])
    ax_.set_yticks([])

    grid_labels(fig, ax
    )
    # ax[-1].set_axis_off()
    # fig.savefig(img_path / "example3.pgf")
    # fig.tight_layout()
    savepgf(fig, img_path / "example4.pgf")
    # tikzplotlib.save(img_path / "example2.tex")


if __name__ == '__main__':
    plot_main()


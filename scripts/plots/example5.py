import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from helper import gridplots, grid_labels, img_path, script_path
from helper import savepgf, add_img_ax


def plot_main():
    fig, ax = gridplots(2, 2,
                        r=0.8,
                        # gridspec_kw=dict(width_ratios=(1.3, 0.7)),
                        ratio=1)
    # fig.set_constrained_layout(False)
    # Left panel, use line plot
    
    add_img_ax(ax[0], script_path.parent / "test/mercury.jpg")
    ax[0].text(x=0.5, y=0.98, s="Mercury",
               color="white", ha="center", va="top",
               transform=ax[0].transAxes)
    add_img_ax(ax[1], script_path.parent / "test/bluvenus.jpg")
    ax[1].text(x=0.5, y=0.98, s="Venus",
               color="white", ha="center", va="top",
               transform=ax[1].transAxes)
    add_img_ax(ax[2], script_path.parent / "test/earth.jpg")
    ax[2].text(x=0.5, y=0.98, s="Earth",
               color="white", ha="center", va="top",
               transform=ax[2].transAxes)
    add_img_ax(ax[3], script_path.parent / "test/mars.jpg")
    ax[3].text(x=0.5, y=0.98, s="Mars",
               color="white", ha="center", va="top",
               transform=ax[3].transAxes)


    labels = grid_labels(fig, ax,
                reserved_space=(0, 0),
    )
    # labels[0].set_color("white")
    # ax[-1].set_axis_off()
    # fig.savefig(img_path / "example3.pgf")
    # fig.tight_layout()
    savepgf(fig, img_path / "example5.pgf")
    # tikzplotlib.save(img_path / "example2.tex")


if __name__ == '__main__':
    plot_main()


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from helper import gridplots, grid_labels, img_path
import tikzplotlib

mpl.rcdefaults()

pgf_dict = {"font.family": "sans-serif",
            "font.serif": [],                    # use latex default serif font
            "font.sans-serif": [],
            "pgf.rcfonts": False,
            # "legend.frameon": False,
            "figure.constrained_layout.use": True}

mpl.rcParams.update(**pgf_dict)


def main():
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
        ax_.plot(x, y, "o", markersize=2,
                 label="$y=\\{0}(x)$".format(func_names[i]))
        ax_.set_xlabel("$x$")
        ax_.set_ylabel("$y$")
        ax_.set_xticks(np.array([-2, -1, 0, 1, 2]) * np.pi)
        ax_.set_xticklabels([r"$-2\pi$", r"$-\pi$", "0",
                              r"$\pi$", r"$2\pi$"])
        ax_.set_ylim(-2, 2)
        ax_.legend(loc=1)

    ax[-1].set_xticks([])
    ax[-1].set_yticks([])
    grid_labels(fig, ax,
                # offsets=[(0, 0), (0, 0),
                                  # (0, -0.03)]
    )
    # fig.set_constrained_layout(False)
    # ax[-1].set_axis_off()
    fig.savefig(img_path / "example2.pgf")
    tikzplotlib.save(img_path / "example2.tex")


if __name__ == '__main__':
    main()


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from helper import gridplots, grid_labels, img_path

mpl.rcdefaults()

pgf_dict = {"font.family": "sans-serif",
            "font.serif": [],                    # use latex default serif font
            "font.sans-serif": [],
            "pgf.rcfonts": False,
            "figure.constrained_layout.use": True}

mpl.rcParams.update(**pgf_dict)


def main():
    fig, ax = gridplots(2, 2,
                        r=0.8,
                        ratio=1.3)
    functions = [np.sin, np.cos,
                 np.tan, lambda x: 1 / np.tan(x)]
    func_names = ["sin", "cos", "tan", "cot"]

    x = np.linspace(-2.0, 2.0, 255) * np.pi
    
    for i, ax_ in enumerate(ax):
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

    grid_labels(fig, ax,
                # offsets=[(0, 0), (0, 0),
                                  # (0, -0.03)]
    )

    fig.savefig(img_path / "example1.pgf")


if __name__ == '__main__':
    main()


# Helper functions for making plots
from pathlib import Path
import matplotlib as mpl
from matplotlib.pyplot import figure
from matplotlib.gridspec import GridSpec as GS
import numpy as np
import string
from .tex_helper import _get_textwidth, _get_preamble
from .path_helper import _module_path

mpl_file = _module_path / "matplotlibrc"
# Update the rcParams
mpl.rcdefaults()
mpl.rc_file(mpl_file.as_posix())

# Load the preamble
preamble = _get_preamble()
print(preamble)
if len(preamble) > 0:
    mpl.rcParams["pgf.preamble"] = preamble



_textwidth = _get_textwidth()
if _textwidth is None:
    _textwidth = 400            # Default values

def relsize(r=1.0, width=_textwidth, ratio=1.618, ppi=72):
    """Relative figure size to \\textwidth"""
    # print("Textwidth is: ", width)
    width_inch = r * width / ppi
    height_inch = r * width / ratio / ppi
    return width_inch, height_inch

def gridplots(nrows=1, ncols=1, span=[],
              r=1.0, ratio=1.618, ppi=72,
              width=None, **args):
    """Modified plt.subplots routine to allow combined grid cells
       For each grid, two digits are provided (row_span, col_span)
       Instead of 2D array, gridplots returns a plain list
    """
    if width is None:           # use automatic detection
        width = _textwidth
    figsize = relsize(r, width, ratio, ppi)
    print(figsize)
    fig = figure(figsize=figsize)
    print("Until here!")
    if (span is None) or (span == []) \
       or (ncols == 1 and nrows == 1):
        axs = fig.subplots(nrows, ncols, **args)
        return fig, axs.flatten()
    else:
        try:
            gs_kw = args["gridspec_kw"]
        except KeyError:
            gs_kw = dict()
        gs = GS(ncols, nrows, figure=fig, **gs_kw)        # Better way?
        axs = []
        r = 0
        c = 0            # counter for row and col
        for r, c, rs, cs in span:
            axs.append(fig.add_subplot(gs[r: r + rs, c: c + cs]))
        axs = np.array(axs)
        return fig, axs


def grid_labels(fig, axes, offsets=[],
                type="latin",
                decorate="{0}", **args):
    """Put the grid labels in a controlled position. 
       Guess the position
    """
    dummy_ax = fig.add_subplot(111)
    dummy_ax.set_axis_off()

    def label_(i, key):
        k = key[0]
        allowed_keys = ["l", "L",
                        "r", "R",
                        "n"]
        if k not in allowed_keys:
            k = "l"
        if k == "l":
            return string.ascii_lowercase[i]
        elif k == "L":
            return string.ascii_uppercase[i]
        elif k == "r":
            raise NotImplementedError
        elif k == "R":
            raise NotImplementedError
        else:                   # n
            return i + 1
    
    gs = axes.flat[0].get_gridspec()
    nr, nc = gs.get_geometry()
    # Determine the spacing each column and row
    hr = gs.get_height_ratios()
    if hr is None:
        h_spacings = np.ones(nr) / nr
    else:
        h_spacings = np.array(hr) / nr

    wr = gs.get_width_ratios()
    if wr is None:
        w_spacings = np.ones(nc) / nc
    else:
        w_spacings = np.array(wr) / nc
    
    for i, ax in enumerate(axes.flat):
        nr, nc, ri, rf, ci, cf = ax.get_subplotspec().get_rows_columns()
        print(i, ri, rf, ci, cf)
        left = np.sum(w_spacings[: ci])
        top = 1 - np.sum(h_spacings[: ri])
        print(left, top)
        try:
            w_offset, h_offset = offsets[i]
            left += w_offset
            top += h_offset
        except (TypeError, IndexError):
            pass

        defaults = dict(size="x-large", weight="bold",
                        ha="left", va="top")
        defaults.update(**args)
        dummy_ax.text(x=left, y=top,
                      s=decorate.format(label_(i, type)),
                      transform=fig.transFigure,
                      **defaults)
    return

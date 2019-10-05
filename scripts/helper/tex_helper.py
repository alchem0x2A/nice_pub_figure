# Handled several things about TeX output 

import re
from tempfile import gettempdir
from pathlib import Path
from subprocess import run
from .path_helper import tex_path


tex_file = tex_path / ".test.tex"
# header_file = tex_path / "header.tex"  # simple header file
header_file = tex_path / "preamble_plot.tex"  # simple header file
# print("TeX file is ", tex_file)

def _get_preamble():
    if header_file.exists():
        with open(header_file, "r") as f:
            content = f.readlines()
            
            content = filter(lambda s: len(s) > 0, map(lambda s: s.strip(),
                                                       content))
            content = filter(lambda s: s[0] != "%", content)
            return list(content)
    else:
        return []

def _render_TeX(engine="lualatex"):
    if tex_file.exists():
        command = [engine, "--draftmode",
                   "--interaction=\"nonstopmode\"",
                   "--output-directory={0}".format(gettempdir()),
                   tex_file.resolve().as_posix()]
        proc = run(" ".join(command),
                   capture_output=True,
                   shell=True, timeout=10,
                   cwd=tex_path)
        return proc.stdout.decode("utf8")
    else:
        return ""


def _get_textwidth(*arg, **argkw):
    output = _render_TeX(*arg, **argkw)
    # print(output)
    # print(output, type(output))
    pattern = r"^\>\s+([\d\.]+)pt.+?$"
    match = re.findall(pattern, output, re.MULTILINE)
    try:
        return float(match[-1])
    except IndexError:
        return None


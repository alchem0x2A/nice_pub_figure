# Handled several things about TeX output 

import re
from tempfile import gettempdir
from pathlib import Path
from subprocess import run
from .path_helper import tex_path


tex_file = tex_path / ".test.tex"
# print("TeX file is ", tex_file)

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
        return proc.stdout.decode("ascii")
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


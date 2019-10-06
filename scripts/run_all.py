from pathlib import Path
from importlib import import_module
from helper import clean_width_cache

root = Path(".")

# Customize this to exclude the submodules
exclude_mods = ["helper", "test"]
exclude_files = ["__init__", ]

func = "plot_main"


def main():
    for f in root.rglob("*.py"):
        # parents starting from root
        parents = list(map(lambda x: x.name, f.parents))[-1::-1]
        script_name = f.with_suffix("").name
        if (len(parents) > 1) and \
           (all([p not in exclude_mods for p in parents[1:]])) and \
           (script_name not in exclude_files):
            # import the module and test if plot_main is inside
            mod_name = ".".join(parents[1:] + [script_name])
            print(mod_name)
            try:
                m = import_module(mod_name)
            except ImportError:
                print("Module {0} import error!".format(mod_name))
                continue
            if hasattr(m, func):
                try:
                    getattr(m, func)()
                    print("Module {0} plot finish!".format(mod_name))
                except Exception as e:
                    print("Module {0} plot failed with {1}!".format(mod_name, e))

    # Clean up width
    clean_width_cache()

if __name__ == '__main__':
    main()

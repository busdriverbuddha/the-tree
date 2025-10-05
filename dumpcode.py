import argparse

from pathlib import Path

parser = argparse.ArgumentParser()


parser.add_argument(
    "module",
    type=str,
    choices=("frontend", "backend"),
    default="backend",
)

GLOB_PATTERNS = {
    'backend': ["*.py"],
    'frontend': [],
}

EXCLUDES = {
    'backend': ['migrations', '__pycache__'],
    'frontend': [],
}

BASEDIRS = {
    'backend': Path("./the_tree"),
    'frontend': Path("./the-tree-frontend"),
}


def get_file_list(module: str) -> list[Path]:
    basedir = BASEDIRS[module]
    excludes = EXCLUDES[module]
    glob_patterns = GLOB_PATTERNS[module]
    paths = []
    for pat in glob_patterns:
        for file in basedir.rglob(pat):
            relpath = file.relative_to(basedir)
            for excl in excludes:
                if excl in str(relpath):
                    break
            else:
                paths.append(relpath)
    return paths


def main(module: str):
    relpaths = get_file_list(module)
    for rp in relpaths:
        print(rp)


if __name__ == "__main__":
    args = parser.parse_args()
    main(
        args.module,
    )

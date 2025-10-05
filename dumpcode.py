import argparse

from pathlib import Path

parser = argparse.ArgumentParser()


parser.add_argument(
    "module",
    type=str,
    choices=("frontend", "backend"),
    default="backend",
)

COMMENT_PREFIX = {
    '.py': "#",
    '.js': "//",
    '.jsx': "//",
}

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


def tag_file(rel_path: Path, base_dir: Path):
    prefix = COMMENT_PREFIX.get(rel_path.suffix, None)
    abspath = base_dir / rel_path
    tag = f"{prefix} {rel_path}"
    print(tag)

    if prefix is None:
        return

    lines = abspath.read_text().splitlines()
    while lines and (lines[0].strip() == "" or lines[0].strip().startswith(prefix)):
        lines.pop(0)

    lines = [tag, ""] + lines + [""]
    text = "\n".join(lines)
    abspath.write_text(text)


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
    basedir = BASEDIRS[module]
    relpaths = get_file_list(module)
    for rp in relpaths:
        tag_file(rp, basedir)


if __name__ == "__main__":
    args = parser.parse_args()
    main(
        args.module,
    )

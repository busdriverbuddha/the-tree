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

DUMP_PATHS = {
    'backend': Path("./dump/backend-dump.txt"),
    'frontend': Path("./dump/frontend-dump.txt"),
}


def tag_file(rel_path: Path, base_dir: Path) -> str:
    prefix = COMMENT_PREFIX.get(rel_path.suffix, None)
    abspath = base_dir / rel_path
    tag = f"{prefix} {rel_path}"

    if prefix is None:
        assert False

    lines = abspath.read_text().splitlines()
    while lines and (lines[0].strip() == "" or lines[0].strip().startswith(prefix)):
        lines.pop(0)

    lines = [tag, ""] + lines + [""]
    text = "\n".join(lines)
    print(f"Writing into {abspath}...")
    abspath.write_text(text)
    return abspath.read_text()


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
    dump = []
    for rp in relpaths:
        dump.append(tag_file(rp, basedir))
    dump_path = DUMP_PATHS[module]
    dump_path.write_text("\n\n".join(dump))
    print(f"Dump written to {dump_path}.")

if __name__ == "__main__":
    args = parser.parse_args()
    main(
        args.module,
    )

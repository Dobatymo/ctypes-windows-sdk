import os
import subprocess
import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

from utils import fix_header_cst, transpile_header_file


def main(args: Namespace) -> None:
    header_files = [
        "shared/basetsd.h",
        "shared/ntdddisk.h",
        "shared/ntddstor.h",
        "shared/ntddscsi.h",
        "shared/nvme.h",
        "shared/scsi.h",
        "um/wingdi.h",
        "um/winioctl.h",
        "km/ata.h",
    ]
    header_files = list(map(Path, header_files))

    if not args.skip_transpile:
        for relpath in header_files.copy():
            print("transpile", relpath)

            inpath = args.in_path / relpath
            outpath = (args.out_path / relpath).with_suffix(".py")
            outpath.parent.mkdir(parents=True, exist_ok=True)

            transpile_header_file(inpath, outpath, relpath, args.pause_after_each_pattern)
            try:
                subprocess.run(
                    [sys.executable, "-m", "ruff", "format", os.fspath(outpath)],
                    capture_output=True,
                    check=True,
                    encoding="utf-8",
                )
            except subprocess.CalledProcessError as e:
                print(e.stdout)
                print(e.stderr)
                header_files.remove(relpath)

    if not args.skip_fix_cst:
        for relpath in header_files.copy():
            print("fixing enums", relpath)
            inpath = (args.out_path / relpath).with_suffix(".py")
            outpath = (args.out_path / relpath).with_name(relpath.stem + "_fixed.py")

            fix_header_cst(inpath, outpath)
            try:
                subprocess.run(
                    [sys.executable, "-m", "ruff", "format", os.fspath(outpath)],
                    capture_output=True,
                    check=True,
                    encoding="utf-8",
                )
            except subprocess.CalledProcessError as e:
                print(e.stdout)
                print(e.stderr)
                header_files.remove(relpath)

    for relpath in header_files.copy():
        print("ruff check", relpath)

        outpath = (args.out_path / relpath).with_name(relpath.stem + "_fixed.py")

        try:
            subprocess.run(
                [sys.executable, "-m", "ruff", "check", os.fspath(outpath), "--fix"],
                capture_output=True,
                check=True,
                encoding="utf-8",
            )
        except subprocess.CalledProcessError as e:
            print(e.stdout)
            print(e.stderr)
            header_files.remove(relpath)

    for relpath in header_files.copy():
        print("run file", relpath)

        outpath = (args.out_path / relpath).with_name(relpath.stem + "_fixed.py")

        try:
            subprocess.run(
                [sys.executable, os.fspath(outpath)],
                capture_output=True,
                check=True,
                encoding="utf-8",
            )
        except subprocess.CalledProcessError as e:
            print(e.stdout)
            print(e.stderr)
            header_files.remove(relpath)

    print("fully processed")
    print(header_files)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--in-path",
        type=Path,
        required=True,
        help="Path to Windows SDK headers. Eg. 'C:/Program Files (x86)/Windows Kits/10/Include/10.0.22621.0'.",
    )
    parser.add_argument("--out-path", type=Path, default=Path("."), help="Output path of Python files.")
    parser.add_argument("--pause-after-each-pattern", action="store_true")
    parser.add_argument("--skip-transpile", action="store_true")
    parser.add_argument("--skip-fix-cst", action="store_true")
    args = parser.parse_args()

    main(args)

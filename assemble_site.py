"""Składa katalog _site/ do publikacji na GitHub Pages.

python freeze.py --demo && python assemble_site.py

W _site/ ląduje: stara strona (wszystkie pliki z repozytorium poza źródłami nowej
strony i narzędziami) oraz nowa strona w demo/ (z build-demo/).
Tak samo robi workflow .github/workflows/pages.yml.
"""
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "_site"

# Pliki i katalogi z głównego katalogu, które nie należą do publikowanej strony.
SKIP_TOP = {
    ".github", ".gitignore", ".idea", "README.md", "CLAUDE.md", "requirements.txt",
    "app.py", "freeze.py", "flickr.py", "deploy_demo.py", "assemble_site.py",
    "data", "templates", "static", "tests", "docs",
}
SKIP_SUFFIX = {".rb"}  # narzędzie Ruby do newsów nie jest częścią strony


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    files = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
                           ).stdout.decode("utf-8").split("\0")
    count = 0
    for name in filter(None, files):
        path = Path(name)
        if path.parts[0] in SKIP_TOP or path.suffix in SKIP_SUFFIX:
            continue
        dest = OUT / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / path, dest)
        count += 1
    demo = ROOT / "build-demo"
    if not demo.exists():
        raise SystemExit("Brak build-demo/. Najpierw: python freeze.py --demo")
    shutil.copytree(demo, OUT / "demo")
    print(f"_site/: {count} plików starej strony + demo/")


if __name__ == "__main__":
    main()

"""Publikuje wersję pokazową pod blekitna14.org/demo/.

python deploy_demo.py          buduje demo i przygotowuje commit na gałęzi master
                               (w osobnym katalogu roboczym); nic nie wysyła
python deploy_demo.py --push   to samo, a na końcu wysyła master na GitHub

Strona blekitna14.org jest serwowana z gałęzi master, więc folder demo/ w master
pojawia się pod adresem /demo/. Reszta master (stara strona) zostaje bez zmian.
Żeby zdjąć demo: usuń folder demo/ z master.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # polskie znaki w konsoli Windows
PUSH = "--push" in sys.argv


def run(*cmd, cwd=ROOT):
    return subprocess.run(cmd, cwd=cwd, check=True, text=True, capture_output=True).stdout.strip()


def main():
    print("Buduję wersję demo...")
    subprocess.run([sys.executable, "freeze.py", "--demo"], cwd=ROOT, check=True)

    run("git", "fetch", "origin", "master")
    work = Path(tempfile.mkdtemp(prefix="blekitna-master-"))
    run("git", "worktree", "add", "-B", "demo-publish", str(work), "origin/master")
    try:
        target = work / "demo"
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(ROOT / "build-demo", target)

        run("git", "add", "-A", "demo", cwd=work)
        if not run("git", "status", "--porcelain", "demo", cwd=work):
            print("Brak zmian w demo, nic do zrobienia.")
            return
        branch = run("git", "rev-parse", "--short", "HEAD", cwd=ROOT)
        run("git", "commit", "-m", f"demo nowej strony (z redesign {branch})", cwd=work)
        sha = run("git", "rev-parse", "HEAD", cwd=work)
        # Commit zostaje na lokalnej gałęzi demo-publish (oparta na origin/master).
        if PUSH:
            run("git", "push", "origin", "demo-publish:master", cwd=work)
            print("Wysłano. Strona pojawi się pod https://blekitna14.org/demo/ po kilku minutach.")
        else:
            print(f"Commit {sha[:8]} gotowy na gałęzi demo-publish (nie wysłany). Żeby opublikować:")
            print("  git push origin demo-publish:master")
    finally:
        run("git", "worktree", "remove", "--force", str(work))


if __name__ == "__main__":
    main()

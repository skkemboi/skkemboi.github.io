"""Remove posts whose `date:` is in the future from this build only.

Runs inside GitHub Actions before `quarto render`. It deletes future posts from the
temporary build copy, never from your repository, so each post appears on its date.
"""
import datetime as dt
import pathlib
import re
import shutil
from zoneinfo import ZoneInfo

today = dt.datetime.now(ZoneInfo("America/Chicago")).date()

for qmd in sorted(pathlib.Path("posts").glob("*/index.qmd")):
    text = qmd.read_text(encoding="utf-8")
    header = text.split("---")[1] if text.startswith("---") else ""
    m = re.search(r"^date:\s*['\"]?(\d{4}-\d{2}-\d{2})", header, re.M)
    if not m:
        continue
    post_date = dt.date.fromisoformat(m.group(1))
    if post_date > today:
        shutil.rmtree(qmd.parent)
        print(f"hidden until {post_date}: {qmd.parent.name}")
    else:
        print(f"published: {qmd.parent.name}")

"""Build index.html from tools/index.template.html with the profile drawings inlined."""
import os, sys
here = os.path.dirname(__file__)
sys.path.insert(0, here)
from profiles import svg
t = open(os.path.join(here, "index.template.html"), encoding="utf-8").read()
subs = {
    "cup_nolabel": svg("cup", label=False), "bowl_nolabel": svg("bowl", label=False),
    "tallcup_nolabel": svg("tall cup", label=False), "wide_bowl_nolabel": svg("wide bowl", label=False),
    "cup": svg("cup"), "wide_bowl": svg("wide bowl"), "tallcup": svg("tall cup"), "bowl": svg("bowl"),
}
for k, v in subs.items():
    t = t.replace("{{" + k + "}}", v)
assert "{{" not in t
open(os.path.join(here, "..", "index.html"), "w", encoding="utf-8").write(t)
print("built index.html")

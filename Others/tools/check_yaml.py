"""Check every .pa.yaml in app/src: YAML parses, and control references resolve.

Usage: python tools/check_yaml.py [app/src]
Exit 0 when clean, 1 when a file fails to parse or a reference is unresolved.
"""
import glob
import os
import re
import sys

import yaml


class _Loader(yaml.SafeLoader):
    pass


_Loader.add_multi_constructor("tag:yaml.org,2002:", lambda loader, suffix, node: None)

SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "app", "src")
BUILTINS = {
    "Color", "Font", "Icon", "DisplayMode", "RGBA", "TextCanvas", "Spinner", "ButtonCanvas",
    "AlignInContainer", "LayoutDirection", "LayoutOverflow", "LayoutAlignItems", "BorderStyle",
    "VerticalAlign", "TextInputType", "SelectedItems", "NotificationType", "ScreenTransition", "FontWeight",
    "IconStyle", "TriggerOutput", "Value", "FormMode", "JSONFormat", "SortOrder", "DataSourceInfo",
    "Parent", "Self", "ThisItem", "ThisRecord", "User", "Table", "ParseJSON", "LookUp",
}
ok = True
declared = set()
texts = {}
for path in glob.glob(os.path.join(SRC, "*.pa.yaml")):
    text = open(path, encoding="utf-8").read()
    texts[path] = text
    try:
        yaml.load(text, Loader=_Loader)
    except yaml.YAMLError as e:
        ok = False
        print("PARSE FAIL", os.path.basename(path), "-", str(e).splitlines()[0])
    declared.update(re.findall(r"^\s*- ([A-Za-z_]\w*):\s*$", text, re.M))
for path, text in texts.items():
    refs = set(re.findall(r"\b([A-Z][A-Za-z0-9_]*)\.(?:X|Y|Width|Height|Text|Selected|Visible|Value|Checked|IsSelected|AllItems)\b", text))
    unresolved = sorted(r for r in refs if r not in declared and r not in BUILTINS and not r.startswith("Screen"))
    if unresolved:
        ok = False
        print("UNRESOLVED", os.path.basename(path), unresolved[:8])
print("OK" if ok else "FAILED", f"({len(texts)} files, {len(declared)} controls)")
sys.exit(0 if ok else 1)

"""Build standalone ChatGPT upload archives from the field guide."""
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "downloads" / "chatgpt"
ARTICLE = re.compile(r"\[([^\]]+)\]\(https://www\.woodworkingcanada\.com/[^)]+\)")
SIBLING = re.compile(r"\[([\w-]+)\]\(\.\./[\w-]+/SKILL\.md\)")


def package(skill):
    files = [skill / "SKILL.md", *sorted(skill.glob("references/**/*.md"))]
    with ZipFile(OUTPUT / f"{skill.name}.zip", "w") as archive:
        for file in files:
            body = ARTICLE.sub(r"“\1” (Sepp Gmeiner, Woodworking Canada)", file.read_text())
            body = SIBLING.sub(r"`\1`", body)
            body = body.replace("Read the selected specialist through its link below or invoke its installed name.",
                                "Invoke the selected specialist by its installed name.")
            if re.search(r"https?://|www\.", body, re.I):
                raise ValueError(f"Unexpected external address in {file}")
            entry = ZipInfo(file.relative_to(ROOT).as_posix())
            archive.writestr(entry, body.encode(), compress_type=ZIP_DEFLATED)


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for instructions in sorted(ROOT.glob("*/SKILL.md")):
        package(instructions.parent)

from datetime import date
from pathlib import Path
import shutil
import sys
import re


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
CASES = ROOT / "cases"


FILES = {
    "recon-notes.md": "recon-notes.md",
    "evidence-log.md": "evidence-log.md",
    "findings.md": "vulnerability-writeup.md",
    "disclosure-email.md": "disclosure-email.md",
    "retrospective.md": "project-retrospective.md",
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def create_case(name: str) -> Path:
    slug = slugify(name)

    if not slug:
        raise ValueError("Case name must contain letters or numbers.")

    folder_name = f"{date.today().isoformat()}-{slug}"
    case_path = CASES / folder_name
    case_path.mkdir(parents=True, exist_ok=False)

    for output_name, template_name in FILES.items():
        shutil.copyfile(TEMPLATES / template_name, case_path / output_name)

    return case_path


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python tools/create_case.py <case-name>")
        sys.exit(1)

    case_name = " ".join(sys.argv[1:])

    try:
        case_path = create_case(case_name)
    except FileExistsError:
        print("Error: case folder already exists.")
        sys.exit(1)
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)

    print(f"Created case folder: {case_path}")


if __name__ == "__main__":
    main()

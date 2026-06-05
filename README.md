# Tsova Research Kit

> Mapping systems. Studying failures. Building discipline.

Tsova Research Kit is a lightweight defensive research framework for organizing vulnerability notes, evidence logs, disclosure drafts, and technical write-ups.

This project is intended for ethical security research, responsible documentation, and structured learning.

## Features

- Vulnerability write-up template
- Recon notes template
- Evidence log template
- Disclosure email template
- Project retrospective template
- Simple Python case-folder generator

## Project Structure

tsova-research-kit/
+- templates/
+- examples/
+- tools/
+- docs/
+- cases/
+- README.md
+- LICENSE
+- .gitignore

## Usage

Create a new case folder:

python tools/create_case.py example-target

This creates:

cases/YYYY-MM-DD-example-target/
+- recon-notes.md
+- evidence-log.md
+- findings.md
+- disclosure-email.md
+- retrospective.md

## Intended Use

This kit is for:

- Defensive cybersecurity notes
- Responsible vulnerability disclosure
- Lab documentation
- Learning-oriented research
- Personal research organization

Do not use this project to support unauthorized access, exploitation, harassment, or abuse.

## License

See LICENSE.

#!/usr/bin/env python3

from tika import parser
from pathlib import Path

pdf_file = Path("printme.pdf")
if not pdf_file.exists():
    print(f"{pdf_file.resolve()} does not exist")
    sys.exit(1)

parsed = parser.from_file(str(pdf_file))

extracted_raw = Path("printme_extracted_raw.txt")
if parsed['status'] == 200:
    with extracted_raw.open('w') as fo:
        fo.write(parsed['content'])
    print(f"Wrote to {extracted_raw.resolve()}")

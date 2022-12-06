from pathlib import Path

def get_html(in_file: str):
    raw_html = Path(in_file)
    with raw_html.open() as fo:
        return fo.read()

def output_html(clean_html, out_file):
    with out_file.open('w') as fo:
        fo.write(clean_html)
        print(f"Wrote to {out_file}")

head = get_html("head.txt")
tail = get_html("tail.txt")
raw = get_html("mainTable-raw.html")
cleaned = raw.replace('<tr>', '<tr tabindex="0">')
cleaned = cleaned.replace('[object Object],', '')
cleaned = cleaned.replace('[object Object]', '')
html = head + cleaned + tail
output_html(html, Path('../static/static.html'))

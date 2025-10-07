from pathlib import Path
from formatter import process_markdown_file

posts_dir = Path(__file__).parent.parent / "_posts"

# posts_dir = Path(__file__).parent

print(posts_dir)

md_files = list(posts_dir.glob("*.md"))

if not md_files:
    print("No markdown files found.")
    exit(0)

for f in md_files:
    print(f"Processing {f} ...")
    try:
        process_markdown_file(f)
    except Exception as e:
        print(f"Error processing {f}: {e}")

print("All files processed.")

import re
from pathlib import Path
from language_analysis import split_verse

def format_verse_block(verse_text, author="", meter="", anvaya="धेयम्! पदच्छेदो यन्त्रसाधितत्वाद् अशुद्धो भवितुम् अर्हति।"):
    return f'''{{% include verse.html
   author="{author}"
   meter="{meter}"
   verse="
   {verse_text}
   "
   anvaya="{anvaya}"
%}}'''

def process_markdown_file(file_path):
    print(f"Processing: {file_path}...")
    text = Path(file_path).read_text(encoding="utf-8")

    # Match both `{% verse ... %}` and `{% include verse.html ... %}`
    verse_block_pattern = re.compile(
        r'(\{%\s*(?:include\s+verse\.html|verse)[^%]*?verse\s*=\s*"(?P<verse>[^"]*?)"\s*[^%]*?%})',
        re.MULTILINE,
    )

    def replace_block(match):
        original_block = match.group(1)
        verse_text = match.group("verse").strip()

        # Extract optional existing author/meter/anvaya fields
        author_match = re.search(r'author\s*=\s*"([^"]*)"', original_block)
        meter_match = re.search(r'meter\s*=\s*"([^"]*)"', original_block)
        anvaya_match = re.search(r'anvaya\s*=\s*"([^"]*)"', original_block)

        author = author_match.group(1) if author_match else ""
        meter = meter_match.group(1) if meter_match else ""
        anvaya = anvaya_match.group(1) if anvaya_match else ""

        # Skip pre-formatted verses
        if "|" in verse_text or "_" in verse_text:
            print("\tSkipping pre-split verse.")
            return original_block

        print("\tAuto-splitting verse...")
        # print(verse_text)
        formatted_verse = split_verse(verse_text)
        # print(formatted_verse)
        if anvaya=='':
            return format_verse_block(formatted_verse, author=author, meter=meter)
        else:
            return format_verse_block(formatted_verse, author=author, meter=meter, anvaya=f"\nधेयम्! उपरि दर्शितः पदच्छेदो यन्त्रसाधितत्वाद् अशुद्धो भवितुम् अर्हति। अन्वयोऽयमेव शुद्धः।\n\n{anvaya}")

    updated_text = verse_block_pattern.sub(replace_block, text)
    Path(file_path).write_text(updated_text, encoding="utf-8")
    print(f"Updated: {file_path}")

if __name__ == "__main__":
    test = """
लक्ष्मीशः सुततां गतोऽजजनुषः कृत्स्नाञ्जनान्ह्लादयं\
स्ताताज्ञामनुपालयन्स गहनं सीतानुजाभ्यामयात्।
पौलस्त्योऽपनिनाय तस्य दयितां तं कौसलः सानुग\
माहत्य क्षितिबाधकं कपिबलैः साकं ह्ययोध्यागमत्॥
"""
    # print(format_verse_block(test))
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 formatter.py path/to/file.md")
        sys.exit(1)
    process_markdown_file(sys.argv[1])


    # match = Chandas.classify(test)

    # print(match)
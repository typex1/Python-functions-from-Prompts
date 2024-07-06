import ebooklib
from ebooklib import epub

def extract_text_from_epub(epub_file, output_file):
    """
    Prompt: Write a Python function that can extract all text from a given file in EPUB format. The text is written to an output file.
    ----
    Extract all text from an EPUB file and write it to an output file.

    Args:
        epub_file (str): The path to the EPUB file.
        output_file (str): The path to the output file where the text will be written.

    Returns:
        None
    """
    book = epub.read_epub(epub_file)
    text = ""

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            bytes_content = item.get_content()
            try:
                text += bytes_content.decode('utf-8')
            except UnicodeDecodeError:
                pass

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Text extracted from {epub_file} and written to {output_file}")
    
extract_text_from_epub('/home/ec2-user/environment/data/TheHousemaidFreidaMcFadden.epub', '/home/ec2-user/environment/data/TheHousemailFreidaMcFadden.txt')
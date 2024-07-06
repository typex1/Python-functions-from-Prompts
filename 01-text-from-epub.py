import zipfile
import re
from bs4 import BeautifulSoup

def extract_text_from_epub(epub_file, output_file):
    """
    Prompt: Write a Python function that can extract all text from a given file in EPUB format. The text is written to an output file as plain text, no XML or HTML.
    ---
    Extracts all text from an EPUB file and writes it to an output file as plain text.

    Args:
        epub_file (str): The path to the EPUB file.
        output_file (str): The path to the output file where the extracted text will be written.
    """
    with zipfile.ZipFile(epub_file, 'r') as epub_zip:
        # Get a list of all files in the EPUB archive
        file_list = epub_zip.namelist()

        # Find the file(s) containing the HTML content
        html_files = [f for f in file_list if f.endswith('.html') or f.endswith('.xhtml')]

        # Initialize an empty string to store the extracted text
        extracted_text = ''

        for html_file in html_files:
            # Read the HTML content from the file
            with epub_zip.open(html_file) as html_content:
                html_data = html_content.read().decode('utf-8')

                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(html_data, 'html.parser')

                # Extract the text from the HTML content
                text = soup.get_text()

                # Remove unwanted characters and line breaks
                text = re.sub(r'\s+', ' ', text).strip()

                # Append the extracted text to the overall text
                extracted_text += text + '\n\n'

    # Write the extracted text to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(extracted_text)
    
extract_text_from_epub('/home/ec2-user/environment/data/TheHousemaidFreidaMcFadden.epub', '/home/ec2-user/environment/data/TheHousemaidFreidaMcFadden.txt')
import zipfile
import xml.etree.ElementTree as ET
import os
import html

"""
prompt: Write a Python function that can extract all text from a given file in EPUB format. The text is written to an output file as plain text, no XML or HTML. Line breaks have to be preserved.
"""

def extract_text_from_epub(epub_path, output_path):
    # Open the EPUB file
    with zipfile.ZipFile(epub_path, 'r') as epub:
        # Find the content.opf file
        opf_path = next(name for name in epub.namelist() if name.endswith('content.opf'))
        
        # Parse the content.opf file
        opf = ET.fromstring(epub.read(opf_path))
        
        # Find all item elements with media-type="application/xhtml+xml"
        namespace = {'opf': 'http://www.idpf.org/2007/opf'}
        items = opf.findall(".//opf:item[@media-type='application/xhtml+xml']", namespace)
        
        # Extract text from each XHTML file
        all_text = []
        for item in items:
            href = item.get('href')
            file_path = os.path.join(os.path.dirname(opf_path), href)
            
            try:
                content = epub.read(file_path).decode('utf-8')
                root = ET.fromstring(content)
                
                # Extract text from all elements
                for elem in root.iter():
                    if elem.text:
                        text = elem.text.strip()
                        if text:
                            all_text.append(html.unescape(text))
                    if elem.tail:
                        tail = elem.tail.strip()
                        if tail:
                            all_text.append(html.unescape(tail))
                
                # Add a newline after each file to preserve structure
                all_text.append('\n')
            
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")
        
        # Write the extracted text to the output file
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(all_text))

# Example usage
epub_file =   '/home/ec2-user/environment/data/UnterDerDrachenwandArnoGeiger.epub'
output_file = '/home/ec2-user/environment/data/UnterDerDrachenwandArnoGeiger.txt'
extract_text_from_epub(epub_file, output_file)
import zipfile
import re
from xml.etree import ElementTree as ET


def extract_text_from_docx(file_path):

    with zipfile.ZipFile(file_path, "r") as docx:
        xml_content = docx.read("word/document.xml")

    root = ET.fromstring(xml_content)

    namespace = {
        "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    }

    paragraphs = []

    for paragraph in root.findall(".//w:p", namespace):

        words = []

        for text_element in paragraph.findall(".//w:t", namespace):
            if text_element.text:
                words.append(text_element.text)

        paragraph_text = "".join(words).strip()

        if not paragraph_text:
            continue

        # Ignore extremely large combined/layout paragraphs
        if len(paragraph_text) > 1000:
            continue

        paragraphs.append(paragraph_text)

    # Remove duplicate paragraphs while preserving order
    cleaned_paragraphs = []
    seen = set()

    for paragraph in paragraphs:

        normalized = re.sub(r"\s+", " ", paragraph).strip()

        if normalized not in seen:
            cleaned_paragraphs.append(normalized)
            seen.add(normalized)

    text = "\n".join(cleaned_paragraphs)

    # Clean excessive spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Clean excessive blank lines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()
from resume_parser.docx_parser import extract_text_from_docx


docx_path = "sample_resume.docx"

text = extract_text_from_docx(docx_path)

print(text)
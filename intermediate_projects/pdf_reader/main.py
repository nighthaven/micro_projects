import re
from collections import Counter
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, "rb") as pdf:
        reader = PdfReader(pdf, strict=False)

        print("Pages:", len(reader.pages))
        print("-"* 10) # Divider

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text

def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r"\s+|[,;?!.-]\s*", text.lower())
        all_words += [word for word in split_text if word]
    return Counter(all_words)



def main():
    extracted_text = extract_text_from_pdf("sample.pdf")
    counter: Counter = Counter(extracted_text)

    for word, mentions in counter.most_common(5):
        print(f"{word:10}: {mentions} times")

if __name__ == "__main__":
    main()


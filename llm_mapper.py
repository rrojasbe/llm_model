#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv
from PyPDF2 import PdfReader
from openai import OpenAI

# Step 1: Initialize OpenAI client with your API key
client = OpenAI(api_key="sk-xxx")  #  Replace with your real key

# Step 2: Function to extract text from PDF
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Step 3: 
def extract_workflow_via_llm(text):
    prompt = f"""
    You are a research assistant helping map scientific workflows.
    Given the following article excerpt, extract the workflow steps (data collection, preprocessing, analysis, modeling, etc.)
    and return them as a numbered list. Focus only on METHODS.

    ARTICLE:
    {text}

    Output only the numbered list.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful scientific assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# Step 4: 
def write_to_csv(output_file, data):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Step Number", "Description"])
        for i, line in enumerate(data, 1):
            writer.writerow([i, line.strip()])

# Step 5: Main function
def main(pdf_path, output_csv_path):
    print("📄 Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    print("🤖 Sending to GPT-4o to extract workflow...")
    workflow_text = extract_workflow_via_llm(text)

    steps = [line for line in workflow_text.split("\n") if line.strip()]
    write_to_csv(output_csv_path, steps)

    print(f"✅ Done! Extracted workflow saved to: {output_csv_path}")

# Step 6: Run 
if __name__ == "__main__":
    pdf_path = "sample_article.pdf"       # Replace with your PDF name if different
    output_csv = "workflow_output.csv"
    main(pdf_path, output_csv)

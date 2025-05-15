#  LLM-Powered Research Workflow Extractor

This project uses OpenAI's GPT API to extract structured research workflows from scientific PDF articles.

##  What It Does

- Reads a PDF file (research article)
- Uses an LLM (using model 4o) to identify key workflow steps in the Methods section
- Outputs those steps into a structured CSV file

##  Tech Stack

- Python 3.10+
- OpenAI API (`openai` library)
- PDF parsing (`PyPDF2`)
- CSV writing

##  File Structure
llm_mapper.py # Main script
sample_article.pdf # Example paper (not included in repo)
workflow_output.csv # Output of extracted steps

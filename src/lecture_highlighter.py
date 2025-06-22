from .text_extractors import extract_text
from .summarizer import Summarizer
from .file_processor import save_summary

class LectureHighlighter:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        """Initialize the lecture highlighter with a summarizer."""
        self.summarizer = Summarizer(model_name)

    def process_file(self, input_file, output_dir="summaries"):
        """Process the input file and save the summary."""
        try:
            # Extract text
            text = extract_text(input_file)
            if not text:
                raise ValueError("No text extracted from the file.")

            # Generate summary
            summary = self.summarizer.summarize_text(text)

            # Save summary
            return save_summary(input_file, summary, output_dir)
        except Exception as e:
            return f"Error processing file: {str(e)}"
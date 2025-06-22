from transformers import pipeline

class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        """Initialize the summarization pipeline."""
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def summarize_text(self, text, max_length=1000, min_length=200):
        """Generate a summary of the provided text."""
        try:
            # Split text into chunks if too long for the model (BART max token limit ~1024)
            chunk_size = 1000  # Approximate token limit
            chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
            summaries = []
            
            for chunk in chunks:
                if chunk.strip():
                    summary = self.summarizer(
                        chunk,
                        max_length=max_length // len(chunks) + 50,
                        min_length=min_length // len(chunks) + 30,
                        do_sample=False
                    )[0]["summary_text"]
                    summaries.append(summary)
            
            # Combine summaries
            return " ".join(summaries).strip()
        except Exception as e:
            raise ValueError(f"Error summarizing text: {str(e)}")
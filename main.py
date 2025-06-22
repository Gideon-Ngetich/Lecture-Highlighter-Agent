import os
from src.lecture_highlighter import LectureHighlighter

def main():
    """Main function to run the lecture highlighter locally."""
    highlighter = LectureHighlighter()
    
    input_file = input("Enter the path to your lecture file (DOCX, PDF, or PPT): ").strip()
    
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found. Please check the path and try again.")
        return
    
    result = highlighter.process_file(input_file)
    print(result)

if __name__ == "__main__":
    main()
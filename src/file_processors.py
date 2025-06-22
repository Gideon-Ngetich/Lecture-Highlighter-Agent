import os
from datetime import datetime

def save_summary(input_file, summary, output_dir="summaries"):
    """Save the summary to a text file."""
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Generate output file path
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}_summary_{timestamp}.txt")

        # Write summary to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"Summary of {base_name}\n")
            f.write("=" * 50 + "\n\n")
            f.write(summary)

        return f"Summary saved to {output_file}"
    except Exception as e:
        return f"Error saving summary: {str(e)}"
import os

def load_documents_from_directory(directory_path: str) -> str:
    """
    Loads all text files from a given directory and returns a single concatenated string.
    """
    combined_text = ""
    if not os.path.exists(directory_path):
        return combined_text
        
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt") or filename.endswith(".md"):
            with open(os.path.join(directory_path, filename), "r", encoding="utf-8") as f:
                combined_text += f.read() + "\n\n"
                
    return combined_text

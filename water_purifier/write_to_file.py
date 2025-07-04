#this file is to write the output to a markdown file
class DataWriter:
    def __init__(self, output, url):
        self.output = output
        self.url = url

    def write_output_to_file(self):
        with open("output.md", "w", encoding="utf-8") as f:
            f.write("## The source file is:\n")
            f.write(f"URL: {self.url}\n\n")
            f.write("## Data fetched from the URL:\n\n")

            f.write("The response from the LLM is:\n")
            f.write(self.output + "\n\n")

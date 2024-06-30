#Extract the transcript from YouTube video and save it to the text file.
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.docstore.document import Document
import textwrap
import string 

url = input("Paste your YouTube url: ")
loader = YoutubeLoader.from_youtube_url(
    url, 
    add_video_info=True 
)
docs = loader.load()
for doc in docs: 
    
    document = Document(
        page_content = doc.page_content,
        metadata = doc.metadata 
        )
    del document.metadata['source']
    
    filename = document.metadata['title']
    exclude = set(string.punctuation)
    filename = "".join(ch for ch in filename if ch not in exclude)

    wrapped_text = textwrap.fill(document.page_content, width=80) 

    with open(filename + ".txt", "w", encoding="utf-8") as file:

        file.write(str(document.metadata["title"]) + "\n")
        file.write(str(document.metadata["author"]) + "\n")        
        file.write("\n")
        file.write(str(wrapped_text))

#Copy the text file and save it to Word document. 
from docx import Document 

with open(filename + ".txt", "r", encoding="utf-8") as txt_file:
    text_content = txt_file.read()

document = Document()
document.add_paragraph(text_content)

document.save(filename + ".docx")

from langchain_community.document_loaders import YoutubeLoader
from langchain_community.docstore.document import Document
import textwrap

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
    
    filename = document.metadata['title'].replace(' ', '_')
    wrapped_text = textwrap.fill(document.page_content, width=80) 

    with open(filename + ".txt", "w", encoding="utf-8") as file:

        file.write(str(document.metadata["title"]) + "\n")
        file.write(str(document.metadata["author"]) + "\n")        
        file.write("\n")
        file.write(str(wrapped_text))
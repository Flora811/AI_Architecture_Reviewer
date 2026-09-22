from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


from fastapi import FastAPI, UploadFile, File, HTTPException

#load_dotenv allows python to read api key from our .env file
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from pydantic import BaseModel

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

#serve css and js files
app.mount(
    "/static",
    StaticFiles(directory=TEMPLATES_DIR),
    name="static"
)

load_dotenv()

#object for our AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

# define what an architecture reviewer should contain
class ArchitectureReview(BaseModel):
    pros: list[str]
    cons: list[str]
    
# define the complete API response
class ReviewResponse(BaseModel):
    filename: str
    content_type: str
    review: ArchitectureReview
    
#Configure Gemini to return structured output
structured_llm = llm.with_structured_output(
    ArchitectureReview,
    method="json_schema"
)

@app.get("/")
def home():
    return FileResponse(TEMPLATES_DIR / "index.html")

@app.post("/review", response_model=ReviewResponse)
async def review_architecture(file: UploadFile = File(...)):
    
    #Validation of the upload file - it should only be .md
    if not file.filename.lower().endswith(".md"):
        raise HTTPException(
            status_code=400,
            detail="Only Markdown (.md) files are allowed."
        )
    
    # Read the file contents
    contents = await file.read()
    
    # Convert bytes into Python String
    try:
        markdown_text = contents.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="The markdown file must use UTF-8 encoding"
        )
    
    # Check if the file is empty
    if not markdown_text.strip():
        raise HTTPException(
            status_code=400,
            detail="The markdown file is empty."
        )
        
    #create our prompt
    prompt = f"""
    You are an experienced software architect.

    Review the following software architecture described
    in Markdown format.

    Analyze the architecture diagram and the considerations
    provided in the document.

    Identify the architectural strengths (PROS)
    and weaknesses (CONS).

    Consider:
    - Scalability
    - Security
    - Performance
    - Maintainability
    - Reliability

    Do not assume that undocumented components are absent.
    Clearly distinguish missing information from confirmed
    architectural weaknesses.

    Provide a concise review with two sections:

    PROS:
    - ...

    CONS:
    - ...

    ARCHITECTURE DOCUMENT:

    {markdown_text}
    """
    
    # send the prompt to gemini
    review = await structured_llm.ainvoke(prompt)
    
    # We dont need to extract the response now
    
    #return the review
    return{
        "filename" : file.filename,
        "content_type" : file.content_type,
        "review" : review
    }
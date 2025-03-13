from typing import Annotated
from fastapi import Body, FastAPI,Form,Request
from fastapi.responses import JSONResponse
import uvicorn
from dotenv import load_dotenv
import sendmail
import json
load_dotenv()
app = FastAPI()

@app.post("/send_mail")
async def sendMail(request: Annotated[dict, Body()] = None):
    try:
        info = request.get("info", None)
        if info is not None:
            try:
                info = info if isinstance(info, dict) else json.loads(info)
                sendmail.send_mail(to=info["email"], __data=info)
            except Exception as e:
                print(f"Error in API INFO Error:CGR001\t {e}")
                return JSONResponse(
                    status_code=422,
                    content={"error": "Invalid Info Data."},
                )
        return JSONResponse(status_code=200, content={"message": "Email sent successfully."})
    
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

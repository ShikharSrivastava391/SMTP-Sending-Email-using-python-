from typing import Annotated
from fastapi import status, Body, FastAPI,Form,Request
from fastapi.responses import JSONResponse
import uvicorn
import os
import sqlite3
import pandas as pd
# from hackathonAPI import *
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
# from ScrapingAlgorithm import WebScraper
from dotenv import load_dotenv
import google.generativeai as genai
# from salesforceKnowledgeArticle import FetchSchema
from fastapi.middleware.cors import CORSMiddleware
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import server
# from GirikonSendMail import send_mail
import json
# from salesforceObjectData import FetchAssociatedObjects
load_dotenv()
app = FastAPI()

@app.post("/ai_web_agent_prod/ScrappingAlgorithm")
async def ScrapperAlgorithm(request: Annotated[dict, Body()] = None):
    try:
        info = request.get("info", None)
        print("info is:-", info)
        print("sending mail logic")
        
        if info is not None:
            try:
                info = info if isinstance(info, dict) else json.loads(info)
                server.send_mail(to=info["email"], __data=info)
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

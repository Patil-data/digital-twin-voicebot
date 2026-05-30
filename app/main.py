import os
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response, JSONResponse
from app.asr_handler import transcribe_audio
from app.tts_handler import synthesize_speech
from app.twin import match_question

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("app/static/index.html") as f:
        return f.read()

@app.post("/ask")
async def ask(audio: UploadFile = File(...)):
    audio_bytes = await audio.read()
    transcript = await transcribe_audio(audio_bytes, audio.filename)
    response_text = match_question(transcript)
    audio_response = synthesize_speech(response_text)
    return Response(content=audio_response, media_type="audio/mpeg")

@app.post("/ask-text")
async def ask_text(request: Request):
    data = await request.json()
    question = data.get("question", "")
    response_text = match_question(question)
    audio_response = synthesize_speech(response_text)
    return Response(content=audio_response, media_type="audio/mpeg")

@app.post("/ask-text-only")
async def ask_text_only(request: Request):
    data = await request.json()
    question = data.get("question", "")
    response_text = match_question(question)
    return JSONResponse({"text": response_text})
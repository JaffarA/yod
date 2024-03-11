from fastapi import FastAPI, HTTPException

from utils import Session, generate_session_id

app = FastAPI()


# global store
sessions: dict[str, Session] = {}


@app.post("/session", status_code=201)
def generate_session(session: Session) -> str:
    session_id = generate_session_id()
    session.session_id = session_id
    sessions[session_id] = session
    return session_id


@app.get("/session/{session_id}/", status_code=200)
def get_session(session_id: str) -> Session:
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    return sessions[session_id]


@app.get("/session/{session_id}/{part}/{data}", status_code=200)
def send_part(session_id: str, part: int, data: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    if part in sessions[session_id].parts:
        raise HTTPException(status_code=400, detail="Part already exists")
    sessions[session_id].parts[part] = data
    return "OK"

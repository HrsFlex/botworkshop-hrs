import time
from typing import Dict, List, Any

class SessionManager:
    def __init__(self):
        # Format: {session_id: {"context": [], "data": {}, "last_accessed": timestamp}}
        self.sessions: Dict[str, Dict[str, Any]] = {}

    def get_session(self, session_id: str) -> Dict[str, Any]:
        """Retrieve or create a session."""
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "context": [],
                "data": {},
                "last_accessed": time.time()
            }
        else:
            self.sessions[session_id]["last_accessed"] = time.time()
        return self.sessions[session_id]

    def clear_session(self, session_id: str):
        """Reset a session's data."""
        if session_id in self.sessions:
            self.sessions[session_id] = {
                "context": [],
                "data": {},
                "last_accessed": time.time()
            }

    def cleanup_old_sessions(self, max_age_seconds: int = 3600):
        """Remove sessions older than max_age_seconds."""
        current_time = time.time()
        expired_sessions = [
            sid for sid, data in self.sessions.items() 
            if current_time - data["last_accessed"] > max_age_seconds
        ]
        for sid in expired_sessions:
            del self.sessions[sid]

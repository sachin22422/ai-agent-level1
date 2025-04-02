import logging
import subprocess
import sys
import os

async def perform_action(translated_command: str):
    try:
        logging.info(f"📥 Received instruction: {translated_command}")

        if "youtube" in translated_command.lower():
            script_path = os.path.join("app", "actions", "youtube_action.py")
            subprocess.Popen([sys.executable, script_path])
            return {"status": "success", "message": "Started YouTube search in separate process"}

        elif "amazon" in translated_command.lower():
            script_path = os.path.join("app", "actions", "amazon_action.py")
            subprocess.Popen([sys.executable, script_path])
            return {"status": "success", "message": "Started Amazon search in separate process"}

        return {"status": "unknown", "message": "No matching automation rule"}

    except Exception as e:
        logging.error(f"❌ Exception: {e}")
        return {"status": "error", "message": str(e)}

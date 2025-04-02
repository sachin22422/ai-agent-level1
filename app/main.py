from fastapi import FastAPI
from pydantic import BaseModel
from app.interact_api import interact
import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
app = FastAPI()

class CommandInput(BaseModel):
    command: str

@app.post("/interact")
async def interact_api(input: CommandInput):
    return await interact(input.command)

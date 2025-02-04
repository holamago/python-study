#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

"""
How to run
uvicorn app:app --reload --host=0.0.0.0 --port=59931
"""

import os
import sys
sys.path.append(f"{os.environ['HOME']}/python-study")
sys.path.append(f"{os.environ['HOME']}/python-study/saturn")
from backend import app
from backend.routes import api
from backend.config import APP_NAME, VERSION, COMPANY, CONTACT
import uvicorn

app.include_router(api.router)

@app.get("/")
async def service():
    return {
        "app": APP_NAME,
        "version": VERSION,
        "company": COMPANY,
        "contact": CONTACT,
    }

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
    )
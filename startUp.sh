#!/bin/bash
source env/bin/activate
uvicorn application.app:app --reload

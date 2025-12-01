# spectre-transport-demo
Demo backend for coordinating a robot, gripper and plate pusher (simulation).

# spectre-transport-demo

A small demo backend built with **FastAPI** that simulates the coordination of
three devices often found in lab automation:

- a SCARA-like robot arm  
- a gripper  
- a plate pusher  

The idea is inspired by my work on plate transport automation, where a backend
coordinates moves between different stations using clear API calls and
asynchronous execution. All devices in this repo are simulated.

## Features

- FastAPI backend with a simple `/health` endpoint  
- `/transport` endpoint that simulates a plate move from station A to B  
- Separate clients for:
  - `RobotClient` – moves between named positions
  - `GripperClient` – open/close actions
  - `PlatePusherClient` – move to indexed positions

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

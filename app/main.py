```python
from fastapi import FastAPI
from pydantic import BaseModel

from .clients import RobotClient, GripperClient, PlatePusherClient

app = FastAPI(
    title="spectre-transport-demo",
    description="Simulated backend that coordinates a robot, gripper and plate pusher.",
    version="0.1.0",
)


class TransportRequest(BaseModel):
    source: str = "A"
    destination: str = "B"


class TransportResult(BaseModel):
    status: str
    source: str
    destination: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/transport", response_model=TransportResult)
async def run_transport(req: TransportRequest):
    """
    Simulate a plate transport from source to destination.
    """

    robot = RobotClient()
    gripper = GripperClient()
    pusher = PlatePusherClient()

    # Example sequence:
    # 1) Move robot to source-safe, open gripper, move in, close, move out
    await robot.move_to(f"{req.source}-safe")
    await gripper.open()
    await robot.move_to(f"{req.source}-dock")
    await gripper.close()
    await robot.move_to(f"{req.source}-safe")

    # 2) Use plate pusher at the source side (simulated)
    await pusher.move_to_site(f"{req.source}_handover")

    # 3) Move robot to destination and release
    await robot.move_to(f"{req.destination}-safe")
    await robot.move_to(f"{req.destination}-dock")
    await gripper.open()
    await robot.move_to(f"{req.destination}-safe")

    # 4) Plate pusher at destination
    await pusher.move_to_site(f"{req.destination}_handover")

    return TransportResult(
        status="completed",
        source=req.source,
        destination=req.destination,
    )

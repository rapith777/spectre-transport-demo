import asyncio
import logging

logger = logging.getLogger(__name__)


class RobotClient:
    """
    Simulated SCARA-like robot client.

    In the real system, this would talk to an industrial controller
    (e.g. via CRI, TCP/IP or fieldbus). Here we just log moves.
    """

    async def move_to(self, position: str):
        logger.info("[ROBOT] Moving to position %s", position)
        # Simulate network / motion delay
        await asyncio.sleep(0.2)
        logger.info("[ROBOT] Reached position %s", position)
        return {"status": "ok", "position": position}


class GripperClient:
    """
    Simulated gripper client.

    In the real project this was controlled via OPC UA through
    an ICE3 gateway. Here we just log actions.
    """

    async def open(self):
        logger.info("[GRIPPER] Opening gripper")
        await asyncio.sleep(0.1)
        return {"status": "opened"}

    async def close(self):
        logger.info("[GRIPPER] Closing gripper")
        await asyncio.sleep(0.1)
        return {"status": "closed"}


class PlatePusherClient:
    """
    Simulated plate pusher, inspired by devices addressed over HTTP
    in the original project.
    """

    async def move_to_site(self, site_name: str):
        logger.info("[PUSHER] Moving plate to site %s", site_name)
        await asyncio.sleep(0.15)
        logger.info("[PUSHER] Plate movement to %s completed", site_name)
        return {"status": "ok", "site": site_name}

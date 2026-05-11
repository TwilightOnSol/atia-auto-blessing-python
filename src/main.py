"""Main entry point for Atia Shrine Automation."""

import sys
import schedule
import time

from .config import validate_keys
from .modules.atia import check_blessings
from .colors import RedColors

logo = r"""
   _____   __  .__            _____          __
  /  _  \_/  |_|__|____      /  _  \  __ ___/  |_  ____
 /  /_\  \   __\  \__  \    /  /_\  \|  |  \   __\/  _ \
/    |    \  | |  |/ __ \_ /    |    \  |  /|  | (  <_> )
\____|__  /__| |__(____  / \____|__  /____/ |__|  \____/
        \/             \/          \/

"""

def job():
    """Job wrapper for scheduled execution."""
    header = "Running 05:05 UTC jobs"
    print(f"\n{RedColors.RED}{header}{RedColors.RESET}")
    check_blessings()


def start() -> None:
    """Initialize and start the application."""

    validate_keys()

    # Schedule job at 05:05 UTC daily
    schedule.every().day.at("05:05").do(job)

    msg1 = "Scheduler started. Waiting for 05:05 UTC to run daily blessing..."
    msg2 = "Note: Times are in UTC. Adjust as needed for your timezone."
    print(f"{RedColors.RED}{logo}{RedColors.RESET}")
    print(f"{RedColors.RED}{msg1}{RedColors.RESET}")
    print(f"{RedColors.RED}{msg2}{RedColors.RESET}")

    # Keep the scheduler running
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    start()

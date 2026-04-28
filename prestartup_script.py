import os
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
COMFYUI_DIR = SCRIPT_DIR.parent.parent


def _copy_assets() -> None:
    src = SCRIPT_DIR / "assets"
    dst = COMFYUI_DIR / "input"
    if not src.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)


# Avoid importing comfy_env (and transitive torch imports) during prestartup.
# Set TRELLIS2_PRESTARTUP_SETUP_ENV=1 to restore the original behavior.
if os.getenv("TRELLIS2_PRESTARTUP_SETUP_ENV", "0") == "1":
    from comfy_env import setup_env  # type: ignore

    setup_env()

import json
from pathlib import Path

with open(Path(__file__).resolve().parent / "seccomp.json", "r") as f:
    data = json.load(f)

data["syscalls"][0]["names"].extend([
    "io_uring_setup", 
    "io_uring_register", 
    "io_uring_enter"
])

with open(Path(__file__).resolve().parent / "seccomp.json", "w") as f:
    json.dump(data, f)
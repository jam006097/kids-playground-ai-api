import sys

sys.path.append("./src")
from ai_api.main import iface

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0")

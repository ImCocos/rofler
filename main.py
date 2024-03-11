import os
from fastapi import FastAPI
import uvicorn


app = FastAPI()


update_cmd = """
rm ~/rofler
wget https://github.com/ImCocos/rofler/archive/refs/heads/main.zip -P ~/;
unzip ~/main.zip -d ~/;
rm ~/main.zip;
mv ~/rofler-main ~/rofler;
python -m venv ~/rofler/venv;
~/rofler/venv/bin/python -m pip install -r ~/rofler/requirements.txt;
mkdir ~/.config/autostart;
cp ~/rofler/rofler ~/.config/autostart/rofler;
# systemctl reboot;
""".strip()


@app.get("/update")
async def root() -> dict[str, str]:
    os.system(update_cmd)
    return {'status': 'ok'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9999)

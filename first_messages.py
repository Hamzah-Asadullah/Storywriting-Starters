from requests import post
from json import loads, dumps

LOG: bool = True
LINK: str = "http://localhost:5001/v1/chat/completions"
MESSAGES: int = 8192
SYSTEM_PROMPT: str = "You are a helpful assistant designed to generate first messages. You do not respond with anything but the direct solution to the user's query."
USER_PROMPT: str = "Generate the \"first-message\" for a storytelling RPG, which includes character description(s), realistic or fantasy environment, and an engaging situation. Do not list options or the main character's actions, what the main character says, or similar; only describe to give the user the freedom of action."

def log(text: str, mode: str='n'):
    if LOG:
        print(">> [", "NOTICE ]:" if mode=='n' else "UPDATE ]:", text, end='\r' if mode=='u' else '\n')

def get_payload(conversation: list[dict[str, str]]):
    payload: dict[str, list[dict[str, str]] | float] = { "messages": conversation, "temperature": 1.1, "top_p": 1, "min_p": 0, "top_k": 100, "presence_penalty": 0.1 }
    return payload

def get_message(conversation: list[dict[str, str]]) -> str:
    payload = get_payload(conversation)
    while True:
        try:
            response = post(LINK, json=payload, timeout=300)
            response.raise_for_status()
            next_msg: str = response.json()["choices"][0]["message"]["content"]
            return next_msg
        except Exception as e:
            log(f"Failed to receive next message. | {str(e)[:50]}")

def main():
    try:
        with open("first_messages.json", "r") as r:
            data = loads(r.read())
        log(f"Loaded {len(data)} messages, will continue.")
    except:
        data: list[str] = []
        log("Starting fresh.")

    conversation: list[dict[str, str]] = [
                { "role": "system", "content": SYSTEM_PROMPT },
                { "role": "user", "content": USER_PROMPT }
            ]
    for message_index in range(len(data), MESSAGES):
        msg: str = get_message(conversation)
        log(f"{round((message_index*100)/MESSAGES, 3)}% | {msg[:60]}")
        data.append(msg)

        with open("first_messages.json", "w") as w:
            w.write(dumps(data))

if __name__ == "__main__":
    main()
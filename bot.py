from dgg_chat import DGGChat

chat = DGGChat()

prefix = "!"
    
@chat.on_chat_message
def on_chat_message(message):
    if message.content.startswith(prefix):
        if message.content.split()[0] == prefix+"sr":#command
            url = message.content.split()[1]
            sr = open("sr.txt",'a', encoding="utf-8")
            if url.startswith("https://youtu"):
                sr.write(url+"\n")
                sr.close()
chat.run_forever()
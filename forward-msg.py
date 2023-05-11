from pyrogram import Client
from pyrogram import filters

api_id = "Your telegram api id"
api_hash = "Your telegram api hash"
app = Client("my_account")

# GET IDS FROM ALL CHANNELS
#async def main():
#    async with app:
#        async for dialog in app.get_dialogs():
#            print(str(dialog.chat.title) + " : " + str(dialog.chat.id))
#app.run(main())

# CHAT ID
SOURCE_CHAT = -1001411149960 
TARGET_CHAT = -1001691579886

while(True):
        
    try:
            
        #Forward the messages
        @app.on_message(filters.chat(SOURCE_CHAT))
        def my_handler(client, message):
            message.copy(  # copy() so there's no "forwarded from" header
                chat_id=TARGET_CHAT,  # the channel you want to post to
                #You can add caption to the message
                #caption="Copied from the VIP group by LUIS"  # Caption
            )

        app.run()
    except:
        print("Ocurrio un error")

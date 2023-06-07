from telethon import TelegramClient, events

api_id = 'API-ID'
api_hash = 'API-HASH'
entity = CHAT_ID

client = TelegramClient('bot_session', api_id, api_hash)


@client.on(events.NewMessage(outgoing = False) )
@client.on(events.Album)
async def handle_new_message(event):
    execute_handle_new_message = True
    if event.grouped_id:
        try:
            execute_handle_new_message = False
            sent_message = await event.forward_to(entity)
            reply_text = f'#album, #{event.chat_id}'
            await client.send_message(entity, reply_text, reply_to = sent_message[len(event)-1].id)
        except Exception as e:
            if event.media:
                media_type = None

                if hasattr(event.media, 'photo'):
                    media_type = 'photo'

                elif hasattr(event.media, 'document'):
                    media_type = 'document'

                reply_text = f'#{media_type}, #{event.chat_id}'
                sent_message = await client.forward_messages(entity, event.message)
            await client.send_message(entity, reply_text, reply_to = sent_message.id)




client.start()
client.run_until_disconnected()
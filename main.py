from telethon import TelegramClient, events
import config

client = TelegramClient('bot_session', config.api_id, config.api_hash)


@client.on(events.NewMessage(outgoing=False))
@client.on(events.Album)
async def handle_new_message(event):
    sender = await event.get_sender()
    user_id = sender.id
    if event.grouped_id:
        print('Got an album with', len(event), 'items')
        sent_message = await event.forward_to(config.entity)
        reply_text = f'TAG: #album\nUID: ```{user_id}```'
        await client.send_message(config.entity, reply_text, reply_to=sent_message[len(event)-1].id, parse_mode="Markdown")
    if event.media:
        media_type = None

        if hasattr(event.media, 'photo'):
            media_type = 'photo'

        elif hasattr(event.media, 'document'):
            media_type = 'document'

        reply_text = f'TAG: #{media_type}\nUID: ```{user_id}```'
        sent_message = await client.forward_messages(config.entity, event.message)
        await client.send_message(config.entity, reply_text, reply_to=sent_message.id, parse_mode="Markdown")

client.start()
client.run_until_disconnected()

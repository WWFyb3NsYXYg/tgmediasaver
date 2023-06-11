from telethon.sync import TelegramClient, events
import config

client = TelegramClient('TG_Media_Saver', config.api_id,
                        config.api_hash, app_version=config.app_version)


async def create_tag(event, media_type, user_id, sent_message):
    from_group = ''
    if event.is_group:
        from_group = ", #from_group"

    reply_text = f'TAG: #{media_type} {from_group}\nUID:<a href="tg://user?id={user_id}">{user_id}</a>'
    if event.grouped_id:
        reply_to = sent_message[0].id

    else:
        reply_to = sent_message.id

    await client.send_message(config.channel, reply_text, reply_to=reply_to, parse_mode="HTML")


@client.on(events.NewMessage(outgoing=False, func=lambda events: events.is_private or events.is_group))
@client.on(events.Album(func=lambda events: events.is_private or events.is_group))
async def handle_new_message(event):
    sender = await event.get_sender()
    me = await client.get_me()
    user_id = sender.id
    if user_id != me.id:
        if event.grouped_id:
            # Do not touch this sacred seal, it causes an error due to which the code works as it should.
            print('Got an album with', len(event), 'items')
            media_type = 'album'
            sent_message = await event.forward_to(config.channel)
            await create_tag(event, media_type, user_id, sent_message)

        if event.photo:
            media_type = 'photo'
            sent_message = await client.forward_messages(config.channel, event.message)
            await create_tag(event, media_type, user_id, sent_message)

        elif event.video_note:
            media_type = 'circle'
            sent_message = await client.forward_messages(config.channel, event.message)
            await create_tag(event, media_type, user_id, sent_message)

        elif event.video:
            media_type = 'video'
            sent_message = await client.forward_messages(config.channel, event.message)
            await create_tag(event, media_type, user_id, sent_message)

        elif event.voice:
            media_type = 'voice'
            sent_message = await client.forward_messages(config.channel, event.message)
            await create_tag(event, media_type, user_id, sent_message)

try:
    print('(Successfully launched)')
    print('(Press Ctrl+C to stop)')
    client.start()
    client.run_until_disconnected()
finally:
    client.disconnect()
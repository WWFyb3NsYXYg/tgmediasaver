# tgmediasaver

**tgmediasaver** is a Python script for a Telegram media saver bot. It utilizes the Telethon library to save media files shared in Telegram groups and albums.

## Features

- Automatically saves photos and documents shared in groups and albums.
- Extracts relevant information from the media, such as media type and user ID.
- For albums, forwards the entire album to a specified entity (channel or chat) and adds a tag with the album type and user ID.
- For individual media files, forwards them to a specified entity and adds a tag with the media type and user ID.

## Usage

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Set up your Telegram API credentials in the `config.py` file.
3. Specify the target entity (channel or chat) where you want to forward the media and add tags in the `config.py` file.
4. Run the script using `python main.py`.
5. The bot will start listening to new messages in groups and albums, automatically saving and forwarding the media.

> Note: Make sure to obtain the necessary API credentials from the Telegram API website before running the script.

## License

This project is licensed under the [MIT License](LICENSE).

Please note that this script should be used responsibly and in compliance with the Telegram Terms of Service.

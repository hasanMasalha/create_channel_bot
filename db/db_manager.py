import json
import os
def save_channel_link(channel_id, link, user_id, filename='channels.json'):
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)
    print(filepath)
    channel_data = {
        channel_id: {
            "link": link,
            "user_id": user_id
        }
    }
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print(f"Warning: {filename} is not a valid JSON file. Starting with an empty file.")
            data = {}
    else:
        data = {}
    data.update(channel_data)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

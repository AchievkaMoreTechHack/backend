from core.config import API_URL


def create_url_story(story_id):
    return story_id
    # if not story_id:
    #     return None
    # if API_URL[-1] == "/":
    #     return API_URL + f"story/{story_id}"
    # return API_URL + f"/story/{story_id}"


def create_url_media(media_id):
    if not media_id:
        return None
    if API_URL[-1] == "/":
        return API_URL + f"media/{media_id}"
    return API_URL + f"/media/{media_id}"

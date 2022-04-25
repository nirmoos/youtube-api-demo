                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #!/usr/bin/python
import argparse
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tabulate import tabulate

load_dotenv()

DEVELOPER_KEY = os.environ["GCP_DEVELOPER_API_KEY"]
SERVICE_NAME = "youtube"
API_VERSION = "v3"
YOUTUBE_VIDEO_TEMPLATE_URL = "https://www.youtube.com/watch?v=%s"


def youtube_search(options):
    youtube = build(SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results,
        type="video",
        fields="items(id,snippet(title))"
    ).execute()

    videos = [
        {
            "id": res["id"]["videoId"],
            "title": res["snippet"]["title"],
            "url": YOUTUBE_VIDEO_TEMPLATE_URL % res["id"]["videoId"]
        }
        for res in search_response.get("items", [])
    ]

    print("\n\033[95mMost trending youtube videos are:\033[96m\n")
    print(tabulate([(v["id"], v["title"], v["url"]) for v in videos], headers=["ID", "Title", "URL"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", help="Search term", required=True)
    parser.add_argument("--max-results", help="Max results", default=10)
    args = parser.parse_args()

    try:
        youtube_search(args)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))

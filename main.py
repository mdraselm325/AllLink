import os
from flask import Flask, jsonify, request
import yt_dlp

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome To Team Calyx All Downloader Api'

@app.route('/alldl', methods=['GET'])
def allLink():
    print("\n<=====> allLink response <=====>\n")
    ulink = request.args.get('link')
    if not ulink:
        return jsonify({"error": "No link provided"}), 400

    # Define a function to capture the download URL
    def get_video_info(url):
        ydl_opts = {
            'format': 'best',  # choose the best quality
            'quiet': True,
            'noplaylist': True,
            'skip_download': True,  # don't download, just get info
            'cookiefile': 'cookies.txt'  # path to your cookies file
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info['url']  # returns direct download URL

    try:
        # Fetch download link using yt-dlp
        download_url = get_video_info(ulink)
        print(download_url)
        print("\n<=====> allLink finish <=====>\n")
        return jsonify({"download_url": download_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug = True)
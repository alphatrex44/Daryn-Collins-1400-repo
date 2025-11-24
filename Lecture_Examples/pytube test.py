import yt_dlp
import shutil
import os


import yt_dlp
import shutil
import os

def download_video(url_or_id, output_path=None):
    if output_path is None:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(repo_root, "video_files")

    os.makedirs(output_path, exist_ok=True)

    if not url_or_id.startswith("http"):
        url = f"https://www.youtube.com/watch?v={url_or_id}"
    else:
        url = url_or_id

    # Build absolute path to node.exe in the same folder
    repo_root = os.path.dirname(os.path.abspath(__file__))
    node_path = os.path.join(repo_root, "node.exe")

    # yt-dlp options
    ydl_opts = {
        "outtmpl": f"{output_path}/%(title)s by %(uploader)s.%(ext)s",
        "exec": f'"{node_path}"'  # force yt-dlp to use local node.exe
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download complete: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")



def main():
    # Ask if user wants the sample download
    print("btw you'll need to open the files with vlc for consistent sound as opus isnt supported by the default mediap layer")
    choice = input("Do you want to download the sample video (Rickroll)? [y/n]: ").strip().lower()
    if choice == "y":
        print("Downloading sample video (Rickroll)...")
        download_video("dQw4w9WgXcQ")
    else:
        print("Skipping sample download.")

    # Loop for user input
    while True:
        user_input = input("\nEnter a YouTube URL or video ID (or 'quit' to exit): ").strip()
        if user_input.lower() == "quit":
            print("Exiting program.")
            break
        elif user_input:
            print("Downloading your video...")
            download_video(user_input)
        else:
            print("No input provided. Try again.")


if __name__ == "__main__":
    main()

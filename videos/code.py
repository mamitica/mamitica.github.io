from youtube_transcript_api import YouTubeTranscriptApi

def fetch_video_transcript(video_url):
    # Extracting Video ID from URL
    if "youtu.be" in video_url:
        video_id = video_url.split('/')[-1]
    else:
        video_id = video_url.split('v=')[-1].split('&')[0]

    # Attempt to fetch the video transcript in Spanish
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'es-419', 'es-MX', 'es-ES'])
        full_transcript = '\\n'.join([item['text'] for item in transcript_list])
        return full_transcript
    except Exception as e:
        return f"Failed to fetch transcript: {str(e)}"

# Main block to set the 'result' variable, as expected by the platform
video_url = "{{1.text}}"
result = fetch_video_transcript(video_url)


from youtube_transcript_api import YouTubeTranscriptApi

def fetch_video_transcript(video_url):
    # Extracting Video ID from URL
    if "youtu.be" in video_url:
        video_id = video_url.split('/')[-1]
    else:
        video_id = video_url.split('v=')[-1].split('&')[0]

    # Attempt to fetch the video transcript in Spanish
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'es-419', 'es-MX', 'es-ES'])
        full_transcript = '\\n'.join([item['text'] for item in transcript_list])
        return full_transcript
    except Exception as e:
        return f"Failed to fetch transcript: {str(e)}"

# Main block to set the 'result' variable, as expected by the platform
video_url = "{{1.text}}"
result = fetch_video_transcript(video_url)
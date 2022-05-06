from youtube_transcript_api import YouTubeTranscriptApi
import sys

def get_transcript(video_id):
  transcription = YouTubeTranscriptApi.get_transcript(video_id)
  with open('transcription.md', 'w') as f:
    for i in transcription:
      f.write(f"{i['text']}\n")

if __name__ == '__main__':
   get_transcript(sys.argv[1])

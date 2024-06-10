from color import Color
import docx
import os


transcripts = {}
radius = 75


print("Loading transcripts...")

for file in os.listdir("./transcripts"):
    if os.path.splitext(file)[1] == ".docx":
        transcriptSeason = int(file[0])
        transcriptEpisode = int(file[1:3])
        if transcriptSeason not in transcripts:
            transcripts[transcriptSeason] = {}

        transcriptDoc = docx.Document("./transcripts/" + file)
        transcript = "\n".join([paragraph.text for paragraph in transcriptDoc.paragraphs])
        transcripts[transcriptSeason][transcriptEpisode] = transcript


def find_phrase(text, phrase):
    location = text.lower().find(phrase.lower())
    if location < 0:
        return
    start = max(0, location - radius)
    end = min(location + radius, len(text))
    print(f"{Color.UNDERLINE}Season {season} Episode {episode}{Color.END}\n" +
          f"{text[start:location]}{Color.YELLOW}{text[location:location+len(phrase)]}{Color.END}{text[location+len(phrase):end]}\n")


while len((search_phrase := input("Enter phrase: "))) > 0:
    print()
    for season in transcripts:
        for episode in transcripts[season]:
            find_phrase(transcripts[season][episode], search_phrase)

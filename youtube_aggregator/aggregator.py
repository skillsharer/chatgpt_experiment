import datetime
import openai
import argparse
from youtube_transcript_api import YouTubeTranscriptApi


def chunk_string(string, chunk_size):
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]


def chunk_words(string, chunk_size):
    words = string.split()
    chunks = []
    chunk = ""
    for word in words:
        if len(chunk) + len(word) + 1 > chunk_size:
            chunks.append(chunk)
            chunk = ""
        if chunk:
            chunk += " "
        chunk += word
    chunks.append(chunk.strip("\n"))
    return chunks


def summarize(video_id, shorten, output_txt):
    srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    if len(srt) == 0:
        raise ValueError("Sorry, I cannot retrieve text from the video.")

    all_text = []
    for element in srt:
        all_text.append(element["text"])

    all_text = ' '.join(all_text)
    chunks = chunk_words(all_text, 4097)

    # Set up the OpenAI API client
    with open("../.env", "r") as envfile:
        my_api_key = envfile.readlines()

    openai.api_key = my_api_key[0].strip("\n")
    model_engine = "text-davinci-003"
    prompt = "Please summarize the following text: "
    responses = []

    for chunk in chunks:
        chunk = prompt + chunk
        try:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=chunk,
                max_tokens=200,
                n=1,
                stop=None,
                temperature=0.1,
            )

            response = completion.choices[0].text
        except Exception as e:
            print(datetime.datetime.now(), "OpenAI API does not response. ERROR: ", e)
            response = ""
        responses.append(response.replace('\n', ''))

    response = ' '.join(responses)

    if shorten:
        final_input = prompt + response
        try:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=final_input,
                max_tokens=500,
                n=1,
                stop=None,
                temperature=0.1,
            )
            response = completion.choices[0].text
        except Exception as e:
            print(datetime.datetime.now(), "OpenAI API does not response. ERROR: ", e)



    if output_txt:
        with open(output_txt, "w") as txtfile:
            txtfile.write(response)
        print(datetime.datetime.now(), "Output written to: ", output_txt)

    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True, help="The YouTube URL which you want to summarize.")
    parser.add_argument("--shorten", type=bool, default=True, help="Shorten the summary of the video")
    parser.add_argument("--output", type=str, default=None, help="Write the result to txt.")
    args = parser.parse_args()

    video_id = args.url.split("v=")[-1]
    shorten = args.shorten
    txt_file = args.output
    response = summarize(video_id, shorten, txt_file)
    print(response)

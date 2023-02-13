# YOUTUBE Aggregator

## About

This code summarizes the transcript of a YouTube video given its URL. It uses the youtube_transcript_api and openai packages to accomplish this. The code chunkifies the transcript text into smaller pieces to overcome API request limitations, and then uses the OpenAI API to summarize each chunk and finally concatenates the chunks back into a full summary. The shorten argument can be used to further shorten the final summary. The summary can also be written to a text file if the output argument is provided. The code is executed with command line arguments that include the YouTube video URL, the option to shorten the summary, and the option to output the summary to a text file.

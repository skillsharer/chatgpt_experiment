# YOUTUBE Aggregator

## About

This code summarizes the transcript of a YouTube video given its URL. It uses the youtube_transcript_api and openai packages to accomplish this. The code chunkifies the transcript text into smaller pieces to overcome API request limitations, and then uses the OpenAI API to summarize each chunk and finally concatenates the chunks back into a full summary. The shorten argument can be used to further shorten the final summary. The summary can also be written to a text file if the output argument is provided. The code is executed with command line arguments that include the YouTube video URL, the option to shorten the summary, and the option to output the summary to a text file.

## Setup

### Getting API key

To get an API key for OpenAI, you need to sign up for an account on the OpenAI website. Once you have created an account, you can access your API key from the OpenAI Dashboard. Simply log in to the dashboard and click on the "API" button. This will display your API key, which you can then use to make API calls in your applications.

It is important to keep your API key secure and not to share it publicly. You should also monitor your usage and be mindful of the number of API calls you make and the amount of data you use. Some OpenAI services may have usage limits or charges associated with them, so be sure to familiarize yourself with the relevant terms of service and pricing information.

If you have the API key, then simply store it in an .env file in the script directory.

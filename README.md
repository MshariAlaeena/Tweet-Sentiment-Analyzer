# Sentiment Analysis of Twitter Data

This Python project performs a basic sentiment analysis on a dataset of tweets. It evaluates each tweet's sentiment as positive, negative, or neutral based on the presence of positive or negative words. The analysis outputs a CSV file summarizing the sentiment scores alongside the number of retweets and replies for each tweet.

## Project Structure

The project is structured as follows:
- `positive_words.txt`: A text file containing a list of words considered to have a positive sentiment.
- `negative_words.txt`: A text file containing a list of words considered to have a negative sentiment.
- `project_twitter_data.txt`: The dataset of tweets to analyze. Each tweet is expected to be accompanied by its retweet and reply counts.
- `sentiment_analysis.py`: The main Python script that performs the sentiment analysis.

## Getting Started

To run this project, ensure you have Python installed on your system. The project does not require any external libraries beyond the Python Standard Library.

### Prerequisites

- Python 3.x

### Running the Script

1. Place the `positive_words.txt`, `negative_words.txt`, and `project_twitter_data.txt` files in the `Scripts\Externals` directory relative to the script.
2. Run the script from the command line or your preferred IDE:

3. The script will generate a file named `resulting_data.csv` in the project's root directory. This file contains the analysis results, including the number of retweets, replies, positive score, negative score, and net sentiment score for each tweet.

## Output

The output CSV file will have the following columns:
- Number of Retweets
- Number of Replies
- Positive Score
- Negative Score
- Net Score

## Customization

You can customize the list of positive or negative words by editing the `positive_words.txt` and `negative_words.txt` files. Adding or removing words from these files will directly affect the sentiment analysis results.

## License

This project is open source and available under the [MIT License](LICENSE.md).

## Acknowledgments

- Thanks to anyone who contributed to the collection of positive and negative words.

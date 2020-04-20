import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
import nltk
import csv
import re
from nltk.corpus import stopwords
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

stop_words = stopwords.words('english')
reddit = praw.Reddit(client_id='RIzXE97ti1Md4A',
                     client_secret='FcT6Zhqefc29yg48VcP-JTm-5z4',
                     user_agent='Reddit Web Scrapper API',
                     username='HadesGeneral',
                     password='Winnie12')


def initialize_program():
    """
    Starts the program, asks for subreddit names, and gives back 1 post from each
    to make sure it is the subreddit you are looking for.
    :return: subreddit_one, subreddit_two
    """
    global subreddit_one, subreddit_two
    sub_one = "nosleep" # input("What is your first subreddit?")    # User input for first subreddit
    subreddit_one = reddit.subreddit(sub_one)   # variable to manipulate first subreddit

    print("")   # visually separate Questions

    sub_two = "libraryofshadows" # input("What is your second subreddit?")   # User input for second subreddit
    subreddit_two = reddit.subreddit(sub_two)   # variable to manipulate first subreddit

    return subreddit_one, subreddit_two


def save_score(x_one, x_two):
    """
    saves the title of the first thousand post's score of the each subreddit sorted by top for manipulation
    : return:
    """
    top_one = x_one.top(limit=1000)
    sub_one_dict_score = {"score": []}

    for submission in top_one:
        sub_one_dict_score['score'].append(submission.score)

    df_one = pd.DataFrame(sub_one_dict_score)
    df_one.to_csv('score_one.csv')

    # ---------------------------------------------------------

    top_two = x_two.top(limit=1000)
    sub_two_dict_score = {"score": []}

    for submission in top_two:
        sub_two_dict_score['score'].append(submission.score)

    df_two = pd.DataFrame(sub_two_dict_score)
    df_two.to_csv('score_two.csv')


def save_title(x_one, x_two):
    """
    saves the title of the first thousand post's title of each subreddit sorted by top for manipulation
    : return:
    """
    top_one = x_one.top(limit=1000)
    sub_one_dict_title = {"title": []}

    for submission in top_one:
        sub_one_dict_title['title'].append(submission.title)

    df = pd.DataFrame(sub_one_dict_title)
    df.to_csv('title_one.csv')

    # ---------------------------------------------------------

    top_two = x_two.top(limit=1000)
    sub_two_dict_title = {"title": []}

    for submission in top_two:
        sub_two_dict_title['title'].append(submission.title)

    df = pd.DataFrame(sub_two_dict_title)
    df.to_csv('title_two.csv')


def save_author(x_one, x_two):
    """
    saves the authors of the first thousand post's authors of each subreddit sorted by top for manipulation
    : return:
    """
    top_one = x_one.top(limit=1000)
    sub_one_dict_author = {"author": []}

    for submission in top_one:
        sub_one_dict_author['author'].append(submission.author)

    df = pd.DataFrame(sub_one_dict_author)
    df.to_csv('author_one.csv')

    # ---------------------------------------------------------

    top_two = x_two.top(limit=1000)
    sub_two_dict_author = {"author": []}

    for submission in top_two:
        sub_two_dict_author['author'].append(submission.author)

    df = pd.DataFrame(sub_two_dict_author)
    df.to_csv('author_two.csv')


def save_body(x_one, x_two):
    """
    saves the body of the first thousand post body's of each subreddit sorted by top for manipulation
    : return:
    """
    top_one = x_one.top(limit=1000)
    sub_one_dict_body = {"body": []}

    for submission in top_one:
        sub_one_dict_body['body'].append(submission.selftext)

    df = pd.DataFrame(sub_one_dict_body)
    df.to_csv('body_one.csv')

    # ----------------------------------------------------------

    top_two = x_two.top(limit=1000)
    sub_two_dict_body = {"body": []}

    for submission in top_two:
        sub_two_dict_body['body'].append(submission.selftext)

    df = pd.DataFrame(sub_two_dict_body)
    df.to_csv('body_two.csv')


def save_all(x_one, x_two):
    """
    Run through Top submissions of the each subreddit while collecting
    the title, body, and author of post
    :return:
    """
    one_all = x_one.top(limit=1000)
    one_dict_all_info = {
            "title": [],
            "body": [],
            "redditor": [],
            "score": []}

    for submission in one_all:
        one_dict_all_info["title"].append(submission.title)
        one_dict_all_info['redditor'].append(submission.author)
        one_dict_all_info['body'].append(submission.selftext)
        one_dict_all_info['score'].append(submission.score)

    df = pd.DataFrame(one_dict_all_info)
    df.to_csv('one_all_info.csv')

    # -------------------------------------------------------------

    two_all = x_two.top(limit=1000)
    two_dict_all_info = {
            "title": [],
            "body": [],
            "redditor": [],
            "score": []}

    for submission in two_all:
        two_dict_all_info["title"].append(submission.title)
        two_dict_all_info['redditor'].append(submission.author)
        two_dict_all_info['body'].append(submission.selftext)
        two_dict_all_info['score'].append(submission.score)

    df = pd.DataFrame(two_dict_all_info)
    df.to_csv('two_all_info.csv')


def character_frequency_title():
    """
    Runs through the titles of the posts from each subreddit and counts each character
    :return: words_one
    """

    title_data_one = pd.read_csv(r"C:\Users\brian\PycharmProjects\coxb_Project_2\title_one.csv")
    dictionary_one = {}

    for submission_text in title_data_one["title"]:
        submission_text = str(submission_text)
        for character in submission_text.split(" " or '\n') and submission_text.replace('\n', ''):
            if character not in stop_words:
                dictionary_one[character] = dictionary_one.get(character, 0)+1

    character_one = list(dictionary_one.items())
    character_one.sort(key=lambda x: x[1])
    character_one.reverse()
    print(character_one)

    # --------------------------------------------------------------------------------------------------------

    title_data_two = pd.read_csv(r"C:\Users\brian\PycharmProjects\coxb_Project_2\title_two.csv")
    dictionary_two = {}

    for submission_text in title_data_two["title"]:
        submission_text = str(submission_text)
        for character in submission_text.split(" " or '\n') and submission_text.replace('\n', ''):
            if character not in stop_words:
                dictionary_two[character] = dictionary_two.get(character, 0)+1

    character_two = list(dictionary_two.items())
    character_two.sort(key=lambda x: x[1])
    character_two.reverse()
    print(character_two)


def word_frequency_body():
    """
    Runs through the bodies of the posts from each subreddit and counts how many each word is used, while taking out
    stopwords
    :return: words_one
    """

    body_data_one = pd.read_csv(r"C:\Users\brian\PycharmProjects\coxb_Project_2\body_one.csv")

    body_data_one.replace(to_replace=['\n', ".", ',', '', '-'], value=" ")

    dictionary_one = {}

    for submission_text in body_data_one["body"]:
        submission_text = str(submission_text)
        for word in submission_text.split(" " or '\n'):
            if word not in stop_words:
                dictionary_one[word] = dictionary_one.get(word, 0)+1

    words_one = list(dictionary_one.items())
    words_one.sort(key=lambda x: x[1])
    words_one.reverse()
    print(words_one)
    print("")

    # -------------------------------------------------------------------------------------------------

    body_data_two = pd.read_csv(r"C:\Users\brian\PycharmProjects\coxb_Project_2\body_two.csv")

    body_data_two.replace(to_replace=['\n', ".", ',', '', '-'], value=" ")

    dictionary_two = {}

    for submission_text in body_data_two["body"]:
        submission_text = str(submission_text)
        for word in submission_text.split(" " or '\n'):
            if word not in stop_words:
                dictionary_two[word] = dictionary_two.get(word, 0)+1

    words_two = list(dictionary_two.items())
    words_two.sort(key=lambda x: x[1])
    words_two.reverse()
    print(words_two)


def word_frequency_title_one():
    """
    Runs through the titles of the posts from the first subreddit and counts how many each word is used, while taking out
    stopwords
    :return: words_one, words_two
    """

    body_data_one = pd.read_csv(r"C:\Users\brian\PycharmProjects\coxb_Project_2\title_one.csv")

    body_data_one.replace(to_replace=['\n', ".", ',', '', '-'], value=" ")

    dictionary_one = {}

    for submission_text in body_data_one["title"]:
        submission_text = str(submission_text)
        for word in submission_text.split(" " or '\n'):
            if word not in stop_words:
                dictionary_one[word] = dictionary_one.get(word, 0)+1

    words_one = list(dictionary_one.items())
    words_one.sort(key=lambda x: x[1])
    words_one.reverse()
    print(words_one)
    print("")

    return words_one


def word_frequency_title_two():
    """
    Runs through the titles of the posts from the second subreddit and counts how many each word is used, while taking out
    stopwords
    :return:  words_two
    """

    body_data_two = pd.read_csv(r"C:\Users\brian\PycharmProjects\coxb_Project_2\title_two.csv")

    body_data_two.replace(to_replace=['\n', ".", ',', '', '-'], value=" ")

    dictionary_two = {}

    for submission_text in body_data_two["title"]:
        submission_text = str(submission_text)
        for word in submission_text.split(" " or '\n'):
            if word not in stop_words:
                dictionary_two[word] = dictionary_two.get(word, 0)+1

    words_two = list(dictionary_two.items())
    words_two.sort(key=lambda x: x[1])
    words_two.reverse()
    print(words_two)

    return words_two


def graph_title():
    """
    Takes the dictionaries made from the titles and makes a bar graph showing visually the number of times each word is
    used between each sub reddit.
    :return:
    """

    word_freq_one = word_frequency_title_one()
    words = []
    freq = []
    for words_in_title in word_freq_one:
        words.append(words_in_title[0])
    for freq_of_word in word_freq_one:
        freq.append(freq_of_word[1])
    print(freq)
    print(words)
    plt.figure(0)
    plt.xlabel("words")  # Label the X axis
    plt.ylabel("Score")  # Label the Y axis
    plt.title("frequency of words")  # Set the plot’s title
    # sample_data["score"] is a list of scores
    plt.scatter(words[:10], freq[:10])
    plt.show()

    # ---------------------------------------------------------------------------------------------

    word_freq_two = word_frequency_title_two()
    words = []
    freq = []
    for words_in_title in word_freq_two:
        words.append(words_in_title[0])
    for freq_of_word in word_freq_two:
        freq.append(freq_of_word[1])
    print(freq)
    print(words)
    plt.figure(0)
    plt.xlabel("words")  # Label the X axis
    plt.ylabel("Score")  # Label the Y axis
    plt.title("frequency of words")  # Set the plot’s title
    # sample_data["score"] is a list of scores
    plt.scatter(words[:10], freq[:10])
    plt.show()


def main():
    initialize_program()
    # save_score(x_one=subreddit_one, x_two=subreddit_two)
    # save_title(x_one=subreddit_one, x_two=subreddit_two)
    # save_author(x_one=subreddit_one, x_two=subreddit_two)
    # save_body(x_one=subreddit_one, x_two=subreddit_two)
    # save_all(x_one=subreddit_one, x_two=subreddit_two)
    # character_frequency_title()
    # word_frequency_body()
    # word_frequency_title_one()
    graph_title()


if __name__ == '__main__':
    main()

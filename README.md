# CSC-386-project-2


Topic:
	The idea of this project is to make a program to allow anyone to input two subreddits and get general info, then to
	be analyzed further by another program.
___
Libraries:

	Praw

	Pandas

	Date and time
___
Functions :
    Initialize_program -- make sure stopwords are up to date and connecting to the subreddits specified by the user
    Save_titles -- Save Titles to their own file
    Save_bodies -- Save bodies to their own file
    Save_authors -- Save authors to their own file
    Save_scores -- Save scores to their own file
    Save_times -- Save the time of posts in their own file
    Save_al1 -- Save all four together in a separate file than the previous three.


___
Data structures:

	Dictionaries:  to hold the post and the values from what we scrape
	PD: used to give a little more structure to dictionaries to be able to analyze
	String: used when looking at the body or title to analyze the post
	List: used to show the post name with the coordinating values in order and ability to sort
    them
___
Corpus:

	I will focus on nosleep and libraryofshadows subreddits, but the program allows for two of any other subreddits.
___
End-use:

	See differences between two similar subreddits made around the same time, but have very different follower base.


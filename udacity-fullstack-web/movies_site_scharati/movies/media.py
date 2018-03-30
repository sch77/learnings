import webbrowser

"""This module provides storage for Movie information and ways to use the
   information
"""


class Movie():
    """ A place to store movie related information
    Attributes:
    VALID_RATINGS : Valid ratings for a Movie
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Inits Movie with title,storyline,poster_image and youtube_trailer
           information.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ opens the youtube_trailer url in webbrowser """
        webbrowser.open(self.trailer_youtube_url)

import media
import fresh_tomatoes

""" This module serves as a landing page for selected movies"""


# constructing movies
toy_story = media.Movie("Toy Story", "A boy and his toys that come to life",
                        "https://bit.ly/2pIGQT0",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

u_turn = media.Movie("U Turn",
                     "A story about what happens when people take a specific \
                     UTurn", "https://bit.ly/2DZ8aRp",
                     "https://www.youtube.com/watch?v=Kdh5P8dtMXA")

udaan = media.Movie("Udaan", "The story of a boy escaping abuse and chasing \
                     his dreams", "https://bit.ly/2GgwShL",
                    "https://www.youtube.com/watch?v=wEJxe2bE-cE")

cowspiracy = media.Movie("Cowspiracy", "How Meat consumption is harming the \
                          planet", "https://bit.ly/2IYY2M3",
                         "https://www.youtube.com/watch?v=nV04zyfLyN4")

into_the_wild = media.Movie("Into the wild", "A person's rejection of the \
                             material world", "https://bit.ly/2I8RKIu",
                            "https://www.youtube.com/watch?v=g7ArZ7VD-QQ")

ondu_motteya_kathe = media.Movie("Ondu motteya kathe", "Story of a bald person \
                                  and his struggles to get married",
                                 "https://bit.ly/2GDZh4O",
                                 "https://www.youtube.com/watch?v=UXv-9QdR3s8")

# populating the set of movies to show on the landing page
movies = [toy_story, udaan, u_turn, cowspiracy, into_the_wild,
          ondu_motteya_kathe]

# populate the landing page and open
fresh_tomatoes.open_movies_page(movies)

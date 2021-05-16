from behave import given, when, then
from behave.runner import Context


@given("person open IMDb website")
def step_impl(context: Context) -> None:
    context.imdb.open_page()


@when("person enter the movie {name} in the search bar")
def step_impl(context: Context, name: str) -> None:
    context.imdb.search(name)


@then("search results are shown and {movie} is presented")
def step_impl(context: Context, movie: str) -> None:
    movies = context.imdb.get_movies()
    assert movie in movies


@then("person open {movie} page and see the {title}")
def step_impl(context: Context, movie: str, title: str) -> None:
    context.imdb.open_movie_page(movie)
    page_title = context.imdb.get_page_title()
    assert f"{title} - IMDb" == page_title


@then("one of the directors is {director}")
def step_impl(context: Context, director: str) -> None:
    directors = context.imdb.get_movie_directors()
    assert director in directors


@then("rating is between 0 and 10")
def step_impl(context: Context) -> None:
    rating = context.imdb.get_movie_rating()
    assert rating >= 0 and rating <= 10

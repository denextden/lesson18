from unittest.mock import MagicMock

import pytest

from project.main_dir.dao.movie import MovieDAO
from project.main_dir.service.movie import MovieService


@pytest.fixture
def movie_dao():
    dao = MovieDAO(None)

    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.delete = MagicMock()
    dao.update = MagicMock()
    return dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movies_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    parameters = ((1, {'id': 1}), (2, {'id': 2}))

    @pytest.mark.parametrize('ind, mid', parameters)
    def test_get_one(self, ind, mid):
        self.movie_service.dao.get_one.return_value = mid
        assert self.movie_service.get_one(ind) == mid, "Bad"

    parameters = (([1, {'id': 1}, 2, {'id': 2}]))

    @pytest.mark.parametrize('movies', parameters)
    def test_get_all(self, movies):
        self.movie_service.dao.get_all.return_value = movies
        assert self.movie_service.get_all() == movies

    parameters = (
        (1, {'id': 1}, 2, {'id': 2}))

    @pytest.mark.parametrize('movie', parameters)
    def test_create(self, movie):
        self.movie_service.dao.create.return_value = movie
        assert self.movie_service.create(movie) == movie

    parameters = (
        (
            {
                'id': 1,
                'title': 'no'
            },
            {
                'id': 1,
                'title': 'yes'
            }
        )
    )

    @pytest.mark.parametrize('movie_orig, movie_new', parameters)
    def test_update(self, movie_orig, movie_new):
        self.movie_service.dao.update.return_value = movie_new
        assert self.movie_service.update(movie_new) == movie_new


    def test_delete(self):
        self.movie_service.delete(1)
        self.movie_service.dao.delete.assert_called_once_with(1)


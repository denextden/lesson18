from unittest.mock import MagicMock

import pytest

from project.main_dir.dao.genre import GenreDAO
from project.main_dir.service.genre import GenreService


@pytest.fixture
def genre_dao():
    dao = GenreDAO(None)

    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.delete = MagicMock()
    dao.update = MagicMock()
    return dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    parameters = ((1, {'id': 1}), (2, {'id': 2}))

    @pytest.mark.parametrize('ind, gid', parameters)
    def test_get_one(self, ind, gid):
        self.genre_service.dao.get_one.return_value = gid
        assert gid != None
        assert self.genre_service.get_one(ind) == gid, "Bad"

    parameters = (([1, {'id': 1}, 2, {'id': 2}]))

    @pytest.mark.parametrize('genres', parameters)
    def test_get_all(self, genres):
        self.genre_service.dao.get_all.return_value = genres
        assert self.genre_service.get_all() == genres

    parameters = (
        (1, {'id': 1}, 2, {'id': 2}))

    @pytest.mark.parametrize('genre', parameters)
    def test_create(self, genre):
        self.genre_service.dao.create.return_value = genre
        assert self.genre_service.create(genre) == genre

    parameters = (
        (
            {
                'id': 1,
                'genre': 'comedy'
            },
            {
                'id': 1,
                'genre': 'horror'
            }
        )
    )

    @pytest.mark.parametrize('genre_orig, genre_new', parameters)
    def test_update(self, genre_orig, genre_new):
        self.genre_service.dao.update.return_value = genre_new
        assert self.genre_service.update(genre_new) == genre_new


    def test_delete(self):
        self.genre_service.delete(1)
        self.genre_service.dao.delete.assert_called_once_with(1)


from unittest.mock import MagicMock

import pytest

from project.main_dir.dao.director import DirectorDAO
from project.main_dir.service.director import DirectorService


@pytest.fixture
def director_dao():
    dao = DirectorDAO(None)

    dao.get_one = MagicMock(return_value={'id': 1})
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.delete = MagicMock()
    dao.update = MagicMock()
    return dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    parameters = ((1, {'id': 1}), (2, {'id': 2}))

    @pytest.mark.parametrize('ind, did', parameters)
    def test_get_one(self, ind, did):
        director = self.director_service.get_one(did)
        assert director != None
        assert director == did

    parameters = (([1, {'id': 1}, 2, {'id': 2}]))

    @pytest.mark.parametrize('directors', parameters)
    def test_get_all(self, directors):
        self.director_service.dao.get_all.return_value = directors
        assert self.director_service.get_all() == directors

    parameters = (
        (1, {'id': 1}, 2, {'id': 2}))

    @pytest.mark.parametrize('director', parameters)
    def test_create(self, director):
        self.director_service.dao.create.return_value = director
        assert self.director_service.create(director) == director

    parameters = (
        (
            {
                'id': 1,
                'name': 'Max'
            },
            {
                'id': 1,
                'name': 'Marry'
            }
        )
    )

    @pytest.mark.parametrize('director_orig, director_new', parameters)
    def test_update(self, director_orig, director_new):
        self.director_service.dao.update.return_value = director_new
        assert self.director_service.update(director_new) == director_new


    def test_delete(self):
        self.director_service.delete(1)
        self.director_service.dao.delete.assert_called_once_with(1)


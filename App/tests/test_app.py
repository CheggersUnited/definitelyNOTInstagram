import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
    get_user,
    get_user_by_username,
    update_user
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bob", "bobpass")
        assert user.username == "bob"

    def test_toDict(self):
        """
        
        id': self.id,
            'username': self.username,
            'email': self.email,
            'tier': self.tier,
            'limit': self.limit,
            'points': self.points,
            'views': self.views,
            'pictures': [pic.toDict() for pic in self.pictures]
        
    
        """
        user = User("bob", "bobpass")
        user_json = user.toDict()
        self.assertDictEqual(user_json, {"id":None, "username":"bob"})
        

    def test_return_type(self):
        #self.assertIsInstance(obj, cls)
        pass

    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password)
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password)

class PictureUnitTests(unittest.TestCase):

    def test_new_picture():
        pass

    def test_picture_tojson():
        pass


class RatingUnitTests(unittest.TestCase):
    
    def  test_create_rating(self):
        pass

    def test_rating_structure(self):
        pass





'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    user = create_user("bob", "bobpass")
    assert authenticate("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"

class PictureIntegrationTests(unittest.TestCase):

    def test_add_image(self):
        pass
    
    def test_delete_image(self):
        pass

    def test_like_image(self):
        pass
    
    def test_dislike_image(self):
        pass

class RatingIntegrationTests(unit.TestCase):

    def test_create_rating(self):
        pass

    def test_upate_rating(self):
        pass

    def test_delete_rating(self):
        pass
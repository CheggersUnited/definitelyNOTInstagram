import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User, Picture, Rating
from App.controllers import (
    create_user,
    get_all_users_json,
    get_all_pictures_json,
    authenticate,
    get_user,
    update_user,
    add_picture,
    delete_picture,
    get_picture,
    like_a_pic,
    dislike_a_pic,
    add_rating,
    delete_rating,
    update_rating,
    get_rating
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bob", "bobpass", "bob@mail.com")
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
        user = User("bob", "bobpass", "bob@mail.com")
        user_json = user.toDict()
        self.assertDictEqual(user_json,
        {
            "id": None,
            "username": "bob",
            "email": "bob@mail.com",
            "tier": 1,
            "limit": 5,
            "points": 0.0,
            "views": 0,
            "pictures": []
        }
        )
        
    """
    def test_return_type(self):
        self.assertIsInstance(obj, cls)
`   """
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password, "bob@mail.com")
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password, "bob@mail.com")
        assert user.check_password(password)

class PictureUnitTests(unittest.TestCase):

    def test_new_picture(self):
        picture = Picture(1, "https://picsum.photos/600")
        assert picture.uid == 1 and picture.url == "https://picsum.photos/600"

    def test_picture_tojson(self):
        picture = Picture(1, "https://picsum.photos/600")
        picture_json = picture.toDict()
        self.assertDictEqual(picture_json, {"pid": None, "uid": 1, "url": "https://picsum.photos/600", "likes":0, "dislikes":0, "points":0.0, "distribution":0})


class RatingUnitTests(unittest.TestCase):
    
    def  test_create_rating(self):
        rating = Rating(1, 1, True)
        assert rating.uid == 1 and rating.pid == 1 and rating.rating == True

    def test_rating_tojson(self):
        rating = Rating(1, 1, True)
        rating_json = rating.toDict()
        self.assertDictEqual(rating_json, {"id": None, "uid": 1, "pid": 1, "rating": True})





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

class UserIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass", "rick@mail.com")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"rick", "email": "rick@mail.com", "tier":1, "limit":5, "points":0.0, "views":0, "pictures":[]}], users_json)

    def test_update_user(self):
        user = update_user(1, "ronnie")
        assert user.username == "ronnie"

class PictureIntegrationTests(unittest.TestCase):

    def test1_add_image(self):
        create_user("ryan", "ryanpass", "ryan@mail.com")
        picture = add_picture(1, "https://picsum.photos/600")
        assert picture.pid != None
    
    def test2_like_image(self):
        picture = get_picture(1)
        points = picture.points
        like_a_pic(1, 1)
        assert points < picture.points
    
    def test3_dislike_image(self):
        picture = get_picture(1)
        points = picture.points
        dislike_a_pic(1, 1)
        assert points > picture.points

    def test4_delete_image(self):
        delete_picture(1)
        self.assertEquals(get_picture(1), None)

class RatingIntegrationTests(unittest.TestCase):

    def test1_create_rating(self):
        rating = add_rating(1, 1, True)
        assert rating.id != None

    def test2_update_rating(self):
        rating = update_rating(1, False)
        assert rating.rating == False

    def test3_delete_rating(self):
        delete_rating(1)
        self.assertEquals(get_rating(1), None)
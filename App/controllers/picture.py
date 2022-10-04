from App.models import Picture
from App.database import db

def add_picture(uid, url):
    picture = Picture(uid=uid, url=url)
    if len(picture.user.pictures) < 5:
        db.session.add(picture)
        db.session.commit()
        return "Picture added to {}'s profile".format(picture.user.username)
    return 'Unable to add any more pictures. Limit reached.'

def delete_picture(pid):
    picture = Picture.query.filter_by(pid=pid).first()
    if picture:
        db.session.delete(picture)
        db.session.commit()
        return 'Picture was successfully removed'
    return 'Invalid picture selected'
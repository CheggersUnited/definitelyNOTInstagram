import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, get_user, get_picture, add_picture, delete_picture, add_rating, like_a_pic, dislike_a_pic, get_all_pictures, get_all_pictures_json )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("email", default="rob@mail.com")
def create_user_command(username, password, email):
    user = create_user(username, password, email)
    if user:
        add_picture(user.id, "https://picsum.photos/600")
        print(f'{username} created!')
    else:
        print("user already exists")

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    elif format == 'pics':
        print(get_all_pictures_json())
    else:
        print(get_all_users_json())

@user_cli.command('addpic', help="Adds a picture to user profile")
@click.argument('uid')
def add_pic(uid):
    add_picture(uid, "https://picsum.photos/600")
    print("picture added to {}'s profile".format(get_user(uid).username))

@user_cli.command('delpic', help="Deletes a picture from user profile")
@click.argument('pid')
def add_pic(pid):
    user = get_picture(pid).user
    delete_picture(pid)
    print("picture deleted from {}'s profile".format(user.username))

@user_cli.command("get", help="Returns a user")
@click.argument("id", default="1")
def get_user_command(id):
    print(get_user(id))

@user_cli.command("like", help="likes a picture")
@click.argument("uid")
@click.argument("pid")
def like_pic_command(uid, pid):
    like_a_pic(uid, pid)
    print('pic liked')

@user_cli.command("dislike", help="dislikes a picture")
@click.argument("uid")
@click.argument("pid")
def dislike_pic_command(uid, pid):
    dislike_a_pic(uid, pid)
    print('pic disliked')

app.cli.add_command(user_cli) # add the group to the cli


'''
Generic Commands
'''


@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')


'''
Test Commands
'''


test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

@test.command("picture", help="Run Picture tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "PictureUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "PictureIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    
@test.command("rating", help="Run Rating tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "RatingUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "RatingIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

app.cli.add_command(test)
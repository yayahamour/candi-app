from app import *
from app.models import User, Role, UserRoles
import pytest

@pytest.fixture
def my_user1():
    my_user1 = User(name="Rudy", email="rudy@gmail.com", password="123456")
    return my_user1

@pytest.fixture
def my_user2():
    my_user2 = User(name="user", email="user@gmail.com", password="123456")
    return my_user2

@pytest.fixture
def my_admin():
    my_admin = Role(name="Admin")
    return my_admin

@pytest.fixture
def my_agent():
    my_agent = Role(name="Agent")
    return my_agent

def test_models(my_user1, my_admin, my_user2, my_agent):
    assert my_user1.name == "Rudy"
    my_user1.roles.append(my_admin)
    assert my_user1.has_roles("Admin")
    my_user2.roles.append(my_agent)
    assert my_user2.has_roles("Agent")
    assert my_user2.name == "user"
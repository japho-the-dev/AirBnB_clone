#!/usr/bin/python3
import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """
    Test case for User.
    """
    def setUp(self):
        """ Create a User."""
        self.user = User()

    def test_user_id(self):
        userId = self.user.id

    def test_user_first_name(self):
        """ Set and get first name.
        """
        self.user.first_name = "Jack"
        self.assertEqual(self.user.first_name, "Jack")

    def test_user_last_name(self):
        """ Set and get lastname.
        """
        self.user.last_name = "Sparrow"
        self.assertEqual(self.user.last_name, "Sparrow")

    def test_user_email(self):
        """ SET and get email.
        """
        self.user.email = "hello@world.com"
        self.assertEqual(self.user.email, "hello@world.com")

    def test_user_password(self):
        """
        Set and Get password.
        """
        self.user.password = "helloworld12345"
        self.assertEqual(self.user.password, "helloworld12345")

    def test_inherited_attributes(self):
        """ Validation
        """
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)

    def test_user_default_attributes(self):
        """ Check if all attributes are present.
        """
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")


if __name__ == '__main__':
    unittest.main()

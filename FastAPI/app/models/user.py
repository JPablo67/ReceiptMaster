"""
Pydantic models for the User entity.
"""

from typing import Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """
    Pydantic model representing a user in the system.

    Attributes:
        user_id (int): The unique identifier for the user.
        username (str): The user's username.
        email (str): The user's email address.
        password (str): The user's password.
        phone_number (Optional[str]): The user's phone number (optional).
        profile_picture (Optional[str]): The URL to the user's profile picture (optional).
    """

    user_id: int
    username: str
    email: str
    password: str
    phone_number: Optional[str] = None
    profile_picture: Optional[str] = None

    class Config:
        """
        Pydantic configuration class to enable ORM mode and provide an example schema.
        """
        orm_mode = True
        schema_extra = {
            "example": {
                "user_id": 1,
                "username": "johndoe",
                "email": "johndoe@example.com",
                "phone_number": "+1234567890",
                "profile_picture": "http://example.com/avatar.jpg"
            }
        }
        
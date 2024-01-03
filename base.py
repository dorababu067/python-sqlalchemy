from db_config import db, Base


# Define an abstract base class for SQLAlchemy models
class BaseModel(Base):
    # Mark the class as abstract to prevent mapping to a database table
    __abstract__ = True

    # Create a query property associated with the session
    query = db.query_property()

    @classmethod
    def create(cls, **kwargs):
        """
        Create a new instance of the model with the provided keyword arguments.

        Example usage:
        user = User.create(username='john_doe', email='john@example.com')
        """
        # Instantiate the model with provided arguments
        instance = cls(**kwargs)
        # Add the instance to the session
        db.add(instance)
        # Commit changes to the database
        db.commit()
        return instance

    def save(self):
        """
        Add the current instance to the session and commit changes to the database.

        Example usage:
        new_user = User(username="Alapakam Dorababu", email="dorababu@example.com")
        new_user.save()
        """
        db.add(self)
        db.commit()

    def update(self, **kwargs):
        """
        Update the attributes of the current instance with the provided keyword arguments
        and commit changes to the database.

        Example usage:
        user.update(username='updated_username')
        """
        # Update instance attributes with provided values
        for key, value in kwargs.items():
            setattr(self, key, value)
        # Commit changes to the database
        db.commit()
        return self

    def delete(self):
        """
        Delete the current instance from the session and commit changes to the database.
        """
        # Delete the instance from the session
        db.delete(self)
        # Commit changes to the database
        db.commit()

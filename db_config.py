from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


DATABASE_URL = config("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# method 1
Database = scoped_session(sessionmaker(bind=engine))


class CRUDMixin(object):
    @classmethod
    def create(cls, **kwargs):
        # Example usage
        # user = User.create(username='john_doe', email='john@example.com')
        instance = cls(**kwargs)
        db.add(instance)
        db.commit()
        return instance

    def update(self, **kwargs):
        # Update user and post
        # user.update(username='updated_username')

        for key, value in kwargs.items():
            setattr(self, key, value)
        db.commit()
        return self

    def delete(self):
        # Delete post
        # post.delete()

        db.delete(self)
        db.commit()


class _Base(CRUDMixin):
    query = Database.query_property()


db = Database
Base = declarative_base(cls=_Base)


# # method 2
# Database = scoped_session(sessionmaker(bind=engine))
# Base = declarative_base()
# db = Database
# users = db.query(User).all()

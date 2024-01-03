from models import User


# Create
# new_user = User(username="Alapakam Dorababu6", email="dora6@example.com")
# new_user.save()


# # Read
users = User.query.all()

for user in users:
    print(user.id, user.username, user.email)

# # Update
# user_to_update = db.query(User).filter_by(username="john_doe").first()
# user_to_update.email = "john.doe@example.com"
# db.commit()

# # Delete
# user_to_delete = db.query(User).filter_by(username="john_doe").first()
# db.delete(user_to_delete)
# db.commit()

import os
from app import create_app
from app.db_con import create_tables
from app.api.v2.models.users import UserModel

user = UserModel("admin@gmail.com", "admin", admin=True)


app = create_app()


if __name__ == '__main__':
    create_tables()
    user.save()
    app.run(debug=True,)

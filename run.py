from app import create_app
from app.db_con import create_tables


app = create_app()


if __name__ == '__main__':
    print(create_tables())
    app.run(debug=True,)

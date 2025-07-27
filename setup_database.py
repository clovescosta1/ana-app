from app import create_app, db

def setup_database():
    app = create_app()
    with app.app_context():
        db.create_all()
        print("? Banco de dados criado com sucesso!")

if __name__ == "__main__":
    setup_database()

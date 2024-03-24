from app import app, db
from models import Cupcake

# Create an application context to work with the database
with app.app_context():
    # Now you can directly use the 'db' instance for database operations
    db.drop_all()
    db.create_all()

    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    db.session.add_all([c1, c2])
    db.session.commit()

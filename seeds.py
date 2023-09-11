from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_database_models import Restaurant, Customer, Review  # Import your database models


DATABASE_FILE = "models.db"  


engine = create_engine(f"sqlite:///{DATABASE_FILE}")


Session = sessionmaker(bind=engine)
session = Session()


restaurants_data = [
    {"name": "Restaurant A", "price": 3},
    {"name": "Restaurant B", "price": 2},
    
]

customers_data = [
    {"first_name": "Jane", "last_name": "Foe"},
    {"first_name": "Aliya", "last_name": "Saun"},
    
]

reviews_data = [
    {"customer_id": 1, "restaurant_id": 1, "star_rating": 4},
    {"customer_id": 2, "restaurant_id": 2, "star_rating": 5},
    
]


for restaurant_info in restaurants_data:
    restaurant = Restaurant(**restaurant_info)
    session.add(restaurant)

for customer_info in customers_data:
    customer = Customer(**customer_info)
    session.add(customer)

for review_info in reviews_data:
    review = Review(**review_info)
    session.add(review)


session.commit()

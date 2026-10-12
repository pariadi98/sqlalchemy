from sqlalchemy import create_engine, Column, INTEGER, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///digishop.db')
engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'usersInfo'

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    address = Column(String)
    score = Column(Float)

class Product(Base):
    __tablename__ = 'productsInfo'

    id = Column(INTEGER, primary_key=True)
    name_product = Column(String)
    price = Column(Float)
    quantity = Column(INTEGER)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionLocal = Session()
###################################################

# user1 = User(name='Ali', address='Ahwaz', score=4.9)
# user2 = User(name='Morteza', address='Tehran', score=4.95)

# sessionLocal.add(user1)
# sessionLocal.add(user2)
# sessionLocal.commit()

# user3 = User(name='AliReza', address='Ahwaz', score=4.9)
# user4 = User(name='Nima', address='Isfahan', score=4.95)
# sessionLocal.add_all([user3, user4])
# sessionLocal.commit()

# users = sessionLocal.query(User).all() #--> select all records
# # print(users)
# for item in users:
#     print('name: ', item.name)
#     print('add: ', item.address)
#     print('score: ', item.score)
#     print('-' * 30)  

# product1 = Product(name_product='Laptop', price=2000, quantity = 30)
# product2 = Product(name_product='Mobile', price=1500, quantity = 50)
# sessionLocal.add_all([product1, product2])
# sessionLocal.commit()

# temp_user = sessionLocal.query(User).filter_by(address='Ahwaz', name='Ali').all()
# print(temp_user)
# print(temp_user[-1].name)
# print(temp_user[-1].address)
#########################################################

# temp_user = sessionLocal.query(User).filter(User.score > 4.9).all()
# # print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.score)
# #     print('-'*30)
# temp_user = sessionLocal.query(User).filter(User.name.like('%Ali')).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.score)
#     print('-'*30)

user = sessionLocal.query(User).filter_by(id=1).first()

# user.name = 'Saeed'
# user.address = 'Tabriz'
# sessionLocal.commit()

############################################

if user !=None:
    sessionLocal.delete(user)
    sessionLocal.commit()
from . import db
from .models import Customer, Product, Order, Artiste, Song
from flask import jsonify
# database storage

class Storage:

    classes = {
        "customer": Customer,
        "product": Product,
        "order": Order,
        "artiste": Artiste,
        "song": Song
    }

    def all(self, cls=None):
        """ gets the table pass in to get all data """
        for key in self.classes.keys():
            if self.classes[key] == cls:
                data = cls.query.all()
                return (data)
            else:
                return None
            
    def get_by_id(self, cls ,id):
        """ get item from the database """
        if cls is None:
            return None
        for key in self.classes.keys():
            if self.classes[key] == cls:
                data = cls.query.filter_by(id).first()
            else:
                return "Data does not exists"
    
    def delete_data(self, cls, id):
        """ delete item from the database """
        if cls is None:
            return None
        for key in self.classes.keys():
            if self.classes[key] == cls:
                data = cls.query.filter_by(id).first()
                db.session.delete(data)
                db.self.save()
                return jsonify({})
            else:
                return "Data does not exists"
            
    def save(self):
        """ save to the database """
        db.session.commit()


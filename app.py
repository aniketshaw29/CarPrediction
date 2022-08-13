import pickle

#to retrive pickled data
model = pickle.load(open("car_price_prediction_model.pickle", "rb")) #rb stands for read-binary mode


#year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner
print(int(model.predict([[2015, 5.90, 60000, 0, 0, 0, 0]])))

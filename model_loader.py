import pickle

Filename = 'intensity_vs_mileage.sav'
loaded_model = pickle.load(open(Filename, 'rb'))

def lamda_handler(event,context):
    Mileage=loaded_model.predict([[event.oil_intensity]])
    return Milage[0]

Mileage=loaded_model.predict([[0.456]])
# print(Mileage)

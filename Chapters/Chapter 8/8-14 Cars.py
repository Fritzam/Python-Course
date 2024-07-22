def car_builder(manufacturer, model, **traits):
    assembled_car = {'Manufacturer': manufacturer, 'Model': model}
    for key, value in traits.items():
        assembled_car[key] = value

    return assembled_car


print(car_builder("Mazda", '6', Class='Medium', Reliability='High', Style='S+'))

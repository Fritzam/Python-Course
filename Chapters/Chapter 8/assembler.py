def car_builder(manufacturer, model, **traits):
    assembled_car = {'Manufacturer': manufacturer, 'Model': model}
    for key, value in traits.items():
        assembled_car[key] = value

    return assembled_car
from apps.services import hue
import pandas as pd



def light__df(light_cols = ['sdk', 'id_', 'name', 'is_on', 'bri', 'hue', 'sat']):
    return pd.DataFrame([o.__dict__ for o in hue.get_lights()])[light_cols]

def light_list(light_cols = ['sdk', 'id_', 'name', 'is_on', 'bri', 'hue', 'sat']):
    return hue.get_lights()

def toggle_light(light_id):
    x = hue.get_light(id_=light_id)
    if x.is_on:
        x.off()
    else:
        x.on()
    return x.is_on
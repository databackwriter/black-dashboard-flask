from apps.services import hue
import pandas as pd

groups = hue.get_groups()

# Print light properties
for group in groups:
    print(group.id_)
    print(group.name)

def light__df(light_cols = ['sdk', 'id_', 'name', 'is_on', 'bri', 'hue', 'sat']):
    return pd.DataFrame([o.__dict__ for o in hue.get_lights()])[light_cols]

def light_list(light_cols = ['sdk', 'id_', 'name', 'is_on', 'bri', 'hue', 'sat']):
    return sorted(hue.get_lights(), key=lambda x: x.name, reverse=True)

def toggle_light(light_id):
    x = hue.get_light(id_=light_id)
    if x.is_on:
        x.off()
    else:
        x.on()
    return x.is_on
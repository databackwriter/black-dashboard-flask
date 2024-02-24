from apps.services import hue

lights = hue.get_lights()
for _ in lights:
    print(_.name, _.id_)

def toggle_light(light_id):
    x = hue.get_light(id_=light_id)
    if x.is_on:
        x.off()
    else:
        x.on()
    return x.is_on
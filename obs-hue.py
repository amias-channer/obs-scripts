import obspython as S
from phue import Bridge
import time
import json


# Amias Channer
# An OBS Python script that allows you to control settings on your hue lights from custom obs hotkeys
# Two hotkeys are assigned
# To use this you will need the phue python library installed
#   pip3 install phue
#
#   for info on settings and values
#   https://github.com/studioimaginaire/phue
#
#  This is set to trigger the colour loop effect on and off with two hotkeys.
#  You could add more hotkeys and trigger static colour settings by adding
#  more instances of h and adding to script_load and script_save


class Hotkey:
    def __init__(self, callback, obs_settings, _id):
        self.obs_data = obs_settings
        self.hotkey_id = S.OBS_INVALID_HOTKEY_ID
        self.hotkey_saved_key = None
        self.callback = callback
        self._id = _id

        self.load_hotkey()
        self.register_hotkey()
        self.save_hotkey()

    def register_hotkey(self):
        description = "Htk " + str(self._id)
        self.hotkey_id = S.obs_hotkey_register_frontend(
            "htk_id" + str(self._id), description, self.callback
        )
        S.obs_hotkey_load(self.hotkey_id, self.hotkey_saved_key)

    def load_hotkey(self):
        self.hotkey_saved_key = S.obs_data_get_array(
            self.obs_data, "htk_id" + str(self._id)
        )
        S.obs_data_array_release(self.hotkey_saved_key)

    def save_hotkey(self):
        self.hotkey_saved_key = S.obs_hotkey_save(self.hotkey_id)
        S.obs_data_set_array(
            self.obs_data, "htk_id" + str(self._id), self.hotkey_saved_key
        )
        S.obs_data_array_release(self.hotkey_saved_key)


class h:
    htk_copy = None  # this attribute will hold instance of Hotkey


class Option:
    txt = "default txt"


def _configure_hue(params):
    bridge = Bridge(hueIP.txt)
    for light in bridge.get_light_objects():
        light._set(params)
        time.sleep(1)


def cb1(pressed):
    if pressed:
        print("Hue on")
        # toggle colorloop at max saturation and brightness
        setting = {
            'on': True,
            'effect': 'colorloop',
            'sat': 255,
            'bri': 255,
            'transitiontime': 100,
        }
        _configure_hue(setting)


def cb2(pressed):
    if pressed:
        # default behaviour is switch off
        setting = {
            'on': True,
            'effect': 'none',
            'sat': 255,
            'bri': 255,
        }
        _configure_hue(setting)


hueIP = Option()

h1 = h()
h2 = h()


def script_properties():
    props = S.obs_properties_create()
    S.obs_properties_add_text(props, "_hueIP", "Hue Bridge IP ", S.OBS_TEXT_DEFAULT)
    return props


def script_update(settings):
    _ip = S.obs_data_get_string(settings, "_hueIP")
    hueIP.txt = _ip


def script_load(settings):
    h1.htk_copy = Hotkey(cb1, settings, "Hue On")
    h2.htk_copy = Hotkey(cb2, settings, "Hue Off")


def script_save(settings):
    h1.htk_copy.save_hotkey()
    h2.htk_copy.save_hotkey()



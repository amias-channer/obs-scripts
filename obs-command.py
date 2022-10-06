import os

import obspython as S

# by Amias Channer 2022 , apache licence.

# An OBS Python script that allows you to run commands from custom obs hotkeys
# Two hotkeys are assigned
#
#  You could add more hotkeys and trigger more commands by adding
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


def run_command(pressed):
    if pressed:
        os.system(command_line.txt)


def script_properties():
    props = S.obs_properties_create()
    S.obs_properties_add_text(props, "_command", "Command to run", S.OBS_TEXT_DEFAULT)
    return props


def script_update(settings):
    _command = S.obs_data_get_string(settings, "_command")
    command_line.txt = _command


def script_load(settings):
    h1.htk_copy = Hotkey(run_command, settings, "Run Command")


def script_save(settings):
    h1.htk_copy.save_hotkey()


command_line = Option()

h1 = h()

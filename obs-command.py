import json
import os

import obspython as obs

# by Amias Channer 2022 , apache licence. v2

# An OBS Python script that allows you to run commands from custom obs hotkeys
# up to six hotkey commands are supported .
#
#  You could add more hotkeys and trigger more commands by increasing state.count and adjusting script_load to  adding
#  more instances of h and adding to script_load and script_save


class Hotkey:
    def __init__(self, callback, obs_settings, _id):
        self.obs_data = obs_settings
        self.hotkey_id = obs.OBS_INVALID_HOTKEY_ID
        self.hotkey_saved_key = None
        self.callback = callback
        self._id = _id

        self.load_hotkey()
        self.register_hotkey()
        self.save_hotkey()

    def register_hotkey(self):
        description = str(self._id)
        self.hotkey_id = obs.obs_hotkey_register_frontend(
            "htk_id" + str(self._id), description, self.callback
        )
        obs.obs_hotkey_load(self.hotkey_id, self.hotkey_saved_key)

    def load_hotkey(self):
        self.hotkey_saved_key = obs.obs_data_get_array(
            self.obs_data, "htk_id" + str(self._id)
        )
        obs.obs_data_array_release(self.hotkey_saved_key)

    def save_hotkey(self):
        self.hotkey_saved_key = obs.obs_hotkey_save(self.hotkey_id)
        obs.obs_data_set_array(
            self.obs_data, "htk_id" + str(self._id), self.hotkey_saved_key
        )
        obs.obs_data_array_release(self.hotkey_saved_key)


class Runtime:
    hotkeys = {}   # t dict of instances of Hotkey
    count = 6
    commands = {}


#    ----   functions called by OBS   ----

def script_properties():
    props = obs.obs_properties_create()
    for i in range(state.count):
        obs.obs_properties_add_text(props, "_{}".format(i), "Command {0}".format(i+1), obs.OBS_TEXT_DEFAULT)
    return props


def script_update(settings):
    for i in range(state.count):
        _command = obs.obs_data_get_string(settings, "_{}".format(i))
        state.commands[i] = _command


def script_load(settings):
    # set up the hotkeys, indvidual callback functions because you cant detect which one is clicked otherwise.
    state.hotkeys[0] = Hotkey(cmd_one,   settings, "Run Command 1")
    state.hotkeys[1] = Hotkey(cmd_two,   settings, "Run Command 2")
    state.hotkeys[2] = Hotkey(cmd_three, settings, "Run Command 3")
    state.hotkeys[3] = Hotkey(cmd_four,  settings, "Run Command 4")
    state.hotkeys[4] = Hotkey(cmd_five,  settings, "Run Command 5")
    state.hotkeys[5] = Hotkey(cmd_six,   settings, "Run Command 6")


def script_save(settings):
    for i in range(state.count):
        state.hotkeys[i].save_hotkey()


#    ----  functions called by call backs

def run_command(pressed):
    print("pressed: {0}".format(pressed))
    if pressed:
        os.system(state.commands[pressed])


# these are because i couldn't parameterize the call back from Hotkey
# which would have meant run_command couldn't tell which hotkey was pressed.

def cmd_one(pressed):
    run_command(1)


def cmd_two(pressed):
    run_command(2)


def cmd_three(pressed):
    run_command(3)


def cmd_four(pressed):
    run_command(4)


def cmd_five(pressed):
    run_command(5)


def cmd_six(pressed):
    run_command(6)


# initialisation

state = Runtime()

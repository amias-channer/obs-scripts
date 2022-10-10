import json
import os

import obspython as obs

# by Amias Channer 2022 , apache licence.

# An OBS Python script that allows a hotkey to trigger a step through the scenes at a configurable interval
#
# the script will advance down the list of Scenes to the end


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
        description = "Htk " + str(self._id)
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
    start = None  # hotkey to start
    end = None    # hotkey to stop


class Options:
    interval = ''


def hotkey_callback_start(pressed):
    if pressed:
        obs.timer_add(scene_advance, options.interval)


def hotkey_callback_end(pressed):
    if pressed:
        obs.timer_remove(scene_advance)


def scene_advance():
    current = obs.obs_frontend_get_current_scene()
    set_next_scene(current)


def set_next_scene(current):
    scenes = obs.obs_frontend_get_scenes()
    get_next = 0

    # find out scene and then select the next one
    for scene in scenes:
        if get_next == 1:
            obs.obs_frontend_set_current_scene(scene)
            get_next = 0

        if scene == current:
            get_next = 1
            # go to the top of the list and restart if this is the last
            if scene == scenes[-1]:
                obs.obs_frontend_set_current_scene(scenes[1])


def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_int_slider(props, "_interval", "Step time", 1000, 10000, 250)
    return props


def script_update(settings):
    options.interval = obs.obs_data_get_int(settings, "_interval")


def script_load(settings):
    state.start = Hotkey(hotkey_callback_start, settings, "Cycle Start")
    state.end = Hotkey(hotkey_callback_end, settings, "Cycle End")


def script_save(settings):
    state.start.save_hotkey()
    state.end.save_hotkey()


options = Options()
state = Runtime()

from utils.enums import SoundPaths, MusicTrack, Sfx


def build_sound_path(sound_enum_value):
    if isinstance(sound_enum_value, Sfx):
        return f"{SoundPaths.SFX.path}{sound_enum_value.sfx_file}"
    elif isinstance(sound_enum_value, MusicTrack):
        return f"{SoundPaths.MUSIC.path}{sound_enum_value.track_file}"
    else:
        raise ValueError(f"Unknown sound enum type: {sound_enum_value}")

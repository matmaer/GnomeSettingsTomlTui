# GnomeSettingsTomlTui
TUI app to set a batch of Gnome settings from a Toml configuration file.

Modern terminal app, or terminal user interfoce (TUI) to set Gnome settings for Gnome itself and applications that use the gsettings API in the dconf database.

The desired settings are provided by the user in a Toml file.  If you don't have a Toml file yet, you can generate a toml config file with the all settings. This file contains all the relevant and usefull setting-schemas with keys, values, type and range. This generated config can be edited with your custom settings.

The Toml config file with these settings should usable on any Linux distribution with any Gnome 3 desktop environment.

Changing these settings is normally done in the Gnome GUI by the user.  On some occasions, for example to configure a newly created user or to verify your current settings against your custom config; you could save some time as opposed to doing this "manually" in the Gnome GUI.  

Gnome is [available](https://www.gnome.org/getting-gnome/) for most major Linux distributions.

Build with [Textual](https://github.com/Textualize/textual), which is part of probably the best Rapid Application Development framework for Python at present time. It's lean, stable and user friendly, at least from my experience. See also [textual.textualize.io](https://textual.textualize.io/).

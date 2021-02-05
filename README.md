# mpv by RisGar

My configuration for mpv I use for anime. Most stuff is forked from [LightArrowsEXE's mpv config](https://github.com/LightArrowsEXE/dotfiles/tree/master/mpv/.config/mpv).

By default FSRCNNX is used for upscaling. If you notice heavy frame drops, please comment the import and uncomment ravu-r3 instead.
YouTube-DL is not included. You can install it from its official repository. Link below.

The included updater.bat is taken from [shinchiro's SourceForge build of mpv](https://sourceforge.net/projects/mpv-player-windows/files/). It does not update the mpv.conf, but instead mpv itself. I highly suggest updating as frequently as possible.

## How to install the base setup:

**Windows:**<br>

1. Create a new folder in `%appdata%` and call it mpv. <br>
2. Dump the contents of this directory in there. <br>
3. Change the paths as necessary in `mpv.conf`.<br>
4. **OPTIONAL:** Run `updater.bat` as Administrator to update your mpv.

**Linux:**<br>
TBA

## How to install VapourSynth and the filtering dependencies:

1. Install the [latest version of VapourSynth](https://github.com/vapoursynth/vapoursynth/releases).<br>
   1.5. Install the latest required version of [Python](https://www.python.org/downloads/), and make sure it's added to PATH.<br>
2. Locate the following directories:<br> \* C:\Users\[your username]\AppData\Roaming\VapourSynth\plugins64<br> \* C:\Users\[your username]\AppData\Local\Programs\Python\Python38\Lib\site-packages<br>
3. Check the .vpy scripts in the repo (in the `vs` directory) and follow the links to the listed dependencies.
4. Download and move the required files to the relevant directories (Python modules go to the `site-packages` directory, everything else goes in the `plugins64` directory).
5. Verify that the scripts are running as intended by cycling through the profiles and pressing the `~` key during playback. It should tell you if it failed, and if it did what the missing dependencies are.
6. To get Discord-RPC to work, copy the dll for your os in the lib folder into mpv's main directory.

## Dependencies:

- [Youtube-dl](https://github.com/ytdl-org/youtube-dl/releases)
- [Gandhi Sans](https://www.fontsquirrel.com/fonts/gandhi-sans) and [Noto Sans](https://fonts.google.com/specimen/Noto+Sans)

## Included shaders/scripts:

- [acompressor](https://github.com/mpv-player/mpv/blob/master/TOOLS/lua/acompressor.lua)
- [autocrop](https://github.com/mpv-player/mpv/blob/master/TOOLS/lua/autocrop.lua)
- [autoload](https://github.com/mpv-player/mpv/blob/master/TOOLS/lua/autoload.lua)
- [auto-profiles](https://github.com/wiiaboo/mpv-scripts/blob/master/auto-profiles.lua)
- [boss-key](https://github.com/detuur/mpv-scripts) - currently deactivated
- [playlistmanager](https://github.com/jonniek/mpv-playlistmanager)
- [reload](https://github.com/4e6/mpv-reload)
- [repl](https://github.com/rossy/mpv-repl)
- [status-line](https://github.com/mpv-player/mpv/blob/master/TOOLS/lua/status-line.lua)
- [visualizer](https://github.com/mfcc64/mpv-scripts/blob/master/visualizer.lua)
- [mpv-discordRPC](https://github.com/noaione/mpv-discordRPC/blob/master/Scripts/mpv-drpc.lua) - currently deactivated

- [FSRCNNX](https://github.com/igv/FSRCNN-TensorFlow/releases)
- [KrigBilateral](https://gist.github.com/igv/a015fc885d5c22e6891820ad89555637)
- [Static Noise Luma](https://pastebin.com/yacMe6EZ)
- [ravu-r3](https://github.com/bjin/mpv-prescalers)

Other:

- [Shinchiro's mpv updater](https://sourceforge.net/projects/mpv-player-windows/files/)

_For additional shaders and scripts, check out the following sources:_

- [Shaders](https://github.com/mpv-player/mpv/wiki/User-Scripts#user-shaders)
- [Scripts](https://github.com/mpv-player/mpv/wiki/User-Scripts#lua-scripts)

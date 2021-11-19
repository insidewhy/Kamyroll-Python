![app workflow](https://github.com/insidewhy/cuteroll/workflows/main/badge.svg)

## Description
cuteroll is a python version app that can be used to download videos and subtitles from Crunchyroll in MP4 and ASS formats.
 
## Features
- Download videos in all resolutions
- Download subtitles in all languages
- Search for videos
- Compatible with or free or premium account
- Use a proxy to unblock the entire catalog
- Available for all platforms (macOS, Windows, Linux, etc.)
- Download all available episodes and movies
- Videos in mp4, mkv with or without Hardsub
- Premium bypass (windows version only)
- Download episodes by interval or number (bash download)

## Requirements
- [ffmpeg](https://www.ffmpeg.org)
- [Python](https://www.python.org/downloads) 3+

### Installation
```bash
pip install cuteroll
```

## Information
 - To use the script log in with your email or username and your Crunchyroll password.
 - Configure your configuration file according to your preferences.
 - If you don't have Python, you can use the compiler version for Windows.
 - Use the premium bypass to download the premium videos.
 - The premium bypass uses a premium pay account dedicated to this use. It is in no way a crack of the site or the API.

## Preferences

#### Video resolution

Resolution | Quality
------------ | -------------
"1080" | FHD
"720" | HD
"480" | SD
"360" | SD
"240" | SD

#### Playlist selection

Resolution | Quality
------------ | -------------
"[3:]" | Take all episodes after 3
"[2:4]" | Take episodes 2 to 4 included
"[-2]" | Take the penultimate episode from the list
"[-2:]" | Take all the last episode from the penultimate
"[:-2]" | Take all episodes except the last 2
"8" | Take episode 8

#### Subtitle language 

Language | Title
------------ | -------------
"" | Without subtitles
"en-US" | English (US)
"en-GB" | English (UK)
"es-419" | Español
"es-ES" | Español (España)
"pt-BR" |Português (Brasil)
"pt-PT" | Português (Portugal)
"fr-FR" | Français (France)
"de-DE" | Deutsch
"ar-SA" | العربية
"it-IT" | Italiano
"ru-RU" | Русский

## Proxy configuration
Secure proxy compatible with Crunchyroll: https://github.com/Snawoot/hola-proxy
![proxy_example](/Presentation/img_proxy.png)

#### Command
- RED: Selected region
  
#### Proxy in $HOME/.config/cuteroll.json
- GREEN: uuid
- BLUE: agent\_key
- PURPLE: host
- YELLOW: port

## Examples

### Login with ID
```
cuteroll --login "MAIL:PASSWORD"
```
or
```
cuteroll -l "MAIL:PASSWORD"
```

### Login with configured ID
```
cuteroll --connect
```
or
```
cuteroll -c
```

### Search a series, films, episode
```
cuteroll --search "QUERY"
```

### Show seasons of a series
```
cuteroll --season "SERIES_ID"
```
or
```
cuteroll -s "SERIES_ID"
```

### Show episodes of a season
```
cuteroll --episode "SEASON_ID"
```
or
```
cuteroll -e "SEASON_ID"
```

### Show movies from a movie list
```
cuteroll --movie "MOVIE_ID"
```
or
```
cuteroll -m "MOVIE_ID"
```

### Download an episode or movie
```
cuteroll --download "EPISODE_ID or MOVIE_ID"
```
or
```
cuteroll -d "EPISODE_ID or MOVIE_ID"
```

### Download playlist (bash download)
```
cuteroll --download "SEASON_ID" --playlist "[START:END]"
```
or
```
cuteroll -d "SEASON_ID" -p "[START:END]"
```

### Get the video stream link (m3u8)
```
cuteroll --url "EPISODE_ID or MOVIE_ID"
```
or
```
cuteroll -u "EPISODE_ID or MOVIE_ID"
```

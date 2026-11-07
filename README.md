

# Python Audio Corruptor (a sequel to (Python Video Corruptor)[https://github.com/denwastkn/pyvidcorruptor/])
FFmpeg is required! ⚠️
To install ffmpeg, follow the guide below.

### Windows
```
winget install Gyan.FFmpeg
```
### Ubuntu based/Debian based
```
sudo apt install ffmpeg
```

### Fedora

```
sudo dnf install ffmpeg
```

### Termux/Android
```
pkg install ffmpeg
```

### Arch based
```
sudo pacman -S ffmpeg
```

### Alpine
```
sudo apk add ffmpeg
```

## Your.... Router?? (OpenWRT)

1. SSH into the router

2. Execute :

Latest :

```
apk add ffmpeg python3
```

Older :

```
opkg install ffmpeg python3
```

### MacOS
```
brew install ffmpeg
```
Or
```
sudo port install ffmpeg
```
⚠️ MacPorts or Homebrew are needed for MacOS

## Python Audio corruptor

⚠️ Python is needed, get it from https://www.python.org/downloads/

This is a simple audio corruptor based off Python and FFmpeg.

To run it :
```
python pyaudiocorruptor.py
```
This is easy to modify.

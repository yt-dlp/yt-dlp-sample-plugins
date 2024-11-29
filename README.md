This repository contains a sample plugin package for [yt-dlp](https://github.com/yt-dlp/yt-dlp#readme).

See [yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#plugins) for more details.


## Installation

Requires yt-dlp `2023.01.02` or above.

### Install with pip

You can install this package with pip:
```
python3 -m pip install -U https://github.com/yt-dlp/yt-dlp-sample-plugins/archive/master.zip
```

### Install manually

1. Download the latest release zip from [releases](https://github.com/yt-dlp/yt-dlp-sample-plugins/releases) 

2. Add the zip to one of the [yt-dlp plugin locations](https://github.com/yt-dlp/yt-dlp#installing-plugins)

    - User Plugins
        - `${XDG_CONFIG_HOME}/yt-dlp/plugins` (recommended on Linux/MacOS)
        - `~/.yt-dlp/plugins/`
        - `${APPDATA}/yt-dlp/plugins/` (recommended on Windows)
    
    - System Plugins
       -  `/etc/yt-dlp/plugins/`
       -  `/etc/yt-dlp-plugins/`
    
    - Executable location
        - Binary: where `<root-dir>/yt-dlp.exe`, `<root-dir>/yt-dlp-plugins/`

For more locations and methods, see [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) 

## Development

See the [Plugin Development](https://github.com/yt-dlp/yt-dlp/wiki/Plugin-Development) section of the yt-dlp wiki.

### Dependencies

Add required dependencies to the `dependencies` section in the `pyproject.toml`.

#### Bundling with release zip

By default, the [release action](.github/workflows/release.yml) will try to bundle the dependencies in the release zip. 
For these dependencies to work, they must be pure python modules.
 
From within the plugin, you will also need to use an import pattern similar to the following:

```py
import sys
import pathlib


import_path = str(pathlib.Path(__file__).parent.parent.parent)

sys.path.append(import_path)
try:
	import some_dependency

except ImportError:
	some_dependency = None

finally:
	sys.path.remove(import_path)
```

If you do not want to bundle the dependencies with the release zip, you can add the dependencies to the exclusion list in the [release action](.github/workflows/release.yml).

## Release

To create a release, simply increment the version in the `pyproject.toml` file.
While convenient, conditional requirements or non pure python modules will most likely not work.
Please edit the `.github/workflows/release.yml` accordingly if you require more control.

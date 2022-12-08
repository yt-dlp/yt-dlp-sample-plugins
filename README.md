This repository contains a sample plugin package for [yt-dlp](https://github.com/yt-dlp/yt-dlp#readme). 

See [yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#plugins) for more details.


## Installation
You can install this package with pip:
```
python3 -m pip install -U https://github.com/yt-dlp/yt-dlp-sample-plugins/archive/master.zip
```

See [yt-dlp installing plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the many other ways this plugin package can be installed.


## Developer Tips

To learn how to write extractors in general, see the [yt-dlp developer instructions](https://github.com/yt-dlp/yt-dlp/blob/master/CONTRIBUTING.md#developer-instructions).

For information regarding the plugin spec, see the [plugins section of the yt-dlp README](https://github.com/yt-dlp/yt-dlp#plugins).


### Run and debug configuration
1. Set your IDE's run configuration to point to the `yt_dlp` Python module.
2. Add your project's root directory containing `yt_dlp_plugins` to `PYTHONPATH` environment variable (this may not be necessary with some IDE run configurations)
3. The `yt_dlp_plugins` folder should be automatically picked up by yt-dlp (run with `-v` to check)


### Importing extractors from other plugins

```py
from yt_dlp_plugins.extractor.example import ExampleIE
```

This works regardless of where the `example` plugin is installed on the system, as long as yt-dlp can find it. 
Your IDE may not be able to resolve the import, but it will work at runtime.

If the user does not have the `example` plugin installed, the import will fail and your extractor will not be imported (but yt-dlp will continue to run). 

The same applies for any other plugin type.

### Poetry configuration

In pyproject.toml:

```
[tool.poetry]
...
packages = [{ include = "yt_dlp_plugins" }]
...
```

See the [Poetry documentation](https://python-poetry.org/docs/pyproject/#packages) for more details.
from .sample import SamplePluginIE

# ⚠ When overriding yt-dlp's extractors, note that the extractor internals
# may change without warning, breaking the plugin


class _SampleOverridePluginIE(SamplePluginIE, plugin_name='O'):
    def _real_extract(self, url):
        self.to_screen(f'Passing through {type(self).__name__}')
        return super()._real_extract(url)

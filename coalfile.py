from coal import CoalFile
from util import git_clone, download, unzip, default_cmake_build, cp
from os import path

class GlmFile(CoalFile):
    repo = "https://github.com/g-truc/glm.git"
    url = "https://github.com/g-truc/glm/releases/download/%s/glm-%s.zip"
    zipfile = "glm.zip"
    exports = ["include"]
    def prepare(self):
        if "version" in self.settings:
            version = self.settings["version"]
            download(self.url % (version, version), self.zipfile)
            unzip(self.zipfile, 'temp')
        else:
            git_clone(self.repo, 'master', 'src')
    def package(self):
        cp('src/glm', 'include/')
        cp('temp/glm/glm', 'include/')
    def info(self, generator):
        generator.add_include_dir('include/')

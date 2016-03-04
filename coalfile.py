from coal import CoalFile
from util import git_clone, download, unzip, default_cmake_build, cp
from os import path

class GlmFile(CoalFile):
    url = "https://github.com/g-truc/glm.git"
    exports = ["include"]
    def prepare(self):
        git_clone(self.url, 'master', 'src')
    def package(self):
        cp('src/glm', 'include/')
    def info(self, generator):
        generator.add_include_dir('include/')

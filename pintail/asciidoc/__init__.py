# pintail - Build static sites from collections of Mallard documents
# Copyright (c) 2016 Shaun McCance <shaunm@gnome.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import subprocess
from lxml import etree

import pintail.site
import pintail.mallard

class AsciiDocPage(pintail.mallard.MallardPage, pintail.site.ToolsProvider):
    def __init__(self, directory, source_file):
        pintail.mallard.MallardPage.__init__(self, directory, source_file)

    @property
    def stage_file(self):
        if self.source_file.endswith('.adoc'):
            return self.source_file[:-5] + '.page'
        else:
            return self.source_file

    def stage_page(self):
        pintail.site.Site._makedirs(self.directory.stage_path)
        subprocess.call(['asciidoctor-mallard',
                         '-o', self.stage_path,
                         self.source_path])

    @classmethod
    def get_pages(cls, directory, filename):
        if filename.endswith('.adoc'):
            return [AsciiDocPage(directory, filename)]
        return []

    @classmethod
    def build_tools(cls, site):
        pass

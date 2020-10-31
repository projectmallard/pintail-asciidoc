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

class AsciiDocPage(pintail.mallard.MallardPage):
    """
    A page written in AsciiDoc, a general-purpose lightweight documentation format.

    The AsciiDocPage class works by converting AsciiDoc to Mallard XML
    using the asciidoctor-mallard plugin.
    """

    def __init__(self, source, filename):
        super().__init__(source, filename)

    @property
    def stage_file(self):
        """
        The name of the staged Mallard XML file for this AsciiDoc page.
        """
        if self.source_file.endswith('.adoc'):
            return self.source_file[:-5] + '.page'
        else:
            return self.source_file

    def stage_page(self):
        """
        Create a Mallard XML file in the stage.
        """
        pintail.site.Site._makedirs(self.directory.get_stage_path())
        subprocess.call(['asciidoctor-mallard',
                         '-o', self.get_stage_path(),
                         self.get_source_path()])

    @classmethod
    def create_pages(cls, source):
        """
        Create a list of pages for all AsciiDoc files in a source directory.
        """
        pages = []
        exclude = (source.site.config.get('exclude_files', source.name) or '').split()
        for filename in os.listdir(source.get_source_path()):
            if filename in exclude:
                continue
            if os.path.isfile(os.path.join(source.get_source_path(), filename)):
                if filename.endswith('.adoc'):
                    pages.append(AsciiDocPage(source, filename))
        return pages

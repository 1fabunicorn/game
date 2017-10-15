"""
    Game Data Class.
    Copyright (C) 2017,  Nova Trauben, noah.trauben@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from mainmodules import ignorethis


class data:

    def __init__(self, progress, login_count, stages, num_to_words, texts, encrypted_files):
        self.progress = int(ignorethis.read_progress())
        self.login_count = 1
        self.stages = 6
        self.num_to_words = {-1: 'welcome.blob', 0: "start", 1: "choices", 2: "second", 3: "third", 4: "forth", 5: "fifth"}
        self.texts = {-1: "texts/welcome.blob", 0: "texts/choices.blob", 1: "texts/sleep.blob", 2: "texts/AKAspy.blob"}
        self.encrypted_files = {-1: '../encrypted_texts/welcome.encrypted', 0: '../encrypted_texts/choices.encrypted',
                                1: '../encrypted_texts/sleep.encrypted', 2: '../encrypted_texts/AKAspy.encrypted'}

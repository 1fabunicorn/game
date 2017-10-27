"""
    Game Data Class.
    Copyright (C) 2017,  Nova Trauben, noah.trauben@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later  version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


class Data:
    """
    Game save class
    """

    def __init__(self):
        pass

    login_count = 1
    stages = abs(min(texts)) + max(texts)
    num_to_words = {-1: 'welcome.blob', 0: "start", 1: "choices", 2: "AKAspy", 3: "madhacker", 4: "forth", 5: "fifth"}
    texts = {-1: "texts/welcome.blob", 0: "texts/choices.blob", 1: "texts/sleep.blob", 2: "texts/AKAspy.blob", 3: "texts/madhacker.blob"}
    encrypted_files = {-1: '../encrypted_texts/welcome.encrypted', 0: '../encrypted_texts/choices.encrypted',
                       1: '../encrypted_texts/sleep.encrypted', 2: '../encrypted_texts/AKAspy.encrypted',
                       3: '../encrypted_texts/madhacker.encrypted'}
    python_scripts = ['brute_password.py', 'brute_password']
    # leak point lists
    saves = {
            "point_1": {"template.txt": 0, "qwerty.txt": 0},
            "point_2": {'b.txt': 0, 'l.txt': 0, 'a.txt': 0, 't.txt': 0},
            "point_3": {'q.txt': 0, 'w.txt': 0, 'e.txt': 0, 'r.txt': 0},
            "progress": -1, "lp": 0
            }

# This file is part of gx52.
#
# Copyright (c) 2018 Roberto Leinardi
#
# gx52 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gx52 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gx52.  If not, see <http://www.gnu.org/licenses/>.
from typing import Any


class DbChange:
    INSERT = 0
    DELETE = 1
    UPDATE = 2

    def __init__(self, entry: Any, change_type: int) -> None:
        self.entry: Any = entry
        self.type: int = change_type

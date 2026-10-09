# Copyright (c) 2019 Matt Martz <matt@sivel.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

import multiprocessing
import os

# Explicit multiprocessing context using the fork start method on POSIX.
# This exists as a compat layer now that Python3.8 has changed the default
# start method for macOS to ``spawn`` which is incompatible with our
# code base currently
#
# This exists in utils to allow it to be easily imported into various places
# without causing circular import or dependency problems
# Windows has no fork start method. Spawn makes the controller importable on
# Windows; execution paths that depend on inherited fork state must provide a
# serial alternative before native Windows task execution is supported.
context = multiprocessing.get_context('spawn' if os.name == 'nt' else 'fork')

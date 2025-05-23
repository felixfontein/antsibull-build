# Author: Felix Fontein <felix@fontein.de>
# Author: Toshio Kuratomi <tkuratom@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or
# https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Ansible Project, 2020
"""Helper to use pkgutil.get_data without having to check the return value."""

from __future__ import annotations

from importlib import resources


def get_antsibull_data(filename: str) -> bytes:
    """
    Retrieve data from the antsibull_build.data package as bytes.

    The filename can be a relative path separated with '/' to access subdirectories.
    See https://docs.python.org/3/library/pkgutil.html#pkgutil.get_data for details.
    """

    try:
        return resources.files("antsibull_build.data").joinpath(filename).read_bytes()
    except (ImportError, OSError) as exc:
        raise RuntimeError(
            f"Cannot find {filename} in the antsibull_build.data package"
        ) from exc

# coding: utf-8
# /*##########################################################################
# Copyright (C) 2016-2018 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ############################################################################*/

__authors__ = ["V. Valls"]
__license__ = "MIT"
__date__ = "19/07/2021"

from numpy.distutils.misc_util import Configuration


def configuration(parent_package='', top_path=None):
    config = Configuration('gui', parent_package, top_path)
    config.add_subpackage('test')
    config.add_subpackage('utils')
    config.add_subpackage('tasks')
    config.add_subpackage('model')
    config.add_subpackage('helper')
    config.add_subpackage('widgets')
    config.add_subpackage('dialog')
    config.add_subpackage('jupyter')
    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(configuration=configuration)

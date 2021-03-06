# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Module defining constants global to the product tests
"""

import os

import prestoadmin
from prestoadmin import main_dir

LOCAL_RESOURCES_DIR = os.path.join(prestoadmin.main_dir,
                                   'tests/product/resources/')

DEFAULT_DOCKER_MOUNT_POINT = '/mnt/presto-admin'
DEFAULT_LOCAL_MOUNT_POINT = os.path.join(main_dir, 'tmp/docker-pa/')

BASE_IMAGE_NAME = 'jdeathe/centos-ssh'
BASE_IMAGE_TAG = 'centos-6-1.2.0'

BASE_TD_IMAGE_NAME = 'teradatalabs/centos6-ssh-test'
BASE_TD_DOCKERFILE_DIR = os.path.join(LOCAL_RESOURCES_DIR, 'centos6-ssh-test')

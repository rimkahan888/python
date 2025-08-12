#!/usr/bin/env python3
"""
Personal Task Manager
A simple command-line application for managing personal tasks
Author: Your Name
Date: 2024
"""

import json
import os
from datetime import datetime, date
import sys

# Application constants
APP_NAME = "Personal Task Manager"
VERSION = "1.0.0"
DATA_FILE = "tasks.json"
#!/usr/bin/python3
"""Model that defines the Storage component"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connector:
    def __init__(self, conntype):
        if conntype == "PGContainer":
            self.conn = "postgresql+psycopg2://zyzzdb:zyzzpass@zyzzdb"
        elif conntype == "Test":
            self.conn = "sqlite:///:memory:"

        self.engine = create_engine(self.conn)
        self.connection = self.engine.connect()
        self.Session = sessionmaker()

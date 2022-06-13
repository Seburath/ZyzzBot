#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Boolean, Numeric
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    date = Column(String)

    gender = Column(String)
    height = Column(Integer)
    neck = Column(Integer)
    waist = Column(Integer)
    hip = Column(Integer)
    weight = Column(Integer)

    body_fat = Column(Integer)
    ffmi = Column(Integer)
    fat_score = Column(Integer)
    ffmi_score = Column(Integer)
    total_score = Column(Integer)

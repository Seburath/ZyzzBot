#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date, datetime
from dateutil import parser

from .model import Data, Base
from .connectors import Connector


class DBMan:
    """Database Manager for the Bot"""

    def __init__(self, conntype):
        connector = Connector(conntype)
        connector.Session.configure(bind=connector.engine)
        Base.metadata.create_all(connector.engine)

        self.session = connector.Session()

    def add_record(self, data):
        data = Data(
            user=data["user"],
            date=datetime.now(),
            gender=data["gender"],
            hip=data["hip"],
            weight=data["weight"],
            height=data["height"],
            neck=data["neck"],
            waist=data["waist"],
            body_fat=data["body_fat"],
            fat_score=data["fat_score"],
            ffmi=data["ffmi"],
            ffmi_score=data["muscle_score"],
            total_score=data["total_score"],
        )

        self.session.add(data)
        self.session.commit()

    def replace_last_record(self, data):
        query = (
            self.session.query(Data)
            .filter_by(user=data["user"])
            .order_by(Data.id.desc())
            .first()
        )

        query.user = (data["user"],)
        query.date = (datetime.now(),)
        query.gender = (data["gender"],)
        query.hip = (data["hip"],)
        query.weight = (data["weight"],)
        query.height = (data["height"],)
        query.neck = (data["neck"],)
        query.waist = (data["waist"],)
        query.body_fat = (data["body_fat"],)
        query.fat_score = (data["fat_score"],)
        query.ffmi = (data["ffmi"],)
        query.ffmi_score = (data["muscle_score"],)
        query.total_score = (data["total_score"],)

        self.session.commit()

    def get_datapoints(self, user):
        query = self.session.query(
            Data.date,
            Data.fat_score,
            Data.ffmi_score,
        ).filter_by(user=user)

        datapoints = {
            "date": [parser.parse(record.date) for record in query],
            "fat_score": [record.fat_score for record in query],
            "muscle_score": [record.ffmi_score for record in query],
        }

        return datapoints

    def get_last_record(self, user):
        query = (
            self.session.query(Data)
            .filter_by(user=user)
            .order_by(Data.id.desc())
            .first()
        )

        if query is not None:
            data = {
                "user": query.user,
                "date": query.date,
                "gender": query.gender,
                "hip": query.hip,
                "weight": query.weight,
                "height": query.height,
                "neck": query.neck,
                "waist": query.waist,
                "body_fat": query.body_fat,
                "fat_score": query.fat_score,
                "ffmi": query.ffmi,
                "muscle_score": query.ffmi_score,
                "total_score": query.total_score,
            }

            return data

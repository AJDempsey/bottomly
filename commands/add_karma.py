# coding=utf-8
from datetime import datetime

from commands.abstract_command import AbstractCommand
from config import Config
from model.karma import Karma


class AddKarmaCommand(AbstractCommand):

    def get_purpose(self):
        return "Awards an imaginary internet point to someone/something."

    def execute(self, awarded_to, awarded_by, reason, karma_type):
        self.config.connect_to_db()
        k = Karma(awarded_to_username=awarded_to,
                  reason=reason,
                  awarded_by_username=awarded_by,
                  awarded=datetime.now(),
                  karma_type=str(karma_type))

        k.save()
        return k

    def __init__(self):
        super(AddKarmaCommand, self)
        self.config = Config()

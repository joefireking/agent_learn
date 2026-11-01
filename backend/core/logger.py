import logging
import sys
import os
from backend.config import get_settings
class _Logger:
    def __init__(self,name:str):
        self._log=logging.getLogger(name)
    def _fmt(selfself,event:str,**kw):
        if kw:
            return event+"|"+" ".join(f"{k}={v!r}" for k,v in kw.items())
        return event
    def debug(self,event:str,**kw):
        self._log.debug(self._fmt(event,**kw))
    def info(self,event:str,*args,**kw):
        if args:
            self._log.info(event,*args)
        else:
            self._log.info(self._fmt(event,**kw))
    def error(self,event:str,**kw):
        exc_info=kw.pop("exc_info",False)
        self._log.error(event,exc_info=exc_info)
    def warning(self,event:str,*args,**kw):
        if args:
            self._log.warning(event,*args)
        else:
            self._log.warning(self._fmt(event,**kw))
    def critical(self,event:str,**kw):
        self._log.critical(self._fmt(event,**kw))
def configure_logging()->None:
    settings=get_settings()
    level=getattr(logging,settings.log_level.upper(),logging.INFO)
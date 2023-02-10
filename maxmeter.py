from dataclasses import dataclass
from typing import ClassVar
from datetime import datetime
from pytz import timezone
from json import dumps
from requests import post
from os import environ
from random import randrange

@dataclass
class MaxMeter:
    '''Class for increment a meter'''
    assetnum: str
    metername: str
    newreading: str
    newreadingdate: str = datetime.now(timezone('Europe/Berlin')).replace(microsecond=0).isoformat()
    isdelta: bool = True
    dorollover: bool = False
    orgid: ClassVar[str] = ''
    siteid: ClassVar[str] = ''
    remarks: ClassVar[str] = 'Zaehlerstand'
    apikey: ClassVar[str] = ''
    url: ClassVar[str] = ''
    inspector: ClassVar[str] = 'MAXADMIN'
    xmethodoverride: ClassVar[str] = 'BULK'

    @classmethod
    def position(cls, orgid, siteid):
        cls.orgid = orgid
        cls.siteid = siteid

    @classmethod
    def login(cls, apikey, url):
        cls.apikey = apikey
        cls.url = url + '/maximo/api/os/MXMETERDATA?lean=1'

    def getData(self):
        cls = MaxMeter
        result = {
                "assetnum": self.assetnum,
                "dorollover": self.dorollover,
                "inspector": cls.inspector,
                "isdelta": self.isdelta,
                "metername": self.metername,
                "newreading": self.newreading,
                "newreadingdate": self.newreadingdate,
                "orgid": cls.orgid,
                "remarks": self.remarks,
                "siteid": cls.siteid
            }
        prefix =  '[ { "_meta": {"method": "SYNC"}, "_data": '
        suffix =  ' } ]'
        return prefix + dumps(result) + suffix
    
    def getHeaders(self):
        cls = MaxMeter
        return {'apiKey': cls.apikey, 'x-method-override': self.xmethodoverride}

    def post(self):
        cls = MaxMeter
        return post(cls.url, data=self.getData(), headers=self.getHeaders(), verify=(environ['APP_VERIFY']=='True')) 

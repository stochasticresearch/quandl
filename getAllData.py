#!/usr/bin/env python

import quandl

class DataDownloader:
    def __init__(self):
        with open('api_key', 'r') as myfile:
            api_key=myfile.read().replace('\n', '')
        quandl.ApiConfig.api_key = api_key
        self.dbAll = None

    def getAllDatabases(self):
        self.dbAll = []

        self.dbAll = quandl.Database.all()
        # get all pages of data
        numPages = dbAll.meta['total_pages']
        numRemainingPages = numPages
        pageNum = 2
        for pageNum in range(2,numRemainingPages+1):
            databases = quandl.Database.all(params={'page': pageNum })
            self.dbAll.extend(databases)

    def filter(self, filters):
        if(self.dbAll==None):
            self.getAllDatabases()

        dbsFiltered = []
        keys = filters.keys()
        vals = filters.values()
        for ii in range(0,len(self.dbAll)):
            match = True
            db = self.dbAll[ii]
            for jj in len(filters):
                try:
                    if(db[keys[jj]]!=vals[jj]):
                        match = False
                except:
                    match = False
            if(match):
                dbsFiltered.extend(db)


if __name__=='__main__':
    dd = DataDownloader()
    freeDbFilter = {'premium':False}
    freeDbs = dd.filter(freeDbFilter)
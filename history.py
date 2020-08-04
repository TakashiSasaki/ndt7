#!/usr/bin/python3
import sys, os, re, datetime, os.path, json

class File():
    __slots__ = [ "dirpath", "filename", "datetime", "lastline", "downloadValue", "downloadUnit", "uploadValue", "uploadUnit",  "minRttValue", "minRttUnit", "downloadRetransValue", "downloadRetransUnit" ]

    def __init__(self, dirpath, filename):
        self.dirpath = dirpath
        self.filename = filename
        m = re.match("([0-9-]+T[0-9:+]+).json", filename)
        if m is None: 
            raise RuntimeError("not ISO8601 string")
        self.datetime = datetime.datetime.fromisoformat(m[1])
        f = open(os.path.join(self.dirpath, self.filename))
        lines = f.readlines()
        self.lastline = lines[len(lines)-1]
        o = json.loads(self.lastline)
        self.downloadValue = o["Download"]["Value"]
        self.downloadUnit= o["Download"]["Unit"]
        self.uploadValue = o["Upload"]["Value"]
        self.uploadUnit= o["Upload"]["Unit"]
        self.minRttValue= o["MinRTT"]["Value"]
        self.minRttUnit= o["MinRTT"]["Unit"]
        self.downloadRetransValue= o["DownloadRetrans"]["Value"]
        self.downloadRetransUnit= o["DownloadRetrans"]["Unit"]

    def toCsv(self):
        return self.dirpath + "," + self.filename + "," + str(self.datetime.timestamp()) + "," + str(self.downloadValue) + "," + self.downloadUnit + "," + str(self.uploadValue) + "," + self.uploadUnit + "," + str(self.minRttValue) + "," + self.minRttUnit + "," + str(self.downloadRetransValue) + "," + self.downloadRetransUnit
        pass

class Files(list):
    def __init__(self, dirpath):
        dirs = os.listdir(dirpath)
        for x in dirs:
            try: 
                f = File(dirpath, x)
                self.append(f)
            except RuntimeError:
                continue
            except KeyError:
                continue
    def toCsv(self):
        lines = [ x.toCsv() for x in self ]
        return "dirpath,filename,datetime,downloadValue,downloadUnit,uploadValue,uploadUnit,minRttValue,minRttUnit,downloadRetransvalue,downloadRetransUnit\n" + "\n".join(lines)

if __name__ == "__main__":
    files = Files(sys.argv[1])
    print(files.toCsv())


import os,sys,stat,commands

def findfile():
	f = '1.txt'
	mode = stat.S_IMODE(os.lstat(f)[stat.ST_MODE])
	print(f)

        for level in "USR", "GRP", "OTH":
            for perm in "R", "W", "X":
                if mode & getattr(stat,"S_I"+perm+level):
                    print level, " has ", perm, " permission"
                else:
                    print level, " does NOT have ", perm, " permission"

findfile()

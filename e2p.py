import argparse
import os
import re


def uselessFile(entryName):
    return entryName in ['@eaDir', '.DS_Store', '.@__thumb']


def ren2plex():
    for index, filename in enumerate(os.listdir(ARGS.dir)):
        if uselessFile(filename):
            continue
        
        if os.path.isdir(filename):
            for subfile in os.listdir(os.path.join(ARGS.dir, filename)):
                m = re.search(r'(.*)\[tmdb(id)?\=(\d+)\](.*$)', subfile, flags=re.A | re.I)
                if m:
                    newsubname = '%s {tmdb-%s}%s' % (m[1].strip(), m[3], m[4])
                    print('   %s ==> %s ' % (subfile, newsubname))
                    os.rename(os.path.join(ARGS.dir, filename, subfile), os.path.join(ARGS.dir, filename, newsubname))

        m = re.search(r'(.*)\[tmdb(id)?\=(\d+)\]', filename, flags=re.A | re.I)
        if m:
            newname = '%s {tmdb-%s}' % (m[1].strip(), m[3])
            print('%d %s ==> %s ' % (index, filename, newname))
            os.rename(os.path.join(ARGS.dir, filename), os.path.join(ARGS.dir, newname))



def loadArgs():
    global ARGS
    parser = argparse.ArgumentParser(description='rename emby folder to plex folder.')
    parser.add_argument('dir', help='folder path.')
    ARGS = parser.parse_args()

def main():
    loadArgs()
    ren2plex()


if __name__ == '__main__':
    main()
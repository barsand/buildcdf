#!/usr/bin/python3
import sys

HEIGHT_STEP = 0.00001


def buildcdf(values, outpath=None):
    values = sorted([float(i) for i in values])
    last_v = values[0]
    result = list()
    cnt = 1

    for curr_v in values[1:]:
        if curr_v != last_v:
            assert not result or last_v > result[-1][0], 'input not sorted'
            result.append([last_v, cnt])
            cnt += 1
        else:
            cnt += 1
        last_v = curr_v

    if not result:
        result.append([0.0, 0.0])
    result.append([last_v, cnt])

    cdf = list()

    h = HEIGHT_STEP
    i = 0
    while i < len(result):
        x, y = result[i][0], float(result[i][1])/cnt
        while y < h:
            i += 1
            x, y = result[i][0], float(result[i][1])/cnt
        cdf.append((x, y))
        while y >= h:
            h += HEIGHT_STEP
        i += 1
    cdf.append((result[-1][0], 1.0))

    if outpath is not None:
        f = open(outpath, 'w')
        f.write('\n'.join(['%f %f' % i for i in cdf]))
        f.close()
    return cdf


if __name__ == '__main__':
    values = list()
    f = sys.stdin
    line = f.readline()
    while line:
        values.append(float(line.rstrip()))
        line = f.readline()
    for dx, dy in buildcdf(values):
        print(dx, dy)
    sys.exit(0)

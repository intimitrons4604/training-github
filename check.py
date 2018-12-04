import re
import sys

DIFFERENCE_FILE_NAME = 'differences.txt'
SUM_FILE_NAME = 'sums.txt'

DIFFERENCE_PATTERN = '(-?\d+) *?- *?(-?\d+) *?= *?(-?\d+)'
SUM_PATTERN = '(-?\d+) *?\+ *?(-?\d+) *?= *?(-?\d+)'


def open_file(name):
    return open(name, mode='r', encoding='utf_8')


def check_differences():
    okay = True
    good_lines = 0
    bad_lines = 0

    pattern = re.compile(DIFFERENCE_PATTERN)

    line_number = 0
    with open_file(DIFFERENCE_FILE_NAME) as file:
        for line in file:
            line_number = line_number + 1
            line = line.strip()

            if not line:
                continue

            match = pattern.match(line)

            if match is None:
                print("%s:%d Line is not in expected format" % (DIFFERENCE_FILE_NAME, line_number))
                okay = False
                bad_lines = bad_lines + 1
                continue

            a = int(match.group(1))
            b = int(match.group(2))
            file_difference = int(match.group(3))

            actual_difference = a - b

            if actual_difference != file_difference:
                print("%s:%d Incorrect difference. File=%d Actual=%d" %
                      (DIFFERENCE_FILE_NAME, line_number, file_difference, actual_difference))
                okay = False
                bad_lines = bad_lines + 1
                continue

            good_lines = good_lines + 1

    print('check_differences(): %d lines okay, %d lines bad' % (good_lines, bad_lines))
    return okay


def check_sums():
    okay = True
    good_lines = 0
    bad_lines = 0

    pattern = re.compile(SUM_PATTERN)

    line_number = 0
    with open_file(SUM_FILE_NAME) as file:
        for line in file:
            line_number = line_number + 1
            line = line.strip()

            if not line:
                continue

            match = pattern.match(line)

            if match is None:
                print("%s:%d Line is not in expected format" % (SUM_FILE_NAME, line_number))
                okay = False
                bad_lines = bad_lines + 1
                continue

            a = int(match.group(1))
            b = int(match.group(2))
            file_sum = int(match.group(3))

            actual_sum = a + b

            if actual_sum != file_sum:
                print("%s:%d Incorrect sum. File=%d Actual=%d" %
                      (SUM_FILE_NAME, line_number, file_sum, actual_sum))
                okay = False
                bad_lines = bad_lines + 1
                continue

            good_lines = good_lines + 1

    print('check_sums(): %d lines okay, %d lines bad' % (good_lines, bad_lines))
    return okay


difference_okay = check_differences()
sums_okay = check_sums()

success = difference_okay and sums_okay
if not success:
    print('Check failed')
    sys.exit(1)
else:
    print('Check passed')

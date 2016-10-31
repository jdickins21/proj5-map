"""
Test program for pre-processing schedule
"""

def process(raw):
    """
    Line by line processing of syllabus file.  Each line that needs
    processing is preceded by 'head: ' for some string 'head'.  Lines
    may be continued if they don't contain ':'.  If # is the first
    non-blank character on a line, it is a comment ad skipped. 
    """
    field = None
    entry = { }
    cooked = [ ]
    week = 0
    for line in raw:
        if len(line) == 0:
            continue
        parts = line.split(',')
        print("lat: " + parts[0] + " " + "lng: " + parts[1])

        cooked.append(parts)

    return cooked

def main():
    f = open("data/loaction.txt")
    parsed = process(f)
    print(parsed)

if __name__ == "__main__":
    main()
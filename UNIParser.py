import urllib
import MLStripper

class UNIParser(object):
    """
    Parses Columbia's directory. Pretty slow
    """

    URL = "https://directory.columbia.edu/people/uni?code="
    # this is not all the categories, add into list as needed
    CATEGORIES = [  "Title", 
                    "Department", 
                    "Address", 
                    "Home Addr",
                    "Campus Tel",
                    "Tel",
                    "UNI",
                    "Email"]

    def __init__(self):
        self.raw = []
        self.uni_data = {}

    def feed(self, uni):
        uni_HTML = urllib.urlopen(self.URL + uni).read()
        uni_stripped = MLStripper.strip_tags(uni_HTML)
        self.raw = uni_stripped.split(":")

    def process(self):
        # remove extraneous elements
        del self.raw[0]
        del self.raw[-1]
        
        # remove extraneous strings before the name
        name = self.raw[0].split()
        name = name[name.index("Page")+1:]
        self.raw[0] = " ".join(name)
        
        # strip last word of last lement "email" because email is not received from the html
        self.raw[-1] = self.strip_last_words(self.raw[-1], 1)
        # populate the dictionary
        for x in range(len(self.raw)-1, 0, -1):
            for compare in self.CATEGORIES:
                c = compare.split(" ")
                # the last len(compare) words 
                key = " ".join(self.raw[x-1].split(" ")[-len(c):])
                if compare == key:
                    self.raw[x-1] = self.strip_last_words(self.raw[x-1], len(c))
                    # strip leading whitespace
                    self.uni_data[key] = self.raw[x].lstrip()
                    break

        # adds name
        self.uni_data["Name"] = self.raw[0]

    def strip_last_words(self, s, n):
        """
        Strips last n number of words in a string
        """
        words = s.split(" ")
        del words[-n:]
        return " ".join(words)

def get_student_info(uni):
    """
    Returns student information
    """
    p = UNIParser()
    p.feed(uni)
    p.process()
    return p.uni_data
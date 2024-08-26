import textwrap

def wrap(string, max_width):
    ans= textwrap.fill(string,max_width)
    return ans

if __name__ == '__main__':

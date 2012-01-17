import os

from easyprocess import EasyProcess

from slideshow.models import DBSession
from slideshow.models import MyModel

class to_html(object):
    def __init__(self, content):
        self.html = content
    def __html__(self):
        return self.html

def my_view(request):
    out = 's5'
    path = '../community.md'
    try:
        with file(path) as f:
            pass
        command = ['pandoc', '-f markdown', '-i', '-w', out, '-s', path]
        command = ' '.join(command)
        pandoc = EasyProcess(command).start().wait()
        result = pandoc.stdout
    except Exception, e:
        result = str(e)
        result += "<br>"
        for f in os.listdir('.'):
            if f.endswith('.org'):
                result += """<a href="%s">%s</a><br>""" % (f, f)

    h = to_html(result)
    return {'title':"""\
If you don't know SSH, then you don't know IT!
""", 'content': h}

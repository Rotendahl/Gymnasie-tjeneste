# Password to use for web authentication
print "\n\n\n\n HEJSA \n\n\n"

c = get_config()

# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always

# Notebook config
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = True
c.NotebookApp.password = u'sha1:309896beb51d:fdbec23ebe5710eae1efbd99b5b0dc89fa36c507'
# It is a good idea to put it on a known, fixed port
c.NotebookApp.port = 1337


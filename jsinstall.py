from JumpScale import j

j.do.execute("python3 setup.py build")
j.do.execute("rm -rf %s/ptpdb/*"%j.do.getPythonLibSystem())

j.do.copyTree("build/lib/", dest=j.do.getPythonLibSystem(), keepsymlinks = False, deletefirst = False, overwriteFiles=True,rsync=False,recursive=True)


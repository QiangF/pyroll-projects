#!/usr/bin/python

from sultan.api import Sultan
from os import path
s = Sultan()

repos="""
pyroll-core
pyroll-freiberg-flow-stress
pyroll-wusatowski-spreading
pyroll-cli
pyroll-lendl-equivalent-method
pyroll-basic
pyroll-marini-spreading
pyroll-report
pyroll-docs
pyroll-sander-spreading
pyroll-hill-spreading
pyroll-sparling-spreading
pyroll-export
pyroll-plugin-template
pyroll-integral-thermal
pyroll-hensel-power-and-labour
pyroll
pyroll-zouhar-contact
pyroll-roux-spreading
pyroll-sims-power-and-labour
pyroll-hitchcock-roll-flattening
pyroll-project.github.io
pyroll-work-roll-elastic-deformation
pyroll-pub1-benchmark
"""

for r in repos.split():
     repo_link = "git@github.com:pyroll-project/" + r + ".git"
     if path.exists(r):
          print("can't overwrite' path {}".format(repo_link))
     else:
         print("adding submodule {}".format(repo_link))
         s.git("submodule", "add", "--depth", "1", "--",  repo_link).run()

def link(i, j):
    destination = "pyroll-{}/pyroll/{}".format(i,j)
    print("processing {}".format(destination))
    if path.exists(destination):
         print("making symlink")
         s.ln("-sf", "./submodules/" + destination, "../" + j).run()

for i in ["core",
          "report",
          "pyroll-basic",
          'lendl-equivalent-method',
          "freiberg-flow-stress",
          "integral-thermal"]:
     j=i.replace("-","_")
     link(i, j)

for i in ["pyroll-basic", ]:
     j=i.replace("pyroll-","") + '.py'
     k=i.replace("pyroll-","")
     link(k, j)

for i in ["hensel-power-and-labour",
          "wusatowski-spreading",
          "hitchcock-roll-flattening"]:
     j=i.replace("-","_") + '.py'
     link(i, j)

s.ln("-sf", "./submodules/pyroll-pub1-benchmark/pyroll_pub1_benchmark", "../benchmark").run()

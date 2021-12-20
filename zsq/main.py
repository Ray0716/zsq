import time
import os
import sys
import getpass
import re
import string
import click
from database import *
from console import *


red = "\033[0;91m"
w = "\033[0;37m"
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
bold = '\033[1m'
end = '\033[0m'
pink = '\033[95m'


# file errors
class nonexistantfilepath(Exception):
  pass
class nonzsqfile(Exception):
  pass


fp = input('filepath: ')

if '.zsq' in fp:
  try:
    f = open(f'{fp}')
  except:
    raise nonexistantfilepath("no such file exists!")
else:
  raise nonzsqfile("the file isn't a '.zsq' file!")


# os.system("clear")
# print("z^2 0.1.0 (default, Dec 13 2021, "+time.strftime("%H:%M:%S")+")")


content = f.read()
colist = content.split("\n")
load = 0
# for i in colist:
#     if i:
#         load += 1

# console()

# num = 0
# os.system("clear")
# print("Compiling script")
# time.sleep(1)
# os.system("clear")
# while num < load:
#     print("Compiling... /")
#     time.sleep(0.08)
#     os.system("clear")
#     print("Compiling... -")
#     time.sleep(0.08)
#     os.system("clear")
#     print("Compiling... \ ")
#     time.sleep(0.08)
#     os.system("clear")
#     num += 1
os.system("clear")


def check():
    df = re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+", lines)
    df = str(df)

"""
def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
    mustend = time.time() + timeout
    while time.time() < mustend:
      if somepredicate(*args, **kwargs): return True
      time.sleep(period)
    return False
"""

allvars = {}
line = 0
read_line = 0
PASS = False
getChar1 = "none"
getChar2 = "none"
getChar3 = "none"
var1 = "Undefined variable"
input1 = "Undefined input"
input2 = "Undefined input"
input3 = "Undefined input"
functions = ["print(", "prompt(", "time.time(", "time.rest("]

def error(the_error):
  print(red + bold + f"line {str(line)}: {code}\n{the_error}" + w)

def timeTime():
  if time_module == 1:
        wrd = "time.time("
        res = lines.partition(wrd)[2]
        try:
          res = res.replace(")", "")

          if res != "" or res != " ":
            error("no arguments must be made inside of the function time.time!")
            exit()
          else:
            return time.time()
        except:
          error("an error occurred while trying to time.time!")
          exit()
  else:
        error("the 'time' module isn't imported or it doesn't exist!")
        exit()

def Print():#add f'string
  #try:
    if '")' in lines or "')" in lines or ")" in lines:
      wrd = "print("
      res = lines.partition(wrd)[2]
      res2 = lines.partition(wrd)[2]
      # print(res)
      if res[-3] == "\"" and res[0] == "\'" or res[-3] == "'" and res[0] == "\"":
        for i in functions:
          if i in res:
            pass
        else:
          error("the 'print' starting quotations and ending quotations are different!")
          exit()
      else:
        res = res.replace("\")","")
        res = res.replace('\')',"")
        res = res.replace("\\n", "\n")
        res = res.replace("\\t", "\t")
        if "\"" in res:
          split_string = res.split("\")", -1)
        elif "'" in res:
          split_string = res.split("\')", -1)
        else:
          for i in functions:
            if i in res2:
              pass
            else:
              error("the 'print' function is missing quotations!")
              exit()
          
        res = split_string[0]
        
        # print(res)
        # print(res[0])
        
        if res[0] == "^": # This allows variables to be referenced inside quotations, like f' strings
          sq_str = True
        else:
          sq_str = False
        res = res.replace("\")","")
        res = res.replace('\')',"")
        res = res.replace("\\n", "\n")
        res = res.replace("\\t", "\t")
        res = res.replace("\\)", ")")
        res = res.replace("\\(", "(")
        res = res.replace('\\"', '"')
        res = res.replace("\\'", "'")
        # colors: res = res.replace("{red}", red)
        res = res.replace('"', "")
        res = res.replace("'", "")
        # res = res.replace(")","")
        
        if sq_str:
          if "{" in res:
            if "}" in res:
              start = "{"
              end = "}"
              check = res[res.find(start) + len(start):res.rfind(end)]
              # print(check)
              # print(allvars)
              if check in allvars:
                # print(check)
                res = res.replace("{", "")
                res = res.replace("}", "")
                dffdfdfdf = allvars[check]
                res = res.replace(check, str(dffdfdfdf))
              else:
                global PASS
                PASS = False
                if "time.time(" in check:
                  # print(check)
                  # print(res)
                  timeTime()
                else:
                  error(f"'{varname}' variable does not exist!")
                  exit()
        if PASS:
          pass
        else:
          try:
            res = res.replace("^", "")
          except:
            pass
          print(res, end="")
          print()
    else:
      error("the 'print' statement must have a closing \")\"!")
      exit()
  #except:
    #print(bold + red + "the 'print' statement must have a closing \")\"!" + w)
    #exit()



newvar = 0
time_module = 0
file = open(fp)
readline2 = 0
for lines in file.readlines():
    if readline2 == 1:
      readline2 = 0
      continue
    if "//" in lines:
      readline2=1
    
    lines = lines.replace('\n','')
    lines = lines.replace('\t','')
    code = lines

    #print(lines)
    # print(lines)

    if lines == '': 
      pass
    """
    elif "/#" in lines:
      wait_until("#/", 0)
      readline2 = 1"""
    if "//" in lines:
      pass
    lines = lines.rstrip()

    # print(lines[:2])
    
    if lines[:2] == "//":
      pass
      read_line = 0
    elif "//" in lines:
      try:
        e = lines.find("//")
        if e != -1:
          lines = lines[:e]
      except:
        pass
    elif "import(\"time\")" in lines or "import('time')" in lines:
      time_module = 1
    elif "import(\"os\")" in lines or "import('os')" in lines:
      os_module = 1

    elif "var " in lines:
      wrd = "var "
      newvar = lines.partition(wrd)[2]
      split_string = newvar.split("\")", -1)
      newvar.replace(")","")
      newvar.replace('\"', '')
      newvar = split_string[0]
      #newvar = variable;
      # print(newvar)
      
      if " " in newvar:
        find_space = newvar.find("\"")
        if find_space == -1:
          find_space1 = newvar.find("\'")
          if find_space1 == -1:
            for i in newvar:
              if i in ["1","2","3","4","5","6","7","8","9","0"]:
                newvar_type = int
              else:
                if newvar in ["true", "false"]:
                  newvar_type = bool
                else:
                  error("variables must be named!")
                  exit()
          else:
            newvar_type = str
        else:
          newvar_type = str
        if find_space != -1:
          newvar2 = newvar[find_space:]
        else:
          if find_space1 != -1:
            newvar2 = newvar[find_space:]
          else:
            error("there was an error with encountering the variable! try again!")
            exit()
        
        newvar2 = newvar2.replace(" ", "")
        # print(newvar)
        e = newvar.find("=")
        if e != -1:
          varname = newvar[:e]
          varname = varname.replace(" ", "")
          VALUE = newvar[e:]
        # print(varname)
        # print(abc)
        # print(newvar2)

        # print(newvar[-1])

        if "=" in newvar:
          idk = []
          Continue = True
          for i in newvar:
            if Continue:
              if i == "=":
                idk.append(i)
                Continue = False
              else:
                idk.append(i)
            else:
              if i == " ":
                idk.append(i)
                break
              else:
                break
          idk = "".join(idk)
          newvar = newvar.replace(idk, "")

          # print(newvar)
          # print(varname)
          # print(newvar)

          for f in functions:
            if f in newvar:
              FUNC = True
              if "print(" in newvar:
                Print()
              elif "prompt(" in newvar:
                global value
                # print("im idiot")
                wrd = "prompt("
                var = lines.partition(wrd)[2]
                split_string = var.split(")", -1)
                var = var.replace(')','')
                var = var.replace('\"',"")
                var = var.replace('\'',"")
                var = var.replace("\\n", "\n")
                var = var.replace("\\t", "\t")
                var = var.replace("\\)", ")")
                var = var.replace("\\(", "(")
                var = var.replace('\\"', '"')
                var = var.replace("\\'", "'")
                # var = var = split_string[0]
                # var = var.strip(")")
                
                value = input(var)
                # print(value)
                allvars[varname] = value
                # print(value)
                

                # print(value)
                # print(allvars)
                # print(allvars[varname])
                
                FUNC = True

          
          if "'" in newvar or "\"" in newvar:
              if newvar[-1] == "'" and newvar[0] == "'" or newvar[-1] == "\"" and newvar[0] == "\"":
                newvar = newvar.replace(newvar[-1], "")
                #newvar = newvar.replace(newvar[0], "")
              else:
                try:
                  if FUNC == True:
                    pass
                except:
                  error("starting quotations and end quotations must be the same!")
                  exit()
              allvars[varname] = newvar
              # print(allvars)
          elif newvar == "true":
            allvars[varname] = True
          elif newvar == "false":
            allvars[varname] = False
          else:
            error("variables must be named after there is a equal sign!")
            exit()
        else:
          try:
            if FUNC:
              pass
          except:
            error("variables cannot include spaces!")
            exit()
        # print(newvar)
      
    elif "prompt(" in lines:
      wrd = "prompt("
      var = lines.partition(wrd)[2]
      split_string = var.split(")", -1)
      var = var.replace(')','')
      var = var.replace('\"',"")
      var = var.replace('\'',"")
      var = var.replace("\\n", "\n")
      var = var.replace("\\t", "\t")
      var = var.replace("\\)", ")")
      var = var.replace("\\(", "(")
      var = var.replace('\\"', '"')
      var = var.replace("\\'", "'")
      # var = var = split_string[0]
      # var = var.strip(")")
      
      input(var)

      """
      if var in allvars:
        # var = input()
        # input()
        # allvars[varname] = var
      else:
        if var not in allvars:
          print(bold + red + f"'{var}' variable does not exist!" + w)
          exit()
        else:
          pass
      """


    elif "print(" in lines:
      Print()
    
    elif "whatif " in lines:
      pass

    elif "time.rest(" in lines:
      if time_module == 1:
        wrd = "time.rest("
        res = lines.partition(wrd)[2]
        try:
          res = res.replace(")","")
          for i in res:
            if i in ["1","2","3","4","5","6","7","8","9","0"]:
              time.sleep(int(res))
            else:
              error("strings cannot be inside integer values!")
              exit()
        except:
          error("an error occurred while trying to time.rest!")
          exit()
      else:
        error("the 'time' module isn't imported or it doesn't exist!")
        exit()
    elif "time.time(" in lines:
      pass

    else:
      if lines in string.whitespace:
        pass
      else:
        error(f"{lines} is not defined!")
        exit()

    line+=1
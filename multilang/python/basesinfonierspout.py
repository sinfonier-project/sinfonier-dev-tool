#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import traceback

MarkEmit = "EMIT:"
MarkKill = "-ModuleFinishMark-"

class BaseSinfonierSpout():

  def __init__(self):

    pass
    
  def initialize(self):

    self.config = dict()
    self.d = dict()
    self.dinput = dict()
    self.it = 0
    self.itmax = int(sys.argv[3])
    if self.itmax == 0:
        self.itmax = float("inf")

    # Parse module.properties
    moduleproperties = str(sys.argv[1])
    try:
      for line in open(moduleproperties).read().splitlines():
        self.config[line.split("=")[0]] = line.split("=")[1]
    except:
      self.log("Error parsing module.properties file, maybe it hasn't a valid format. key=value") 

    # Parse input.json
    inputjsonfile = str(sys.argv[2])
    try:
      self.dinput = json.loads(open(inputjsonfile).read())
    except:
      self.log("Error parsing input.json file, maybe it's not a valid JSON format")   
 
  def log(self,msg):

    print msg
    sys.stdout.flush()

  def getParam(self, param):

    if param in self.config.keys():
        return self.config[param]
    else:
        return ""

  def usernextTuple(self):

    raise NotImplementedError("update: This method must be implemented in your class")

  def useropen(self):

    raise NotImplementedError("update: This method must be implemented in your class")

  def userclose(self):

    raise NotImplementedError("update: This method must be implemented in your class")

  def addField(self,s,o):
    
    self.log("Added field '"+str(s)+"' with value: "+str(o))
    self.d[s] = o

  def getField(self,s):
    
    return self.getNestedField(s) if "." in s else self.d[s]

  def removeField(self,s):
    
    del self.d[s]

  def getNestedField(self,s):

    value = self.d.copy()
    for part in s.split("."):
      if type(value[part]) == "dict":
        value = json.loads(value[part])
      else:
        value = value[part]
    return value

  def existsField(self,s):
    
    return True if s in self.d.keys() else None

  def run(self):
    
    try:
        self.initialize()
        self.useropen()
        # Maximum iterations specified
        while self.it < self.itmax:
            # Reset input JSON
            self.d = self.dinput.copy()
            self.usernextTuple()
        self.userclose()
        print MarkKill
        sys.stdout.flush()
    except:
        print traceback.format_exc()

  def emit(self):
    
    self.log("Result tuple: "+json.dumps(self.d))
    print MarkEmit+json.dumps(self.d)
    sys.stdout.flush()
    self.it = self.it + 1
    
  def getJson(self):
      
    return self.d

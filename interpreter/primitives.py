"""

This file defines classes for the primitives provided by the attack 
specification language. Every class includes a method that returns 
an XML block related to a primitive execution.

"""

__author__ = "Alessandro Pischedda, Marco Tiloca"
__email__ = "alessandro.pischedda@gmail.com, marco.tiloca84@gmail.com"

import sys

# Wrong number of arguments
def error_arguments(name, ex_number, g_number):
    """Return the string which contains the error message"""

    sys.exit('Error: %s() takes exactly %d arguments ( %d given )' 
              %(name, ex_number, g_number))



class Clone:
    """Return the XML version of clone(srcPacketName, dstPacketName)"""	

    name = "Clone"
    argv = []
    argc = 2 # Expected number of arguments

    def __init__(self, args):
        self.argv = args.split(':')

    def __str__(self):
        if self.argc != len(self.argv):
            error_arguments(self.name, self.argc, len(self.argv))
        xml = ('\t<action>\n\t\t<name>Clone</name>\n\t\t<parameters>packetName:'
               '%s:newPacketName:%s</parameters>\n\t</action>'%(self.argv[0], 
               self.argv[1]))
        
        return xml

	
class Send:
    """Return the XML version of send(packetName, delay)"""

    name = "Send"
    argv = []
    argc = 2

    def __init__(self, args):
        self.argv = args.split(":")

    def __str__(self):
        if self.argc != len(self.argv):
            error_arguments(self.name, self.argc, len(self.argv))

        xml = ('\t<action>\n\t\t<name>Send</name>\n\t\t<parameters>packetName:'
               '%s:delay:%s</parameters>\n\t</action>' % (self.argv[0], 
               self.argv[1]))

        return xml



class Drop:
    """Return the XML version of drop(packetName)"""

    name = "Drop"
    argv = []
    argc = 1

    def __init__(self, args):
        self.argv = args.split(":")

    def __str__(self):
        if self.argc != len(self.argv):
            error_arguments(self.name, self.argc, len(self.argv))

        xml = ('\t<action>\n\t\t<name>Drop</name>\n\t\t<parameters>packetName:'
               '%s</parameters>\n\t</action>' % (self.argv[0]))

        return xml


class Move:
    """
    Return the XML version of move(x, y, z).
    Node(s) and occurrence time are not stored in this object.
    """
    argv = []
    argc = 3	
    name = "Move"

    def __init__(self, args):
        self.argv = args.split(":")

    def __str__(self):
        if self.argc != len(self.argv):
            error_arguments(self.name, self.argc, len(self.argv))
		
        coordinates = self.argv[0]+":"+self.argv[1]+":"+self.argv[2]
        
        xml = ('\t<action>\n\t\t<name>Move</name>\n\t\t<parameters>%s'
              '</parameters>\n\t</action>' % (coordinates))

        return xml


class Destroy:
    """Return the XML version of destroy().
        --- Node(s) and occurrence time are not stored in this object.
    """
    def __str__(self):
		
        xml = "\t<action>\n\t\t<name>Destroy</name>\n\t</action>"

        return xml


class Change:
    """
    Return the XML version of change(packet, field, newContent).
   	The field format is layer.field 
   	The layer can be APP, MAC, and ROUTING or NET
   	Possible field names are related to the particular layer
    """
	
    argv = []
    argc = 3
    name = "Change"

    def __init__(self, args):
        self.argv = args.split(":")

    def __str__(self):
        if self.argc != len(self.argv):
            error_arguments(self.name, self.argc, len(self.argv))
			
        field = self.argv[1].replace('"', "")
		
        xml = ('\t<action>\n\t\t<name>Change</name>\n\t\t<parameters>'
               'packetName:%s:field_name:%s:value:%s</parameters>\n\t</action>'
              % (self.argv[0], field, self.argv[2]))

        return xml


class Retrieve:
    """
    Return the XML version of retrieve(packet, field , variable).

    The field format is layer.field 
    	
   	The layer can be APP, MAC, and ROUTING or NET
   	Possible field names are related to the particular layer
   	The third parameter must be a variable
    """
	
    argv = []
    argc = 3
    name = "Retrieve"

    def __init__(self, args):
        self.argv = args.split(":")

    def __str__(self):
        if self.argc != len(self.argv):
            error_arguments(self.name, self.argc, len(self.argv))

        field = self.argv[1].replace('"', "")
		
        xml = ('\t<action>\n\t\t<name>Retrieve</name>\n\t\t<parameters>'
               'packetName:%s:field_name:%s:varName:%s</parameters>\n\t'
               '</action>' % (self.argv[0], field, self.argv[2]))

        return xml


class Put:
    """
    Return the XML version of 
    put(packet, dstNodes, direction, updateStat, delay).
    dstNodes is a list of node IDs, separated by the char '|'
    """	

    argv = []
    argc = 5
    name = "Put"

    def __init__(self, args):
        self.argv = args.split(":")

    def __str__(self):
        if self.argc != len(self.argv):
            error_arguments(self.name, self.argc, len(self.argv))

        xml = ('\t<action>\n\t\t<name>Put</name>\n\t\t<parameters>packetName:'
               '%s:nodes:%s":direction:%s:throughWC:%s:delay:%s</parameters>'
               '\n\t</action>' % (self.argv[0], self.argv[1], self.argv[2],
               self.argv[3], self.argv[4]))

        return xml



class Create:
    """
    Return the XML version of 
    create(packet, layer1.type, value1, layer2.type, value2, ...)
    """

    argv = []
    argc = 7 # at most
    name = "Create"

    def __init__(self, args):
        self.argv = args.split(":")

    def __str__(self):
        if len(self.argv) < 3:
            error_arguments(self.name, self.argc, len(self.argv))

        xml = ('\t<action>\n\t\t<name>Create</name>\n\t\t<parameters>'
               'packetName:%s' % (self.argv[0]))		
		
        i = 1 # Skip the first argument, i.e. the packet name
        while i < len(self.argv):
            # Remove '"' from string arguments
            field = self.argv[i].replace('"',"")
            xml = xml + ":" + field
            i = i + 1
		
        xml = xml + "</parameters>\n\t</action>"

        return xml


class Expression:
    """
    Handle an expression and return its XML version
    """

    expr = ""

    def __init__(self, expression):
        self.expr = expression

    def __str__(self):
        xml = "\t<action>\n\t\t<name>Expression</name>"
        xml = xml + self.expr
        xml = xml + "\n\t</action>"
        return xml

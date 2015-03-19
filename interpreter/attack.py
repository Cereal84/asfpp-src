"""
This file defines classes for the three kinds of attacks ammitted by the 
attack specification language. Every class includes a method that returns 
 an XML block related to the attack execution.
"""

__author__ = "Alessandro Pischedda, Marco Tiloca"
__email__ = "alessandro.pischedda@gmail.com, marco.tiloca84@gmail.com"

class PhysicalAttack:
    """Return a string in XML format which contains all the Physical 
    attacks"""

    time = "" # attack occurrence time
    nodes = "" # list of involved nodes
    stmts = [] # list of actions

    # t - time , n - nodes, s - statements
    def __init__(self, t, n, s):
        self.time = t
        self.nodes = n
        self.stmts = list(s)

    def __str__(self):
        xml = '''\n<Attack>\n\t<start_time>%s</start_time>
                \n\t<node>%s</node>''' %(self.time, self.nodes)

        for stmt in self.stmts:
            xml = xml +'\n%s' %(str(stmt))

        xml = xml+'\n</Attack>\n'

        return xml


class ConditionalAttack:
    """Return a string in XML format which contains all the Conditional
    attacks"""

    time = ""  # attack first occurrence time
    nodes = "" # list of involved nodes
    stmts = [] # list of actions
    var_dict = {} # dictionary of variables <name, XML string>
    packetFilter = "" # packet filter

    # t - time , n - nodes, v - variables, s - statements, f - packet filter
    def __init__(self, t, n, v, s, f):
        self.time = t
        self.nodes = n
        self.stmts = list(s)
        self.var_dict = dict(v)
        self.stmts = list(s)
        self.packetFilter = f

    def __str__(self):
        xml = '''\n<Attack>\n\t<start_time>%s</start_time>
		         \n\t<node>%s</node>''' %(self.time, self.nodes)

        for key in self.var_dict.keys():
            xml = xml + '\n\t<var><name>%s</name>%s</var>' %(str(key), 
                            str(self.var_dict[key]))

        xml = xml + '\n\t<filter>%s</filter>\n' %(self.packetFilter)
			
        for stmt in self.stmts:
            xml = xml + '\n%s' %(str(stmt))

        xml = xml+'\n</Attack>\n'
        return xml


class UnconditionalAttack:
    """Return a string in XML format which contains all the 
    Unconditional attacks"""

    time = "" # attack first occurrence time
    stmts = [] # list of actions
    var_dict = {} # dictionary of variables <name, XML string>
    frequency = "" # attack repetition frequency

    # t - time , f - frequency , v - variables, s - statements
    def __init__(self, t, f, v, s):
        self.time = t
        self.stmts = list(s)
        self.var_dict = dict(v)
        self.frequency = f

    def __str__(self):
        xml = '''\n<Attack>\n\t<start_time>%s</start_time>
                \n\t<frequency>%s</frequency>''' %(self.time, self.frequency)

        for key in self.var_dict.keys():
            xml = xml+'\n\t<var><name>%s</name>%s</var>' % (str(key), 
                        str(self.var_dict[key]))

        for stmt in self.stmts:
            xml = xml +'\n%s' %(str(stmt))

        xml = xml+'\n</Attack>\n'

        return xml

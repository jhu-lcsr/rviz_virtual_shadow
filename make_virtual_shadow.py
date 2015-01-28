#!/usr/bin/env python

"""
Read in a generated URDF XML
Add material tags to all links with XPATH
    xpath select //link/visual
    xpath set elem/material name="shadowblack"
        <texture filename="package://rviz_virtual_shadow/black.png"/>
"""

from __future__ import print_function

import xml.etree.ElementTree as ET
import rospy

def main():

    rospy.init_node('make_virtual_shadow')

    param_name = rospy.get_param('~model_param','/robot_description')
    robot_description = rospy.get_param(param_name)

    tree = ET.fromstring(robot_description)
    visuals = tree.findall('link/visual')

    for e in visuals:
        mat = e.find('material')
        if mat is not None:
            e.remove(mat)
        mat = ET.SubElement(e, 'material')
        mat.attrib['name'] = 'ShadowBlack'
        tex = ET.SubElement(mat, 'texture')
        tex.attrib['filename'] = "package://rviz_virtual_shadow/black.png"

    rospy.set_param(param_name+'_shadow',ET.tostring(tree))

    return 0

if __name__ == '__main__':
    main()

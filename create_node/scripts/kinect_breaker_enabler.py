#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2011, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import roslib
roslib.load_manifest('create_node')
import rospy
from create_node.srv import SetTurtlebotMode

service = 'turtlebot_node/set_operation_mode'

def set_to_full():
    '''
      This waits until it finds a serial connection and then sets the operation mode.
    '''
    rospy.init_node('io_mode_changer')
    rospy.wait_for_service(service)
    while True:
        try:
            service_proxy = rospy.ServiceProxy(service, SetTurtlebotMode)
            service_proxy(3)
            break
        except Exception:
            # Turtlebot node set_operation_node service will throw an exception
            # if it isn't serially connected
            # yet. Unfortunately it only throws a normal Exception (needs fixing)
            # and it would be better if it threw a particular exception so we could
            # handle the cases here
            rospy.sleep(3)
            continue

if __name__ == '__main__':
    try:
        set_to_full()
    except rospy.ROSInterruptException: pass
    except IOError: pass

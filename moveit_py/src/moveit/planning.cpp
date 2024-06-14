/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2022, Peter David Fagan
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of the copyright holder nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *********************************************************************/

/* Author: Peter David Fagan */

#include "moveit_ros/moveit_cpp/moveit_cpp.h"
#include "moveit_ros/moveit_cpp/planning_component.h"
#include "moveit_ros/planning_scene_monitor/planning_scene_monitor.h"
#include "moveit_ros/trajectory_execution_manager/trajectory_execution_manager.h"

PYBIND11_MODULE(planning, m)
{
  m.doc() = "Python bindings for moveit_cpp functionalities.";

  // Provide custom function signatures
  py::options options;
  options.disable_function_signatures();

  // Construct module classes
  moveit_py::bind_planning_component::initPlanRequestParameters(m);
  moveit_py::bind_planning_component::initMultiPlanRequestParameters(m);
  moveit_py::bind_planning_component::initPlanningComponent(m);
  moveit_py::bind_planning_scene_monitor::initPlanningSceneMonitor(m);
  moveit_py::bind_planning_scene_monitor::initContextManagers(m);
  moveit_py::bind_trajectory_execution_manager::initTrajectoryExecutionManager(m);
  moveit_py::bind_moveit_cpp::initMoveitPy(m);
}

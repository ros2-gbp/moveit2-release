%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-moveit-ros-planning
Version:        2.12.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_ros_planning package

License:        BSD-3-Clause
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       fmt-devel
Requires:       ros-rolling-ament-index-cpp
Requires:       ros-rolling-eigen3-cmake-module
Requires:       ros-rolling-generate-parameter-library
Requires:       ros-rolling-message-filters
Requires:       ros-rolling-moveit-common
Requires:       ros-rolling-moveit-core
Requires:       ros-rolling-moveit-msgs
Requires:       ros-rolling-moveit-ros-occupancy-map-monitor
Requires:       ros-rolling-pluginlib >= 1.11.2
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclcpp-action
Requires:       ros-rolling-rclcpp-components
Requires:       ros-rolling-srdfdom
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-tf2
Requires:       ros-rolling-tf2-eigen
Requires:       ros-rolling-tf2-geometry-msgs
Requires:       ros-rolling-tf2-msgs
Requires:       ros-rolling-tf2-ros
Requires:       ros-rolling-urdf
Requires:       ros-rolling-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  fmt-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ament-index-cpp
BuildRequires:  ros-rolling-eigen3-cmake-module
BuildRequires:  ros-rolling-generate-parameter-library
BuildRequires:  ros-rolling-message-filters
BuildRequires:  ros-rolling-moveit-common
BuildRequires:  ros-rolling-moveit-core
BuildRequires:  ros-rolling-moveit-msgs
BuildRequires:  ros-rolling-moveit-ros-occupancy-map-monitor
BuildRequires:  ros-rolling-pluginlib >= 1.11.2
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclcpp-action
BuildRequires:  ros-rolling-rclcpp-components
BuildRequires:  ros-rolling-srdfdom
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-tf2
BuildRequires:  ros-rolling-tf2-eigen
BuildRequires:  ros-rolling-tf2-geometry-msgs
BuildRequires:  ros-rolling-tf2-msgs
BuildRequires:  ros-rolling-tf2-ros
BuildRequires:  ros-rolling-urdf
BuildRequires:  ros-rolling-ros-workspace
Conflicts:      ros-rolling-moveit-ros-planning-interface < 2.1.5
Obsoletes:      ros-rolling-moveit-ros-planning-interface < 2.1.5
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-gmock
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-launch-testing-ament-cmake
BuildRequires:  ros-rolling-moveit-configs-utils
BuildRequires:  ros-rolling-moveit-resources-panda-moveit-config
BuildRequires:  ros-rolling-ros-testing
%endif

%description
Planning components of MoveIt that use ROS

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Fri Nov 29 2024 Henning Kayser <henningkayser@picknik.ai> - 2.12.0-1
- Autogenerated by Bloom

* Wed Sep 18 2024 Henning Kayser <henningkayser@picknik.ai> - 2.11.0-1
- Autogenerated by Bloom

* Fri Jun 14 2024 Henning Kayser <henningkayser@picknik.ai> - 2.10.0-1
- Autogenerated by Bloom

* Thu Mar 07 2024 Henning Kayser <henningkayser@picknik.ai> - 2.9.0-2
- Autogenerated by Bloom

* Wed Jan 10 2024 Henning Kayser <henningkayser@picknik.ai> - 2.9.0-1
- Autogenerated by Bloom

* Sun Sep 10 2023 Henning Kayser <henningkayser@picknik.ai> - 2.8.0-2
- Autogenerated by Bloom

* Sun Sep 10 2023 Henning Kayser <henningkayser@picknik.ai> - 2.8.0-1
- Autogenerated by Bloom

* Thu May 18 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.4-1
- Autogenerated by Bloom

* Mon Apr 24 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.3-1
- Autogenerated by Bloom

* Tue Apr 18 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.2-1
- Autogenerated by Bloom

* Thu Mar 23 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.1-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Henning Kayser <henningkayser@picknik.ai> - 2.7.0-2
- Autogenerated by Bloom


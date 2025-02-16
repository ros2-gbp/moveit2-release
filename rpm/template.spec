%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-moveit-ros-visualization
Version:        2.13.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_ros_visualization package

License:        BSD-3-Clause
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-geometric-shapes
Requires:       ros-rolling-interactive-markers
Requires:       ros-rolling-moveit-common
Requires:       ros-rolling-moveit-ros-planning-interface
Requires:       ros-rolling-moveit-ros-robot-interaction
Requires:       ros-rolling-moveit-ros-warehouse
Requires:       ros-rolling-object-recognition-msgs
Requires:       ros-rolling-pluginlib >= 1.11.2
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-rviz2
Requires:       ros-rolling-tf2-eigen
Requires:       ros-rolling-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  pkgconfig
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-class-loader
BuildRequires:  ros-rolling-geometric-shapes
BuildRequires:  ros-rolling-interactive-markers
BuildRequires:  ros-rolling-moveit-common
BuildRequires:  ros-rolling-moveit-ros-planning-interface
BuildRequires:  ros-rolling-moveit-ros-robot-interaction
BuildRequires:  ros-rolling-moveit-ros-warehouse
BuildRequires:  ros-rolling-object-recognition-msgs
BuildRequires:  ros-rolling-pluginlib >= 1.11.2
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-rviz2
BuildRequires:  ros-rolling-tf2-eigen
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Components of MoveIt that offer visualization

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
* Sun Feb 16 2025 Henning Kayser <henningkayser@picknik.ai> - 2.13.0-1
- Autogenerated by Bloom

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


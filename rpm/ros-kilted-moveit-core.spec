%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/kilted/.*$
%global __requires_exclude_from ^/opt/ros/kilted/.*$

%global __cmake_in_source_build 1

Name:           ros-kilted-moveit-core
Version:        2.13.2
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS moveit_core package

License:        BSD-3-Clause
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp-devel
Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       bullet-devel
Requires:       eigen3-devel
Requires:       fcl-devel
Requires:       octomap-devel
Requires:       ros-kilted-angles
Requires:       ros-kilted-common-interfaces
Requires:       ros-kilted-eigen-stl-containers
Requires:       ros-kilted-eigen3-cmake-module
Requires:       ros-kilted-generate-parameter-library
Requires:       ros-kilted-geometric-shapes
Requires:       ros-kilted-geometry-msgs
Requires:       ros-kilted-google-benchmark-vendor
Requires:       ros-kilted-kdl-parser
Requires:       ros-kilted-moveit-common
Requires:       ros-kilted-moveit-msgs
Requires:       ros-kilted-octomap-msgs
Requires:       ros-kilted-osqp-vendor
Requires:       ros-kilted-pluginlib
Requires:       ros-kilted-random-numbers
Requires:       ros-kilted-rclcpp
Requires:       ros-kilted-rsl
Requires:       ros-kilted-ruckig
Requires:       ros-kilted-sensor-msgs
Requires:       ros-kilted-shape-msgs
Requires:       ros-kilted-srdfdom
Requires:       ros-kilted-std-msgs
Requires:       ros-kilted-tf2
Requires:       ros-kilted-tf2-eigen
Requires:       ros-kilted-tf2-geometry-msgs
Requires:       ros-kilted-tf2-kdl
Requires:       ros-kilted-trajectory-msgs
Requires:       ros-kilted-urdf
Requires:       ros-kilted-urdfdom
Requires:       ros-kilted-urdfdom-headers
Requires:       ros-kilted-visualization-msgs
Requires:       ros-kilted-ros-workspace
BuildRequires:  assimp-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  bullet-devel
BuildRequires:  eigen3-devel
BuildRequires:  fcl-devel
BuildRequires:  octomap-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-kilted-ament-cmake
BuildRequires:  ros-kilted-angles
BuildRequires:  ros-kilted-common-interfaces
BuildRequires:  ros-kilted-eigen-stl-containers
BuildRequires:  ros-kilted-eigen3-cmake-module
BuildRequires:  ros-kilted-generate-parameter-library
BuildRequires:  ros-kilted-geometric-shapes
BuildRequires:  ros-kilted-geometry-msgs
BuildRequires:  ros-kilted-google-benchmark-vendor
BuildRequires:  ros-kilted-kdl-parser
BuildRequires:  ros-kilted-moveit-common
BuildRequires:  ros-kilted-moveit-msgs
BuildRequires:  ros-kilted-octomap-msgs
BuildRequires:  ros-kilted-osqp-vendor
BuildRequires:  ros-kilted-pluginlib
BuildRequires:  ros-kilted-random-numbers
BuildRequires:  ros-kilted-rclcpp
BuildRequires:  ros-kilted-rsl
BuildRequires:  ros-kilted-ruckig
BuildRequires:  ros-kilted-sensor-msgs
BuildRequires:  ros-kilted-shape-msgs
BuildRequires:  ros-kilted-srdfdom
BuildRequires:  ros-kilted-std-msgs
BuildRequires:  ros-kilted-tf2
BuildRequires:  ros-kilted-tf2-eigen
BuildRequires:  ros-kilted-tf2-geometry-msgs
BuildRequires:  ros-kilted-tf2-kdl
BuildRequires:  ros-kilted-trajectory-msgs
BuildRequires:  ros-kilted-urdf
BuildRequires:  ros-kilted-urdfdom
BuildRequires:  ros-kilted-urdfdom-headers
BuildRequires:  ros-kilted-visualization-msgs
BuildRequires:  ros-kilted-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-kilted-ament-cmake-gmock
BuildRequires:  ros-kilted-ament-cmake-google-benchmark
BuildRequires:  ros-kilted-ament-cmake-gtest
BuildRequires:  ros-kilted-ament-index-cpp
BuildRequires:  ros-kilted-launch-testing-ament-cmake
BuildRequires:  ros-kilted-moveit-resources-panda-moveit-config
BuildRequires:  ros-kilted-moveit-resources-pr2-description
BuildRequires:  ros-kilted-orocos-kdl-vendor
BuildRequires:  ros-kilted-rcl-interfaces
BuildRequires:  ros-kilted-rclpy
%endif

%description
Core libraries used by MoveIt

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/kilted" \
    -DAMENT_PREFIX_PATH="/opt/ros/kilted" \
    -DCMAKE_PREFIX_PATH="/opt/ros/kilted" \
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
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/kilted

%changelog
* Tue Apr 22 2025 Henning Kayser <henningkayser@picknik.ai> - 2.13.2-2
- Autogenerated by Bloom

* Wed Apr 16 2025 Henning Kayser <henningkayser@picknik.ai> - 2.13.2-1
- Autogenerated by Bloom

* Tue Apr 15 2025 Henning Kayser <henningkayser@picknik.ai> - 2.13.1-1
- Autogenerated by Bloom

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


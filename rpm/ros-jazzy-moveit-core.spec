%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-moveit-core
Version:        2.12.3
Release:        1%{?dist}%{?release_suffix}
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
Requires:       ros-jazzy-angles
Requires:       ros-jazzy-common-interfaces
Requires:       ros-jazzy-eigen-stl-containers
Requires:       ros-jazzy-eigen3-cmake-module
Requires:       ros-jazzy-generate-parameter-library
Requires:       ros-jazzy-geometric-shapes
Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-google-benchmark-vendor
Requires:       ros-jazzy-kdl-parser
Requires:       ros-jazzy-moveit-common
Requires:       ros-jazzy-moveit-msgs
Requires:       ros-jazzy-octomap-msgs
Requires:       ros-jazzy-osqp-vendor
Requires:       ros-jazzy-pluginlib
Requires:       ros-jazzy-random-numbers
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rsl
Requires:       ros-jazzy-ruckig
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-shape-msgs
Requires:       ros-jazzy-srdfdom
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-tf2
Requires:       ros-jazzy-tf2-eigen
Requires:       ros-jazzy-tf2-geometry-msgs
Requires:       ros-jazzy-tf2-kdl
Requires:       ros-jazzy-trajectory-msgs
Requires:       ros-jazzy-urdf
Requires:       ros-jazzy-urdfdom
Requires:       ros-jazzy-urdfdom-headers
Requires:       ros-jazzy-visualization-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  assimp-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  bullet-devel
BuildRequires:  eigen3-devel
BuildRequires:  fcl-devel
BuildRequires:  octomap-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-angles
BuildRequires:  ros-jazzy-common-interfaces
BuildRequires:  ros-jazzy-eigen-stl-containers
BuildRequires:  ros-jazzy-eigen3-cmake-module
BuildRequires:  ros-jazzy-generate-parameter-library
BuildRequires:  ros-jazzy-geometric-shapes
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-google-benchmark-vendor
BuildRequires:  ros-jazzy-kdl-parser
BuildRequires:  ros-jazzy-moveit-common
BuildRequires:  ros-jazzy-moveit-msgs
BuildRequires:  ros-jazzy-octomap-msgs
BuildRequires:  ros-jazzy-osqp-vendor
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-random-numbers
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rsl
BuildRequires:  ros-jazzy-ruckig
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-shape-msgs
BuildRequires:  ros-jazzy-srdfdom
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-tf2
BuildRequires:  ros-jazzy-tf2-eigen
BuildRequires:  ros-jazzy-tf2-geometry-msgs
BuildRequires:  ros-jazzy-tf2-kdl
BuildRequires:  ros-jazzy-trajectory-msgs
BuildRequires:  ros-jazzy-urdf
BuildRequires:  ros-jazzy-urdfdom
BuildRequires:  ros-jazzy-urdfdom-headers
BuildRequires:  ros-jazzy-visualization-msgs
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-gmock
BuildRequires:  ros-jazzy-ament-cmake-google-benchmark
BuildRequires:  ros-jazzy-ament-cmake-gtest
BuildRequires:  ros-jazzy-ament-index-cpp
BuildRequires:  ros-jazzy-launch-testing-ament-cmake
BuildRequires:  ros-jazzy-moveit-resources-panda-moveit-config
BuildRequires:  ros-jazzy-moveit-resources-pr2-description
BuildRequires:  ros-jazzy-orocos-kdl-vendor
BuildRequires:  ros-jazzy-rcl-interfaces
BuildRequires:  ros-jazzy-rclpy
%endif

%description
Core libraries used by MoveIt

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
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
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Tue Apr 15 2025 Henning Kayser <henningkayser@picknik.ai> - 2.12.3-1
- Autogenerated by Bloom

* Sun Feb 16 2025 Henning Kayser <henningkayser@picknik.ai> - 2.12.2-1
- Autogenerated by Bloom

* Wed Dec 18 2024 Henning Kayser <henningkayser@picknik.ai> - 2.12.1-1
- Autogenerated by Bloom

* Fri Nov 29 2024 Henning Kayser <henningkayser@picknik.ai> - 2.12.0-1
- Autogenerated by Bloom

* Fri Jun 14 2024 Henning Kayser <henningkayser@picknik.ai> - 2.10.0-1
- Autogenerated by Bloom

* Mon Apr 22 2024 Henning Kayser <henningkayser@picknik.ai> - 2.9.0-1
- Autogenerated by Bloom


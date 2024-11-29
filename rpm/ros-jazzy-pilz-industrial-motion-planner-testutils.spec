%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-pilz-industrial-motion-planner-testutils
Version:        2.12.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS pilz_industrial_motion_planner_testutils package

License:        BSD-3-Clause
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-eigen3-cmake-module
Requires:       ros-jazzy-moveit-common
Requires:       ros-jazzy-moveit-core
Requires:       ros-jazzy-moveit-msgs
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-eigen3-cmake-module
BuildRequires:  ros-jazzy-moveit-common
BuildRequires:  ros-jazzy-moveit-core
BuildRequires:  ros-jazzy-moveit-msgs
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-tf2-eigen
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Helper scripts and functionality to test industrial motion generation

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
* Fri Nov 29 2024 Christian Henkel <c.henkel@pilz.de> - 2.12.0-1
- Autogenerated by Bloom

* Fri Jun 14 2024 Christian Henkel <c.henkel@pilz.de> - 2.10.0-1
- Autogenerated by Bloom

* Mon Apr 22 2024 Christian Henkel <c.henkel@pilz.de> - 2.9.0-1
- Autogenerated by Bloom

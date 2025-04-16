%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-moveit-configs-utils
Version:        2.13.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_configs_utils package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-ament-index-python
Requires:       ros-rolling-launch
Requires:       ros-rolling-launch-param-builder
Requires:       ros-rolling-launch-ros
Requires:       ros-rolling-srdfdom
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Python library for loading moveit config parameters in launch files

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Apr 16 2025 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.13.2-1
- Autogenerated by Bloom

* Tue Apr 15 2025 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.13.1-1
- Autogenerated by Bloom

* Sun Feb 16 2025 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.13.0-1
- Autogenerated by Bloom

* Fri Nov 29 2024 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.12.0-1
- Autogenerated by Bloom

* Wed Sep 18 2024 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.11.0-1
- Autogenerated by Bloom

* Fri Jun 14 2024 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.10.0-1
- Autogenerated by Bloom

* Thu Mar 07 2024 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.9.0-2
- Autogenerated by Bloom

* Wed Jan 10 2024 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.9.0-1
- Autogenerated by Bloom

* Sun Sep 10 2023 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.8.0-2
- Autogenerated by Bloom

* Sun Sep 10 2023 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.8.0-1
- Autogenerated by Bloom

* Thu May 18 2023 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.7.4-1
- Autogenerated by Bloom

* Mon Apr 24 2023 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.7.3-1
- Autogenerated by Bloom

* Tue Apr 18 2023 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.7.2-1
- Autogenerated by Bloom

* Thu Mar 23 2023 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.7.1-1
- Autogenerated by Bloom

* Tue Mar 21 2023 MoveIt Release Team <moveit_releasers@googlegroups.com> - 2.7.0-2
- Autogenerated by Bloom


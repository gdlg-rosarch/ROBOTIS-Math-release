Name:           ros-kinetic-robotis-math
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS robotis_math package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/robotis_math
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-kinetic-roscpp
BuildRequires:  eigen3-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roscpp

%description
This package is a set of basic math fuctions for ROBOTIS's robots. We provide
some linear algebra and trajectory generation funntions and classes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Sep 29 2016 pyo <pyo@robotis.com> - 0.2.2-0
- Autogenerated by Bloom

* Fri Sep 02 2016 pyo <pyo@robotis.com> - 0.2.1-0
- Autogenerated by Bloom

* Wed Aug 31 2016 pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

* Wed Aug 17 2016 pyo <pyo@robotis.com> - 0.1.0-0
- Autogenerated by Bloom


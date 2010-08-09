%define rev     2034

Name:           telepathy-sharp
Version:        0.13.2
Release:        %mkrel -c svn%rev 3
Summary:        .NET package containing proxy classes for use in clients 

Group:          System/Libraries
License:        MIT
URL:            http://tapioca-voip.sourceforge.net/wiki/index.php/SubProjects
Source0:        %{name}-rev%rev.tar.bz2
Patch: telepathy-sharp-dir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires:  mono-devel
BuildRequires:  gnome-common
BuildRequires:  ndesk-dbus-devel

%description
Telepathy-sharp is a .NET package containing proxy classes for use in clients. 

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Telepathy-sharp is a .NET package containing proxy classes for use in clients. 

%prep
%setup -q -n %name
%patch
./autogen.sh

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig INdT_Telepathydir=%_prefix/lib/mono/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_prefix}/lib/mono/gac/INdT.Telepathy/
%{_prefix}/lib/mono/telepathy-sharp/INdT.Telepathy.dll

%files devel
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/telepathy-sharp.pc

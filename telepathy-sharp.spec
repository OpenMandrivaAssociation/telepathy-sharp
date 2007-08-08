%define rev     2034

Name:           telepathy-sharp
Version:        0.0
Release:        %mkrel 0.svn%rev.1
Summary:        Telepathy-sharp is a .NET package containing proxy classes for use in clients 

Group:          Networking/Instant messaging
License:        LGPL
URL:            http://tapioca-voip.sourceforge.net/wiki/index.php/SubProjects
Source0:        %{name}-rev%rev.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  mono-devel
BuildRequires:  gnome-common
BuildRequires:  ndesk-dbus

%description

Telepathy-sharp is a .NET package containing proxy classes for use in clients. 

%files
%defattr(-,root,root,-)
%{_libdir}/mono/gac/INdT.Telepathy/*/INdT.Telepathy.dll
%{_libdir}/mono/gac/INdT.Telepathy/*/INdT.Telepathy.dll.mdb
%{_libdir}/telepathy-sharp/INdT.Telepathy.dll
%{_libdir}/pkgconfig/telepathy-sharp.pc

#--------------------------------------------------------------------

%prep
%setup -q -n %name


%build
sh ./autogen.sh
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

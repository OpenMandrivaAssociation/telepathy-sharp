%define rev     2034

Name:           telepathy-sharp
Version:        0.13.2
Release:        %mkrel -c svn%rev 4
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


%changelog
* Sun Aug 14 2011 Götz Waschk <waschk@mandriva.org> 0.13.2-0.svn2034.4mdv2012.0
+ Revision: 694491
- rebuild

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.13.2-0.svn2034.3mdv2011.0
+ Revision: 567920
- split out devel package
- update build deps

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.13.2-0.svn2034.2mdv2011.0
+ Revision: 170576
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 27 2007 Götz Waschk <waschk@mandriva.org> 0.13.2-0.svn2034.2mdv2008.0
+ Revision: 71870
- fix dir in pkgconfig file

* Thu Aug 09 2007 Götz Waschk <waschk@mandriva.org> 0.13.2-0.svn2034.1mdv2008.0
+ Revision: 60815
- use the right version
- make it a proper noarch package
- fix License
- fix file list

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Import telepathy-sharp


%define		trac_ver	0.11
%define		plugin		paste
Summary:	Pastebin Plugin for Trac
Name:		trac-plugin-%{plugin}
Version:	0.2.2
Release:	0.1
License:	BSD-like / GPL / ...
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/tracpasteplugin?old_path=/&format=zip#/trac%{plugin}plugin.zip
# Source0-md5:	a3245291029bc84636eaa2de9e6dc877
URL:		http://trac-hacks.org/wiki/TracPastePlugin
BuildRequires:	python-devel
Requires:	python-pygments > 0.5
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n trac%{plugin}plugin
mv %{trac_ver}/* .

%build
%{__python} setup.py build
%{__python} setup.py egg_info

ver=$(awk '$1 == "Version:" {print $2}' *.egg-info/PKG-INFO)
test "$ver" = %{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
# XXX: try to figure out from .egg-info / __init__py at build time
#trac-enableplugin "%{plugin}.Trac%{plugin}Module"

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/trac%{plugin}
%{py_sitescriptdir}/*-*.egg-info

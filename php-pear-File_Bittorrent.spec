%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Bittorrent
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Decode and Encode data in Bittorrent format
Summary(pl.UTF-8):	%{_pearname} - Kodowanie i dekodowanie danych w formacie Bittorent
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a4c7b7380450b65b80d2a1880a612f1f
URL:		http://pear.php.net/package/File_Bittorrent/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.2
Requires:	php-pear-PHP_Compat >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package consists of two classes which handles the encoding and
decoding of data in Bittorrent format.

You can also extract useful informations from .torrent files.

Usage Example:
<http://m.tacker.org/pear/File_Bittorrent/example.phps>

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza dwie klasy obsługujące kodowanie i dekodowanie
danych w formacie Bittorent.

Można także wydobyć wiele przydatnych informacji z plików .torrent.

Przykład użycia:
<http://m.tacker.org/pear/File_Bittorrent/example.phps>

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*

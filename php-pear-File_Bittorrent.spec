%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Bittorrent
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Decode and Encode data in Bittorrent format
Summary(pl):	%{_pearname} - Kodowanie i dekodowanie danych w formacie Bittorent
Name:		php-pear-%{_pearname}
Version:	1.0.0
%define	_rc RC2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	1058c11cf549d492b38a3708e872d7dc
URL:		http://pear.php.net/package/File_Bittorrent/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PHP_Compat >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package consists of two classes which handles the encoding and
decoding of data in Bittorrent format.

You can also extract useful informations from .torrent files.

Usage Example
http://m.tacker.org/pear/File_Bittorrent/example.phps

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza dwie klasy obs³uguj±ce kodowanie i dekodowanie
danych w formacie Bittorent.

Mo¿na tak¿e wydobyæ wiele przydatnych informacji z plików .torrent.

Przyk³ad u¿ycia:
http://m.tacker.org/pear/File_Bittorrent/example.phps

Ta klasa ma w PEAR status: %{_status}.

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

%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Bittorrent
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Decode and Encode data in Bittorrent format
Summary(pl):	%{_pearname} - Kodowanie i dekodowanie danych w formacie Bittorent
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2ba4a617603fd8958ea4ea7a68b11878
URL:		http://pear.php.net/package/File_Bittorrent/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{example.php,freebsd.torrent}
%{php_pear_dir}/%{_class}/%{_subclass}

# centos/sclo spec file for php-tidy
#
# Copyright (c) 2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%if 0%{?scl:1}
%if "%{scl}" == "rh-php56"
%global sub_prefix sclo-php56-
%else
%global sub_prefix %{scl_prefix}
%endif
%scl_package        php-tidy
%else
%global pkg_name    %{name}
%endif

%global pecl_name  tidy
%global ini_name   20-%{pecl_name}.ini

Name:           %{?sub_prefix}php-%{pecl_name}
Summary:        Standard PHP module provides tidy library support
Version:        5.6.25
Release:        1%{?dist}
Source0:        http://www.php.net/distributions/php-%{version}.tar.bz2

License:        PHP
Group:          Development/Languages
URL:            http://php.net/%{pecl_name}

BuildRequires:  %{?scl_prefix}php-devel >= 5.6.25
BuildRequires:  libtidy-devel

%if "%{?scl_prefix}" != "%{?sub_prefix}"
Provides:      %{?scl_prefix}php-%{pecl_name}          = %{version}-%{release}
Provides:      %{?scl_prefix}php-%{pecl_name}%{?_isa}  = %{version}-%{release}
%endif

Requires:       %{?scl_prefix}php(zend-abi) = %{php_zend_api}
Requires:       %{?scl_prefix}php(api) = %{php_core_api}


%description
The %{name} package contains a dynamic shared object that will
add support for using the tidy library to PHP.

Package built for PHP %(%{__php} -r 'echo PHP_MAJOR_VERSION.".".PHP_MINOR_VERSION;')%{?scl: as Software Collection (%{scl} by %{?scl_vendor}%{!?scl_vendor:rh})}.


%prep
%setup -q -n php-%{version}

# Configuration file
cat << 'EOF' | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF


%build
cd ext/%{pecl_name}

%{_bindir}/phpize
%configure \
    --with-tidy \
    --with-libdir=%{_lib} \
    --with-php-config=%{_bindir}/php-config

make %{?_smp_mflags}


%install
# Install the NTS stuff
make -C ext/%{pecl_name} install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}


%check
cd ext/%{pecl_name}

# can load the module
%{_bindir}/php -n \
    -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    -m | grep %{pecl_name}

# Upstream test suite
export NO_INTERACTION=1
export REPORT_EXIT_STATUS=1
make test 


%files
%license LICENSE
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Thu Mar  9 2017 Remi Collet <remi@remirepo.net> - 5.6.25-1
- initial package
- version 5.6.25

